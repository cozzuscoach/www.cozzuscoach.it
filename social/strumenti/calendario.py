#!/usr/bin/env python3
"""Gestione di social/calendario.json.

  python social/strumenti/calendario.py aggiungi FILE.json        aggiunge o sostituisce voci (per id), mai quelle già pubblicate
  python social/strumenti/calendario.py approva [DA] [A]          bozza -> programmato per le date AAAA-MM-GG comprese (default: tutte)
  python social/strumenti/calendario.py stato                     riepilogo per giorno
  python social/strumenti/calendario.py pulisci [GIORNI]          elimina i media delle voci pubblicate da più di GIORNI (default 10)
"""
import datetime, json, os, sys

SOCIAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAL = os.path.join(SOCIAL, "calendario.json")


def carica():
    return json.load(open(CAL, encoding="utf-8"))


def scrivi(cal):
    cal["post"].sort(key=lambda p: p["quando"])
    with open(CAL, "w", encoding="utf-8") as f:
        json.dump(cal, f, ensure_ascii=False, indent=2)
        f.write("\n")


def main(a):
    cal = carica()
    if a[0] == "aggiungi":
        nuove = json.load(open(a[1], encoding="utf-8"))
        idx = {p["id"]: i for i, p in enumerate(cal["post"])}
        for v in nuove:
            if v["id"] in idx:
                if cal["post"][idx[v["id"]]].get("stato") in ("pubblicato", "in_corso"):
                    print("già pubblicata, non la tocco:", v["id"]); continue
                cal["post"][idx[v["id"]]] = v
            else:
                cal["post"].append(v)
        scrivi(cal); print(len(nuove), "voci aggiunte o aggiornate")
    elif a[0] == "approva":
        da, al = (a[1], a[2] if len(a) > 2 else a[1]) if len(a) > 1 else ("0000", "9999")
        n = 0
        for p in cal["post"]:
            if p.get("stato") == "bozza" and da <= p["quando"][:10] <= al:
                p["stato"] = "programmato"; n += 1
        scrivi(cal); print(n, "voci programmate")
    elif a[0] == "stato":
        giorni = {}
        for p in cal["post"]:
            giorni.setdefault(p["quando"][:10], []).append(f'{p["quando"][11:]} {p["tipo"]:<8} {p["stato"]}')
        for g, r in sorted(giorni.items()):
            print(g); print("  " + "\n  ".join(r))
    elif a[0] == "pulisci":
        limite = (datetime.date.today() - datetime.timedelta(days=int(a[1]) if len(a) > 1 else 10)).isoformat()
        tolti = 0
        for p in cal["post"]:
            if p.get("stato") == "pubblicato" and p["quando"][:10] < limite and not p.get("media_rimossi"):
                for u in p["media"] + ([p["copertina"]] if p.get("copertina") else []):
                    f = os.path.join(SOCIAL, "media", u.rsplit("/", 1)[1])
                    if os.path.exists(f):
                        os.remove(f); tolti += 1
                p["media_rimossi"] = True
        scrivi(cal); print(tolti, "file rimossi")
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:] or ["stato"])
