#!/usr/bin/env python3
"""Pubblica su Instagram (e sulla Pagina Facebook) i post in scadenza di social/calendario.json.

Uso:
  python scripts/pubblica_ig.py              pubblica i post con orario passato (ora di Roma)
  python scripts/pubblica_ig.py --dry-run    mostra cosa pubblicherebbe, senza chiamate di rete
  python scripts/pubblica_ig.py --verifica   controlla token, account Instagram e Pagina (sola lettura)

Variabili d'ambiente:
  IG_TOKEN     token utente di sistema Meta (non scade)
  IG_ID        ID dell'account Instagram (@cozzus_run_coach)
  FB_PAGE_ID   facoltativo: ID della Pagina Facebook; se manca si pubblica solo su Instagram
  SALVA_GIT=1  nel workflow: salva lo stato del calendario con commit e push a ogni passaggio

Calendario: {"fuso": "Europe/Rome", "post": [voce, ...]}. Ogni voce:
  id          identificativo unico, es. "2026-11-02-consiglio-tallone"
  quando      "AAAA-MM-GGTHH:MM" ora di Roma
  tipo        image | carousel | reel | story
  media       lista di URL pubblici (https://cozzuscoach.it/social/media/...): JPEG per le immagini, MP4 per i video
  didascalia  testo del post (ignorato per le storie)
  copertina   facoltativo, solo reel: URL JPEG della copertina
  fb          facoltativo, default true (false per le storie): pubblica anche sulla Pagina Facebook
  stato       bozza | programmato | in_corso | pubblicato | errore
Campi scritti dallo script: ig_id, fb_id, fb_errore, pubblicato_il, tentativi, errore.

Regole:
  - esce solo ciò che è "programmato" (o "errore" con meno di 3 tentativi); "bozza" non esce mai
  - prima della pubblicazione la voce passa a "in_corso" e lo stato viene salvato: se il workflow si interrompe
    a metà la voce resta "in_corso" e NON viene ritentata (evita doppie pubblicazioni): va controllata a mano
  - un errore durante la pubblicazione vera e propria (media_publish) non viene ritentato, per lo stesso motivo
  - se un media non è ancora online (GitHub Pages in ritardo) la voce aspetta il giro successivo
  - token non valido (errore 190): il workflow fallisce in modo visibile
  - un errore su Facebook non blocca Instagram: finisce in fb_errore
"""
import datetime, json, os, subprocess, sys, time, urllib.error, urllib.parse, urllib.request
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAL = os.path.join(ROOT, "social", "calendario.json")
TZ = ZoneInfo("Europe/Rome")
G = "https://graph.facebook.com/" + os.environ.get("IG_API_VERSION", "v26.0")
MAX_TENTATIVI = 3
ATTESA_MEDIA_ORE = 6  # oltre questo ritardo un media mancante diventa errore


class TokenError(RuntimeError):
    pass


class Pubblicazione(RuntimeError):
    """Errore nella fase finale: non si ritenta, il post potrebbe essere uscito."""


# ---------------------------------------------------------------- rete
def call(method, path, **params):
    params["access_token"] = os.environ["IG_TOKEN"]
    q = urllib.parse.urlencode(params)
    url = f"{G}/{path}" + (f"?{q}" if method == "GET" else "")
    req = urllib.request.Request(url, data=None if method == "GET" else q.encode(), method=method)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")[:400]
        try:
            code = json.loads(body).get("error", {}).get("code")
        except ValueError:
            code = None
        if code == 190:
            raise TokenError(f"token non valido o revocato (190): {body}")
        raise RuntimeError(f"HTTP {e.code} su {path.split('?')[0]}: {body}")


def online(url):
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "cozzuscoach-social"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status == 200
    except Exception:
        return False


def attendi(cid, limite=600):
    t0 = time.time()
    while time.time() - t0 < limite:
        s = call("GET", cid, fields="status_code").get("status_code")
        if s == "FINISHED":
            return
        if s in ("ERROR", "EXPIRED"):
            raise RuntimeError(f"elaborazione del media fallita ({s})")
        time.sleep(10)
    raise RuntimeError("elaborazione del media troppo lunga")


def is_video(url):
    return url.lower().split("?")[0].endswith(".mp4")


