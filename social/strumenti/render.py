"""Grafiche Cozzu's Coach: storie 1080x1920 e caroselli 1080x1350, renderizzate con Playwright.
Uso da Python: render([spec, ...]) -> salva JPEG in spec["out"]."""
import html, os
from playwright.sync_api import sync_playwright

SOCIAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.path.join(SOCIAL, "libreria")
TMP = os.environ.get("COZZUS_TMP", "/tmp/cozzus")
os.makedirs(TMP, exist_ok=True)
F = f"file://{SOCIAL}/risorse/fonts"
FOCAL = {  # punto da tenere al centro del ritaglio (x, y in frazioni)
    "03": (.62, .5), "04": (.72, .35), "06": (.55, .5), "07": (.72, .45), "08": (.5, .7), "14": (.55, .6),
    "15": (.62, .55), "17": (.5, .45), "20": (.55, .5), "23": (.6, .5), "25": (.5, .6), "31": (.55, .5),
    "36": (.6, .6), "38": (.35, .6), "39": (.6, .5), "41": (.45, .5), "42": (.5, .5), "43": (.5, .55),
    "44": (.5, .55), "45": (.45, .5), "46": (.55, .45), "48": (.68, .5), "51": (.55, .4), "53": (.5, .5),
    "54": (.5, .5), "60": (.45, .5), "13": (.55, .6), "22": (.55, .75), "24": (.25, .7), "28": (.55, .5),
    "56": (.65, .55), "58": (.6, .6), "21": (.5, .6), "16": (.5, .4), "59": (.5, .45), "47": (.5, .4),
    "55": (.5, .35), "52": (.5, .6), "57": (.55, .5), "35": (.5, .7), "11": (.5, .55),
}
C = dict(sea="#0A5C73", light="#0D7A96", deep="#073F50", sky="#DDF0F4", sun="#F2A93B", ink="#15222A", grey="#5B6B73", bg="#EEF3F4")

CSS = f"""
@font-face{{font-family:B;src:url({F}/Barlow-Regular.ttf);font-weight:400}}
@font-face{{font-family:B;src:url({F}/Barlow-Medium.ttf);font-weight:500}}
@font-face{{font-family:B;src:url({F}/Barlow-SemiBold.ttf);font-weight:600}}
@font-face{{font-family:B;src:url({F}/Barlow-Bold.ttf);font-weight:700}}
@font-face{{font-family:BC;src:url({F}/BarlowCondensed-SemiBold.ttf);font-weight:600}}
@font-face{{font-family:BC;src:url({F}/BarlowCondensed-Bold.ttf);font-weight:700}}
@font-face{{font-family:BC;src:url({F}/BarlowCondensed-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:BC;src:url({F}/BarlowCondensed-Black.ttf);font-weight:900}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:{C['deep']};color:#fff;font-family:B,sans-serif}}
.c{{font-family:BC,sans-serif}}
.frame{{position:relative;overflow:hidden}}
.ph{{position:absolute;inset:0;background-size:cover}}
.kick{{display:inline-block;background:{C['sun']};color:{C['deep']};font-family:BC;font-weight:800;letter-spacing:.12em;text-transform:uppercase;padding:12px 22px}}
.brand{{font-family:BC;font-weight:800;letter-spacing:.16em;text-transform:uppercase}}
.brand i{{display:inline-block;width:.55em;height:.55em;border-radius:50%;background:{C['sun']};margin-right:.45em;vertical-align:.08em}}
"""


def ph(photo, extra=""):
    x, y = FOCAL.get(photo, (.5, .5))
    return f'<div class="ph" style="background-image:url({LIB}/foto/{photo}.jpg);background-position:{x*100:.0f}% {y*100:.0f}%;{extra}"></div>'


def esc(s):
    return html.escape(s or "").replace("\n", "<br>")


