#!/usr/bin/env python3
"""Pubblica su Instagram i post in scadenza di social/calendario.json.

Uso:
  python scripts/pubblica_ig.py                 pubblica i post con data passata (ora di Roma)
  python scripts/pubblica_ig.py --dry-run       mostra cosa pubblicherebbe, senza chiamate di rete
  python scripts/pubblica_ig.py --rinnova-token rinnova il token e aggiorna il secret IG_TOKEN (richiede GH_PAT)

Variabili d'ambiente: IG_TOKEN, IG_ID, IG_API_VERSION (default v21.0), GH_PAT e GH_REPO (solo per il rinnovo).
Il calendario è un JSON con campi: id, quando (ISO locale di Roma), tipo (image|reel|story|carousel),
media (lista di URL pubblici su GitHub Pages), didascalia, stato (programmato|pubblicato|errore), ig_id, errore.
"""
import json, os, sys, time, urllib.parse, urllib.request, datetime, subprocess
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAL = os.path.join(ROOT, "social", "calendario.json")
TZ = ZoneInfo("Europe/Rome")
API = os.environ.get("IG_API_VERSION", "v21.0")
BASE = f"https://graph.instagram.com/{API}"


def call(method, url, params=None):
    data = None
    if method == "POST":
        data = urllib.parse.urlencode(params or {}).encode()
    else:
        url = url + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(url, data=data, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code}: {e.read().decode()[:300]}")


def attendi(container_id, token):
    # i Reel vanno elaborati prima della pubblicazione
    for _ in range(60):
        s = call("GET", f"{BASE}/{container_id}", {"fields": "status_code", "access_token": token})
        code = s.get("status_code")
        if code == "FINISHED":
            return
        if code in ("ERROR", "EXPIRED"):
            raise RuntimeError(f"elaborazione media fallita: {code}")
        time.sleep(10)
    raise RuntimeError("elaborazione media troppo lunga")


def pubblica(post, token, ig_id):
    tipo, media = post["tipo"], post["media"]
    if tipo == "carousel":
        figli = []
        for url in media:
            c = call("POST", f"{BASE}/{ig_id}/media", {"image_url": url, "is_carousel_item": "true", "access_token": token})
            figli.append(c["id"])
        params = {"media_type": "CAROUSEL", "children": ",".join(figli), "caption": post.get("didascalia", ""), "access_token": token}
        cid = call("POST", f"{BASE}/{ig_id}/media", params)["id"]
    elif tipo == "reel":
        cid = call("POST", f"{BASE}/{ig_id}/media", {"media_type": "REELS", "video_url": media[0],
                   "caption": post.get("didascalia", ""), "access_token": token})["id"]
        attendi(cid, token)
    elif tipo == "story":
        key = "video_url" if media[0].lower().endswith(".mp4") else "image_url"
        cid = call("POST", f"{BASE}/{ig_id}/media", {"media_type": "STORIES", key: media[0], "access_token": token})["id"]
        if key == "video_url":
            attendi(cid, token)
    else:  # image
        cid = call("POST", f"{BASE}/{ig_id}/media", {"image_url": media[0], "caption": post.get("didascalia", ""), "access_token": token})["id"]
    time.sleep(2)
    return call("POST", f"{BASE}/{ig_id}/media_publish", {"creation_id": cid, "access_token": token})["id"]


def rinnova_token():
    token = os.environ["IG_TOKEN"]
    r = call("GET", "https://graph.instagram.com/refresh_access_token",
             {"grant_type": "ig_refresh_token", "access_token": token})
    nuovo, giorni = r["access_token"], r.get("expires_in", 0) // 86400
    pat, repo = os.environ.get("GH_PAT"), os.environ.get("GH_REPO")
    if not pat or not repo:
        raise SystemExit("Token rinnovato ma GH_PAT non impostato: aggiorna IG_TOKEN a mano.")
    subprocess.run(["gh", "secret", "set", "IG_TOKEN", "--repo", repo, "--body", nuovo],
                   check=True, env={**os.environ, "GH_TOKEN": pat})
    print(f"Token rinnovato: valido per circa {giorni} giorni. Secret aggiornato.")


def main():
    if "--rinnova-token" in sys.argv:
        return rinnova_token()
    dry = "--dry-run" in sys.argv
    cal = json.load(open(CAL, encoding="utf-8"))
    adesso = datetime.datetime.now(TZ)
    token, ig_id = os.environ.get("IG_TOKEN", ""), os.environ.get("IG_ID", "")
    if not dry and (not token or not ig_id):
        raise SystemExit("Mancano IG_TOKEN o IG_ID nei secret del repository.")
    fatti = 0
    for post in cal["post"]:
        if post.get("stato") != "programmato":
            continue
        quando = datetime.datetime.fromisoformat(post["quando"]).replace(tzinfo=TZ)
        if quando > adesso:
            continue
        if dry:
            print(f"[dry-run] {post['id']} {post['tipo']} alle {post['quando']} -> {post['media']}")
            continue
        try:
            post["ig_id"] = pubblica(post, token, ig_id)
            post["stato"], post["pubblicato_il"] = "pubblicato", adesso.isoformat(timespec="seconds")
            fatti += 1
            print(f"pubblicato {post['id']}")
        except Exception as e:
            post["stato"], post["errore"] = "errore", str(e)
            print(f"errore {post['id']}: {e}", file=sys.stderr)
    if not dry:
        with open(CAL, "w", encoding="utf-8") as f:
            json.dump(cal, f, ensure_ascii=False, indent=2)
            f.write("\n")
    print(f"fatto: {fatti} pubblicati")


if __name__ == "__main__":
    main()