# ---------------------------------------------------------------- Instagram
def contenitore_ig(post, ig):
    tipo, media, cap = post["tipo"], post["media"], post.get("didascalia", "")
    if tipo == "image":
        cid = call("POST", f"{ig}/media", image_url=media[0], caption=cap)["id"]
    elif tipo == "carousel":
        if not 2 <= len(media) <= 10:
            raise RuntimeError("un carosello va da 2 a 10 elementi")
        figli = []
        for u in media:
            p = {"is_carousel_item": "true"}
            p.update({"media_type": "VIDEO", "video_url": u} if is_video(u) else {"image_url": u})
            figli.append(call("POST", f"{ig}/media", **p)["id"])
        for f in figli:
            attendi(f, 300)
        cid = call("POST", f"{ig}/media", media_type="CAROUSEL", children=",".join(figli), caption=cap)["id"]
    elif tipo == "reel":
        extra = {"cover_url": post["copertina"]} if post.get("copertina") else {}
        cid = call("POST", f"{ig}/media", media_type="REELS", video_url=media[0], caption=cap, share_to_feed="true", **extra)["id"]
    elif tipo == "story":
        key = "video_url" if is_video(media[0]) else "image_url"
        cid = call("POST", f"{ig}/media", media_type="STORIES", **{key: media[0]})["id"]
    else:
        raise RuntimeError(f"tipo sconosciuto: {tipo}")
    attendi(cid)
    return cid


def pubblica_ig(post, ig):
    cid = contenitore_ig(post, ig)
    try:
        return call("POST", f"{ig}/media_publish", creation_id=cid)["id"]
    except TokenError:
        raise
    except Exception as e:
        raise Pubblicazione(str(e))


# ---------------------------------------------------------------- Facebook
_page_token = {}


def page_token(page):
    if page not in _page_token:
        _page_token[page] = call("GET", page, fields="access_token")["access_token"]
    return _page_token[page]


def fb_call(page, method, path, **params):
    saved = os.environ["IG_TOKEN"]
    os.environ["IG_TOKEN"] = page_token(page)
    try:
        return call(method, path, **params)
    finally:
        os.environ["IG_TOKEN"] = saved


def pubblica_fb(post, page):
    tipo, media, cap = post["tipo"], post["media"], post.get("didascalia", "")
    if tipo == "image":
        return fb_call(page, "POST", f"{page}/photos", url=media[0], message=cap)["post_id"]
    if tipo == "carousel":
        foto = [u for u in media if not is_video(u)]
        ids = [fb_call(page, "POST", f"{page}/photos", url=u, published="false")["id"] for u in foto]
        att = {f"attached_media[{i}]": json.dumps({"media_fbid": x}) for i, x in enumerate(ids)}
        return fb_call(page, "POST", f"{page}/feed", message=cap, **att)["id"]
    if tipo == "reel":
        return fb_call(page, "POST", f"{page}/videos", file_url=media[0], description=cap)["id"]
    raise RuntimeError(f"tipo non pubblicabile su Facebook: {tipo}")


# ---------------------------------------------------------------- calendario
def carica():
    with open(CAL, encoding="utf-8") as f:
        return json.load(f)


TOCCATI = {}  # id -> voce modificata da questa esecuzione


def scrivi(cal):
    with open(CAL, "w", encoding="utf-8") as f:
        json.dump(cal, f, ensure_ascii=False, indent=2)
        f.write("\n")


def salva(cal, msg, post=None):
    """Salva il calendario. Con SALVA_GIT=1 fa commit e push su main, unendo per id le voci
    aggiunte nel frattempo da altri (il contenuto settimanale) senza perderle."""
    if post is not None:
        TOCCATI[post["id"]] = post
    scrivi(cal)
    if os.environ.get("SALVA_GIT") != "1":
        return
    git = lambda *a: subprocess.run(["git", *a], cwd=ROOT, check=True, capture_output=True, text=True)
    for _ in range(4):
        try:
            git("fetch", "--depth=1", "origin", "main")
            git("reset", "--hard", "FETCH_HEAD")
            remoto = carica()
            nostre = TOCCATI
            ids_remoti = {p["id"] for p in remoto["post"]}
            remoto["post"] = [nostre.get(p["id"], p) for p in remoto["post"]] + [p for i, p in nostre.items() if i not in ids_remoti]
            cal["post"] = remoto["post"]
            scrivi(cal)
            git("add", "social/calendario.json")
            if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT).returncode == 0:
                return
            git("commit", "-m", f"social: {msg}")
            git("push", "origin", "HEAD:main")
            return
        except subprocess.CalledProcessError as e:
            print("salvataggio non riuscito, riprovo:", (e.stderr or "")[-200:], file=sys.stderr)
            time.sleep(5)
    raise RuntimeError("impossibile salvare il calendario su GitHub")


def pronto(post):
    st = post.get("stato")
    return st == "programmato" or (st == "errore" and post.get("tentativi", 0) < MAX_TENTATIVI and not post.get("non_ritentare"))