def story(s):
    W, H = 1080, 1920
    lab, title, body = esc(s.get("label")), esc(s.get("title")), esc(s.get("body"))
    big = s.get("big")
    shade = "linear-gradient(180deg,rgba(7,63,80,.55) 0%,rgba(7,63,80,.05) 28%,rgba(7,63,80,.15) 45%,rgba(7,63,80,.93) 70%,rgba(7,63,80,.98) 100%)"
    bigh = f'<div class="c" style="font-weight:900;font-size:{s.get("bigsize",230)}px;line-height:.9;color:{C["sun"]};margin-bottom:18px">{esc(big)}</div>' if big else ""
    items = "".join(f'<div style="display:flex;gap:22px;align-items:baseline;margin-top:20px"><span class="c" style="font-weight:800;color:{C["sun"]};font-size:46px;min-width:46px">{i+1}</span><span style="font-size:42px;font-weight:500;line-height:1.3">{esc(t)}</span></div>' for i, t in enumerate(s.get("items", [])))
    note = f'<div style="margin-top:34px;font-size:30px;color:{C["sky"]};opacity:.9">{esc(s["note"])}</div>' if s.get("note") else ""
    return W, H, f"""
<div class="frame" style="width:{W}px;height:{H}px">{ph(s['photo'])}
<div style="position:absolute;inset:0;background:{shade}"></div>
<div style="position:absolute;left:80px;top:150px"><span class="kick" style="font-size:34px">{lab}</span></div>
<div style="position:absolute;left:80px;right:80px;bottom:230px">
  {bigh}
  <div class="c" style="font-weight:800;font-size:{s.get('tsize',96)}px;line-height:.98;text-transform:uppercase">{title}</div>
  <div style="width:110px;height:9px;background:{C['sun']};margin:34px 0 30px"></div>
  <div style="font-size:{s.get('bsize',44)}px;line-height:1.35;font-weight:500">{body}</div>{items}{note}
</div>
<div style="position:absolute;left:80px;right:80px;bottom:110px;display:flex;justify-content:space-between;align-items:center">
  <span class="brand" style="font-size:34px"><i></i>Cozzu's Coach</span><span style="font-size:30px;font-weight:600;color:{C['sky']}">cozzuscoach.it</span>
</div></div>"""


def cover(s):
    W, H = 1080, 1350
    shade = "linear-gradient(180deg,rgba(7,63,80,.35) 0%,rgba(7,63,80,0) 30%,rgba(7,63,80,.2) 50%,rgba(7,63,80,.95) 82%)"
    return W, H, f"""
<div class="frame" style="width:{W}px;height:{H}px">{ph(s['photo'])}
<div style="position:absolute;inset:0;background:{shade}"></div>
<div style="position:absolute;left:72px;top:72px;right:72px;display:flex;justify-content:space-between;align-items:center">
  <span class="kick" style="font-size:30px">{esc(s.get('label'))}</span><span class="brand" style="font-size:30px"><i></i>Cozzu's Coach</span></div>
<div style="position:absolute;left:72px;right:72px;bottom:80px">
  <div class="c" style="font-weight:900;font-size:{s.get('tsize',124)}px;line-height:.9;text-transform:uppercase">{esc(s['title'])}</div>
  <div style="width:110px;height:9px;background:{C['sun']};margin:30px 0 26px"></div>
  <div style="display:flex;justify-content:space-between;align-items:flex-end;gap:30px">
   <div style="font-size:40px;line-height:1.3;font-weight:500;color:{C['sky']}">{esc(s.get('sub'))}</div>
   <div class="c" style="font-weight:800;font-size:34px;letter-spacing:.1em;white-space:nowrap">SCORRI →</div></div>
</div></div>"""


def point(s):
    W, H = 1080, 1350
    n = s.get("n")
    num = f'<div class="c" style="position:absolute;left:72px;top:600px;width:150px;height:150px;background:{C["sun"]};color:{C["deep"]};font-weight:900;font-size:110px;line-height:150px;text-align:center">{n}</div>' if n else ""
    return W, H, f"""
<div class="frame" style="width:{W}px;height:{H}px;background:{C['deep']}">
<div class="frame" style="position:absolute;left:0;top:0;width:{W}px;height:680px">{ph(s['photo'])}</div>
{num}
<div style="position:absolute;left:72px;right:72px;top:{790 if n else 740}px">
  <div class="c" style="font-weight:800;font-size:{s.get('tsize',78)}px;line-height:1;text-transform:uppercase">{esc(s['title'])}</div>
  <div style="font-size:{s.get('bsize',40)}px;line-height:1.38;margin-top:26px;color:#fff;font-weight:500">{esc(s['body'])}</div>
</div>
<div style="position:absolute;left:72px;right:72px;bottom:52px;display:flex;justify-content:space-between;font-size:26px;color:{C['sky']}">
  <span class="brand"><i></i>Cozzu's Coach</span><span>{esc(s.get('foot',''))}</span></div>
</div>"""


