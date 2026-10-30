"""Reel 1080x1920: segmenti di clip (ritagliati 9:16) + testo in sovrimpressione + musica sintetizzata."""
import os, subprocess, numpy as np, wave
from render import render, LIB, TMP

SR = 44100


def _env(n, a=0.005, r=0.2):
    t = np.arange(n) / SR
    return np.minimum(1, t / a) * np.exp(-t / r)


def musica(path, dur, bpm=100, seed=0, mood="up"):
    """Base strumentale semplice e originale: cassa, clap, charleston, basso e accordi."""
    rng = np.random.default_rng(seed)
    n = int(dur * SR); out = np.zeros(n + 6 * SR)
    beat = 60 / bpm; t = lambda s: int(s * SR)
    prog = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]] if mood == "up" else [[57, 60, 64], [53, 57, 60], [55, 59, 62], [52, 55, 59]]
    hz = lambda m: 440 * 2 ** ((m - 69) / 12)
    nb = int(dur / beat) + 1
    for b in range(nb):
        s = t(b * beat)
        # cassa
        L = t(.35); tt = np.arange(L) / SR; f = 50 + 70 * np.exp(-tt * 30)
        out[s:s + L] += .9 * np.sin(2 * np.pi * np.cumsum(f) / SR) * _env(L, .001, .12)
        # clap sui tempi 2 e 4
        if b % 2 == 1:
            L = t(.2); out[s:s + L] += .28 * rng.standard_normal(L) * _env(L, .001, .05)
        # charleston in ottavi
        for h in (0, .5):
            L = t(.05); hs = s + t(h * beat)
            x = rng.standard_normal(L); x = np.diff(np.concatenate([[0], x]))
            out[hs:hs + L] += .10 * x * _env(L, .0005, .015)
        # basso e accordi, un accordo per battuta da 4
        ch = prog[(b // 4) % 4]
        L = t(beat * .9); tt = np.arange(L) / SR
        out[s:s + L] += .30 * np.sin(2 * np.pi * hz(ch[0] - 12) * tt) * _env(L, .01, .35)
        if b % 4 == 0:
            L = t(beat * 4); tt = np.arange(L) / SR
            pad = sum(np.sin(2 * np.pi * hz(m) * tt) + .3 * np.sin(4 * np.pi * hz(m) * tt) for m in ch)
            out[s:s + L] += .06 * pad * np.minimum(1, tt / .3) * np.exp(-tt / 3)
    out = out[:n]
    fade = int(1.2 * SR); out[-fade:] *= np.linspace(1, 0, fade); out[:int(.05 * SR)] *= np.linspace(0, 1, int(.05 * SR))
    out = out / np.max(np.abs(out)) * .8
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((out * 32767).astype(np.int16).tobytes())


def reel(name, segs, outdir, bpm=100, seed=0, mood="up"):
    """segs: [{clip: path, start: s, dur: s, fx: 0..1 (centro orizzontale del ritaglio), text: {overlay spec}}]"""
    work = os.path.join(TMP, "_reel", name); os.makedirs(work, exist_ok=True)
    render([dict(kind="overlay", out=f"{work}/o{i}.png", **s["text"]) for i, s in enumerate(segs)])
    parts = []
    for i, s in enumerate(segs):
        fx = s.get("fx", .5)
        vf = (f"scale=-2:1920,crop=1080:1920:'(iw-1080)*{fx}':0,setsar=1,fps=30" if not s.get("vertical")
              else "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30")
        if s.get("slow"):
            vf += f",setpts={1/s['slow']}*PTS"
        p = f"{work}/p{i}.mp4"
        fl = (f"[0:v]{vf},eq=saturation=1.05[v];[v][1:v]overlay=0:0:format=auto,"
              f"fade=t=in:st=0:d=0.25,fade=t=out:st={s['dur']-0.25}:d=0.25[o]")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(s.get("start", 0)), "-t", str(s["dur"] / s.get("slow", 1) + .5 if s.get("slow") else s["dur"]),
                        "-i", s["clip"], "-loop", "1", "-i", f"{work}/o{i}.png", "-filter_complex", fl, "-map", "[o]",
                        "-t", str(s["dur"]), "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", p], check=True)
        parts.append(p)
    with open(f"{work}/list.txt", "w") as f:
        f.writelines(f"file '{p}'\n" for p in parts)
    dur = sum(s["dur"] for s in segs)
    musica(f"{work}/m.wav", dur, bpm, seed, mood)
    out = os.path.join(outdir, f"{name}.mp4"); cover = os.path.join(outdir, f"{name}-copertina.jpg")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{work}/list.txt", "-i", f"{work}/m.wav",
                    "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p",
                    "-r", "30", "-c:a", "aac", "-b:a", "128k", "-ar", "44100", "-movflags", "+faststart", "-shortest", out], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", "0.6", "-i", out, "-frames:v", "1", "-q:v", "3", cover], check=True)
    return out, cover