def verifica():
    ig, page = os.environ["IG_ID"], os.environ.get("FB_PAGE_ID")
    print("::notice::verifica Instagram (IG_ID lungo", len(ig), "cifre)")
    print("Instagram:", call("GET", ig, fields="username,name,followers_count,media_count"))
    print("::notice::Instagram ok")
    print("Limite pubblicazioni:", call("GET", f"{ig}/content_publishing_limit", fields="quota_usage,config")["data"])
    if page:
        print("::notice::verifica Pagina (FB_PAGE_ID lungo", len(page), "cifre)")
        print("Pagina:", call("GET", page, fields="name,followers_count"))
        page_token(page)
        print("::notice::Pagina Facebook ok")


def main():
    args = sys.argv[1:]
    dry = "--dry-run" in args
    if not dry and not (os.environ.get("IG_TOKEN") and os.environ.get("IG_ID")):
        sys.exit("Mancano IG_TOKEN o IG_ID nei secret del repository.")
    if "--verifica" in args:
        return verifica()

    cal = carica()
    adesso = datetime.datetime.now(TZ)
    ig, page = os.environ.get("IG_ID", ""), os.environ.get("FB_PAGE_ID", "")
    in_scadenza = [p for p in cal["post"] if pronto(p)
                   and datetime.datetime.fromisoformat(p["quando"]).replace(tzinfo=TZ) <= adesso]
    bloccati = [p["id"] for p in cal["post"] if p.get("stato") == "in_corso"]
    if bloccati:
        print("ATTENZIONE: voci rimaste 'in_corso' (controllare a mano se sono uscite):", ", ".join(bloccati))
    if not in_scadenza:
        print(f"{adesso:%Y-%m-%d %H:%M}: niente da pubblicare")
        return 0

    rc = 0
    for post in sorted(in_scadenza, key=lambda p: p["quando"]):
        if dry:
            print(f"[dry-run] {post['id']} {post['tipo']} {post['quando']} -> {post['media']}")
            continue
        mancanti = [u for u in post["media"] + ([post["copertina"]] if post.get("copertina") else []) if not online(u)]
        if mancanti:
            ritardo = adesso - datetime.datetime.fromisoformat(post["quando"]).replace(tzinfo=TZ)
            if ritardo < datetime.timedelta(hours=ATTESA_MEDIA_ORE):
                print(f"{post['id']}: media non ancora online, riprovo al prossimo giro: {mancanti}")
                continue
            post["stato"], post["errore"], post["non_ritentare"] = "errore", f"media non raggiungibili: {mancanti}", True
            salva(cal, f"errore {post['id']}", post)
            rc = 1
            continue

        post["stato"] = "in_corso"
        post["tentativi"] = post.get("tentativi", 0) + 1
        post.pop("errore", None)
        salva(cal, f"in pubblicazione {post['id']}", post)
        try:
            post["ig_id"] = pubblica_ig(post, ig)
            post["stato"], post["pubblicato_il"] = "pubblicato", datetime.datetime.now(TZ).isoformat(timespec="minutes")
            print(f"Instagram: pubblicato {post['id']} ({post['ig_id']})")
        except TokenError as e:
            post["stato"], post["errore"] = "errore", str(e)[:300]
            post["tentativi"] -= 1  # non è colpa del post
            salva(cal, f"errore token {post['id']}", post)
            print("!!! TOKEN NON VALIDO: rigenerarlo e aggiornare il secret IG_TOKEN.", e, file=sys.stderr)
            return 2
        except Pubblicazione as e:
            post["stato"], post["errore"], post["non_ritentare"] = "errore", "fase finale: " + str(e)[:280], True
            rc = 1
        except Exception as e:
            post["stato"], post["errore"] = "errore", str(e)[:300]
            rc = 1
        if post["stato"] == "pubblicato" and page and post.get("fb", post["tipo"] != "story"):
            try:
                post["fb_id"] = pubblica_fb(post, page)
                print(f"Facebook: pubblicato {post['id']} ({post['fb_id']})")
            except Exception as e:
                post["fb_errore"] = str(e)[:300]
                print(f"::warning::Facebook non pubblicato {post['id']}: {str(e)[:300]}")
        salva(cal, f"{post['stato']} {post['id']}", post)
        if post["stato"] == "errore":
            print(f"::error::{post['id']}: {post['errore']}")
    return rc


if __name__ == "__main__":
    for k in ("IG_TOKEN", "IG_ID", "FB_PAGE_ID"):  # spazi o a capo incollati per sbaglio nei secret
        if k in os.environ:
            os.environ[k] = "".join(os.environ[k].split())
    try:
        rc = main()
    except Exception as e:
        print(f"::error::{type(e).__name__}: {str(e)[:500]}")  # visibile nel riepilogo del workflow
        raise
    if rc == 2:
        print("::error::Token Meta non valido: rigenerarlo e aggiornare il secret IG_TOKEN")
    sys.exit(rc)