def cta(s):
    W, H = 1080, 1350
    shade = "linear-gradient(180deg,rgba(10,92,115,.45) 0%,rgba(10,92,115,.85) 45%,rgba(7,63,80,.97) 100%)"
    note = f'<div style="font-size:26px;color:{C["sky"]};margin-top:40px;line-height:1.35">{esc(s["note"])}</div>' if s.get("note") else ""
    return W, H, f"""
<div class="frame" style="width:{W}px;height:{H}px">{ph(s['photo'])}
<div style="position:absolute;inset:0;background:{shade}"></div>
<div style="position:absolute;left:72px;right:72px;top:90px"><span class="brand" style="font-size:32px"><i></i>Cozzu's Coach</span></div>
<div style="position:absolute;left:72px;right:72px;bottom:90px">
  <div class="c" style="font-weight:900;font-size:{s.get('tsize',104)}px;line-height:.92;text-transform:uppercase">{esc(s['title'])}</div>
  <div style="font-size:40px;line-height:1.35;margin:30px 0 44px;color:{C['sky']};font-weight:500">{esc(s.get('body'))}</div>
  <span class="c" style="display:inline-block;background:{C['sun']};color:{C['deep']};font-weight:800;font-size:50px;text-transform:uppercase;padding:24px 38px">Richiedi il tuo programma</span>
  <div style="font-size:34px;font-weight:600;margin-top:26px">cozzuscoach.it · oppure scrivici in DM</div>{note}
</div></div>"""


def overlay(s):
    """Testo trasparente per i reel (1080x1920)."""
    W, H = 1080, 1920
    pos = s.get("pos", "bottom")
    top = "top:300px" if pos == "top" else ("top:760px" if pos == "mid" else "bottom:330px")
    k = f'<span class="kick" style="font-size:34px;margin-bottom:26px">{esc(s["label"])}</span><br>' if s.get("label") else ""
    sub = f'<div style="font-size:46px;font-weight:600;margin-top:22px;line-height:1.3;text-shadow:0 2px 14px rgba(0,0,0,.6)">{esc(s["sub"])}</div>' if s.get("sub") else ""
    btn = f'<div style="margin-top:36px"><span class="c" style="display:inline-block;background:{C["sun"]};color:{C["deep"]};font-weight:800;font-size:52px;text-transform:uppercase;padding:22px 36px">Richiedi il tuo programma</span><div style="font-size:38px;font-weight:600;margin-top:22px;text-shadow:0 2px 14px rgba(0,0,0,.6)">cozzuscoach.it · DM</div></div>' if s.get("cta") else ""
    if pos == "bottom":
        shade = "background:linear-gradient(180deg,rgba(7,63,80,0) 0%,rgba(7,63,80,0) 40%,rgba(7,63,80,.75) 100%);"
    elif pos == "top":
        shade = "background:linear-gradient(180deg,rgba(7,63,80,.82) 0%,rgba(7,63,80,.6) 26%,rgba(7,63,80,0) 46%,rgba(7,63,80,0) 82%,rgba(7,63,80,.5) 100%);"
    else:
        shade = "background:rgba(7,63,80,.5);"
    return W, H, f"""
<div class="frame" style="width:{W}px;height:{H}px;background:transparent">
<div style="position:absolute;inset:0;{shade}"></div>
<div style="position:absolute;left:80px;right:80px;{top}">{k}
 <div class="c" style="font-weight:900;font-size:{s.get('tsize',112)}px;line-height:.95;text-transform:uppercase;text-shadow:0 4px 24px rgba(0,0,0,.45)">{esc(s['title'])}</div>{sub}{btn}</div>
<div style="position:absolute;left:80px;bottom:110px" class="brand"><span style="font-size:34px;text-shadow:0 2px 12px rgba(0,0,0,.5)"><i></i>Cozzu's Coach</span></div>
</div>"""


KINDS = dict(story=story, cover=cover, point=point, cta=cta, overlay=overlay)


def render(specs):
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        for s in specs:
            W, H, body = KINDS[s["kind"]](s)
            transp = s["kind"] == "overlay"
            css = CSS + ("html,body{background:transparent!important}" if transp else "")
            pg.set_viewport_size({"width": W, "height": H})
            tmp = os.path.join(TMP, "_r.html")
            with open(tmp, "w", encoding="utf-8") as fh:
                fh.write(f"<!doctype html><html><head><meta charset=utf-8><style>{css}</style></head><body>{body}</body></html>")
            pg.goto("file://" + tmp)
            pg.wait_for_load_state("load")
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(100)
            out = s["out"]
            os.makedirs(os.path.dirname(out), exist_ok=True)
            if transp:
                pg.screenshot(path=out, omit_background=True)
            else:
                pg.screenshot(path=out, type="jpeg", quality=90)
        b.close()
