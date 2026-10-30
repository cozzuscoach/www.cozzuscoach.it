"""Funzioni comuni per produrre una settimana di contenuti."""
import json, os, sys
from render import render, LIB, TMP, SOCIAL
from reel import reel

MED = f"{SOCIAL}/media"
URL = "https://cozzuscoach.it/social/media/"
clip = lambda i: f"{LIB}/video/{i:02d}.mp4"
ONLY = sys.argv[1:]  # per rifare solo alcune voci

HT = "#cozzuscoach #corsa #running #runningitalia #salento #salentorunning #puglia #runner #allenamento"
CTA = "\n\n👉 Richiedi il tuo programma: link in bio o scrivici in DM."
ORIENT = "\n\nIndicazioni di orientamento: non sostituiscono il parere di un medico o di un fisioterapista."

posts = []  # voci del calendario


def add(pid, quando, tipo, files, didascalia="", copertina=None):
    v = dict(id=pid, quando=quando, tipo=tipo, media=[URL + os.path.basename(f) for f in files], stato="bozza")
    if didascalia:
        v["didascalia"] = didascalia
    if copertina:
        v["copertina"] = URL + os.path.basename(copertina)
    posts.append(v)


def go(pid):
    return not ONLY or any(pid.startswith(o) for o in ONLY)


def carosello(pid, quando, slides, didascalia):
    files = [f"{MED}/{pid}-{i+1}.jpg" for i in range(len(slides))]
    if go(pid):
        render([dict(s, out=f) for s, f in zip(slides, files)])
    add(pid, quando, "carousel", files, didascalia)


def storia(pid, quando, spec):
    f = f"{MED}/{pid}.jpg"
    if go(pid):
        render([dict(spec, out=f)])
    add(pid, quando, "story", [f])


def video(pid, quando, segs, didascalia, **kw):
    if go(pid):
        out, cov = reel(pid, segs, MED, **kw)
    else:
        out, cov = f"{MED}/{pid}.mp4", f"{MED}/{pid}-copertina.jpg"
    add(pid, quando, "reel", [out], didascalia, cov)




def salva(nome):
    posts.sort(key=lambda p: p["quando"])
    json.dump(posts, open(f"{TMP}/{nome}.json", "w"), ensure_ascii=False, indent=1)
    print(len(posts), "voci")
