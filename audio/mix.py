#!/usr/bin/env python3
"""Score, foley and narration for "What Happened to Rochester? The City Kodak Built" → out/mix.wav (48 kHz stereo). Timing from ../film.json.

A SCORE THAT REWINDS. One theme (the "button theme", an 8-bar parlour tune in F major) is the spine, and the music travels back
through its own history as the story does:
  hook, frame 10  — the theme REVERSED: reverse-piano swells over a cold synth pad in D minor
  frames 9–7      — the electric decades: vibraphone, pad, a pulsing piano; fragments of the theme, never finished
  frame 8         — low strings; deep hits under the implosions
  frame 6         — the peak: warm strings and vibraphone in F major, the first four bars, cut off
  frame 5         — the lab: pizzicato bass, glockenspiel blips, a Lydian question mark
  frame 4         — mid-century lush: strings, harp, clarinet sings six bars
  frame 3         — string quartet and piano (Kodachrome came from a pianist and a violinist); a flute whistles the tune;
                    under Eastman's death a single low cello note, no swell
  frame 2         — parlour upright with a ragtime lilt and clarinet; seven bars, left hanging on C7
  frame 1         — music box and upright: the whole theme, resolved, for the first time
  epilogue        — a fast-forward chirp, then the theme slower on piano and strings; the music box alone on the end card
Between frames the last moments of music are TAPE-REWOUND (reversed, accelerating) under the motor whir of the strip.
Foley (series set): soft shutter on picture cut-ins, paper for cards, low thump on each frame card, quiet room tone; plus projector
clicks for the slide tray, deep booms for the implosions, cassette motor, counter clicks. Music ducks ≈ 8 dB under the voice."""
import json, os, sys
import numpy as np, soundfile as sf, soxr
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.environ.get('LIB') or os.path.expanduser('~/lemo-opuscar'); sys.path.insert(0, LIB)
from core.audio import sampler as S
from core.audio.sfx import SR, add, bp, hp, lp, noise, env_exp, t_, thump, norm, limit, brown, click
F = json.load(open(os.path.join(D, 'film.json'), encoding='utf-8')); DUR = F['dur']; SC = F['scenes']; VO = {v['id']: v for v in F['voice']}
N = int(DUR * SR); S.seed(5); np.random.seed(5)
BPM = 72; BEAT = 60 / BPM; BAR = 4 * BEAT
ev = []; rev_notes = []   # rev_notes: (t_end, inst, pitch, dur, vel, pan, gain) — rendered, reversed, placed so they END at t_end
def E(t, inst, p, d, v=.6, pan=0, g=.3, **k): ev.append(dict(t=t, inst=inst, pitch=p, dur=d, vel=v, pan=pan, gain=g, **k))
def oc(n, k): return n[:-1] + str(int(n[-1]) + k)
# the theme: (beat from the start of bar 1, pitch, beats)
THEME = [(0, 'A4', 1), (1, 'C5', 1), (2, 'F5', 2), (4, 'E5', 1), (5, 'D5', 1), (6, 'A4', 2), (8, 'A#4', 1), (9, 'D5', 1), (10, 'F5', 1.5), (11.5, 'E5', .5),
         (12, 'D5', 1), (13, 'C5', 3), (16, 'A4', 1), (17, 'C5', 1), (18, 'F5', 1.5), (19.5, 'G5', .5), (20, 'A5', 1), (21, 'G5', 1), (22, 'F5', 1), (23, 'D5', 1),
         (24, 'C5', 1), (25, 'D5', .5), (25.5, 'E5', .5), (26, 'G5', 1), (27, 'E5', 1), (28, 'F5', 4)]
THEME_CH = ['F', 'Dm', 'Bb', 'C', 'F', 'Bb', 'C7', 'F']
CH = {'F': ('F2', ['A3', 'C4', 'F4']), 'Dm': ('D2', ['A3', 'D4', 'F4']), 'Bb': ('A#1', ['A#3', 'D4', 'F4']), 'C': ('C2', ['G3', 'C4', 'E4']), 'C7': ('C2', ['A#3', 'C4', 'E4']),
      'Gm': ('G1', ['A#3', 'D4', 'G4']), 'A': ('A1', ['A3', 'C#4', 'E4']), 'Am': ('A1', ['A3', 'C4', 'E4']), 'G': ('G1', ['G3', 'B3', 'D4']),
      'Fmaj7#11': ('F2', ['A3', 'B3', 'E4']), 'Eb': ('D#2', ['G3', 'A#3', 'D#4'])}
def theme(t0, inst, bars=(1, 8), tempo=1.0, v=.55, g=.3, oct_=0, pan=.1, reverse=False, stac=False):
    b0 = (bars[0] - 1) * 4; b1 = bars[1] * 4
    for b, p, n in THEME:
        if b0 <= b < b1:
            tt = t0 + (b - b0) * BEAT / tempo; dd = (.25 if stac else n * .95) * BEAT / tempo; pp = oc(p, oct_)
            if reverse: rev_notes.append((tt + dd + .3, inst, pp, dd, v, pan, g))
            else: E(tt, inst, pp, dd, v, pan, g)
def bars_in(a, b, length=BAR):
    t, i = a, 0
    while t < b - .5: yield t, i; t += length; i += 1

# ── chapter spans: each counter card starts a frame; the music of a frame begins with the narrator on the card (t0 + 2.0) ──
cards = [s for s in SC if s['type'] == 'counter']
spans = [('hook', 0.0, cards[0]['t0'])] + [(c['frame'], c['t0'], (cards[i + 1]['t0'] if i + 1 < len(cards) else DUR)) for i, c in enumerate(cards)]
title = next(s for s in SC if s['type'] == 'title'); endcard = next(s for s in SC if s['type'] == 'end')
def line(i): return VO[i]['t'], VO[i]['t'] + VO[i]['d']

def pad(a, b, notes, g=.06, bright=900):   # a soft synth pad (detuned saws, low-passed) — the modern colour
    n = int((b - a) * SR); tt = np.arange(n) / SR; y = np.zeros(n)
    for p in notes:
        f = S.hz(p)
        for det in (-.004, .0, .005): y += np.sign(np.sin(2 * np.pi * f * (1 + det) * tt)) * .3 + np.sin(2 * np.pi * f * (1 + det) * tt)
    y = lp(y, bright, 2); env = np.minimum(1, np.minimum(tt / 2.5, (tt[-1] - tt) / 2.5 + 1e-9)); return (y * env * g / len(notes)).astype(np.float32)
PADS = []   # (t0, array)

for name, a, b in spans:
    m0 = a + 2.0 if name != 'hook' else 2.9
    if name == 'hook':
        PADS.append((2.9, pad(2.9, title['t0'], ['D3', 'A3', 'F4'], .05, 700)))
        for t, i in bars_in(4.0, title['t0'] - 1, BAR * 2):
            ch = ['Dm', 'Bb', 'Gm', 'A'][i % 4]; bb, cc = CH[ch]
            rev_notes.append((t + BAR * 2 - .2, 'piano', cc[1], 1.6, .5, -.2, .32)); rev_notes.append((t + BAR * 2 - .2, 'piano', oc(bb, 1), 1.6, .45, .1, .28))
        theme(title['t0'] - 16 * BEAT - 2, 'piano', (1, 4), reverse=True, v=.5, g=.3, oct_=0)
        # the title: strings and a soft timpani in D minor, opening into F
        E(title['t0'], 'timpani', 'D2', 2.5, .5, 0, .35); E(title['t0'], 'cellos', 'D3', 4.5, .5, -.2, .2, attack=.8); E(title['t0'], 'violas', 'A3', 4.5, .45, .1, .16, attack=.8)
        E(title['t0'], 'violins', 'F4', 4.5, .45, .3, .14, attack=.8); E(title['t0'] + 2.2, 'horn', 'A3', 2.8, .45, 0, .2, attack=.3)
    elif name == 'f10':
        PADS.append((m0, pad(m0, b - .3, ['D3', 'A3', 'F4'], .05, 650)))
        for t, i in bars_in(m0, b - .5, BAR * 2):
            ch = ['Dm', 'Bb', 'Gm', 'A'][i % 4]; bb, cc = CH[ch]
            for j, p in enumerate(cc): rev_notes.append((t + BAR * 2 - .15, 'piano', p, 2.0, .45, -.3 + .3 * j, .22))
            rev_notes.append((t + BAR * 2 - .15, 'piano', oc(bb, 1), 2.0, .45, 0, .24))
            if i % 2 == 1: theme(t, 'piano', (1, 2), reverse=True, v=.45, g=.22, oct_=1)
    elif name == 'f9':
        PADS.append((m0, pad(m0, b - .3, ['F3', 'C4', 'A4'], .04, 900)))
        for t, i in bars_in(m0, b - .5):
            ch = ['Dm', 'Bb', 'F', 'C'][i % 4]; bb, cc = CH[ch]
            for k in range(8): E(t + k * BEAT / 2, 'vibraphone', oc(cc[k % 3], 1 if k % 4 == 3 else 0), 1.2, .38, -.3 + .2 * (k % 3), .18)
            E(t, 'contrabass', bb if bb[-1] != '1' else oc(bb, 1), BAR, .4, -.1, .12, attack=.3)
            if i % 4 == 2: theme(t, 'glockenspiel', (1, 2), v=.35, g=.12, oct_=1)
    elif name == 'f8':
        for t, i in bars_in(m0, b - .5, BAR * 2):
            ch = ['Dm', 'Bb', 'Dm', 'A'][i % 4]; bb, cc = CH[ch]
            E(t, 'cellos', oc(bb, 1) if bb[-1] == '1' else bb, BAR * 2 + .4, .4, -.2, .2, attack=1.0); E(t, 'violas', cc[0], BAR * 2 + .4, .35, .2, .1, attack=1.2)
            for k in (0, 3, 5): E(t + k * BEAT, 'piano', oc(cc[k % 3], 1), 2.2, .3, .2, .16)
        for s in SC:
            if s['type'] == 'implode' and a <= s['t0'] < b:
                tb = s['t0'] + (-s.get('boom', -.35)) * s['vd'] if s.get('boom', -.35) < 0 else s['t0'] + s['boom']
                E(tb, 'gran_cassa', 'hit', None, .9, 0, .8); E(tb + .05, 'timpani', 'D2', 3, .8, 0, .5); E(tb + .4, 'gong', None, None, .35, 0, .25)
    elif name == 'f7':
        PADS.append((m0, pad(m0, b - .3, ['A2', 'E3', 'C4'], .035, 800)))
        sad = line('d08')[0]
        for t, i in bars_in(m0, b - .5):
            ch = (['C', 'G', 'Am', 'F'] if t < sad else ['Am', 'F', 'Dm', 'Am'])[i % 4]; bb, cc = CH[ch]
            for k in range(8): E(t + k * BEAT / 2, 'piano', cc[(k * 2) % 3] if k % 2 else oc(cc[0], 0), .5, .32 + .06 * (k % 2 == 0), .15 - .1 * (k % 2), .15)
            E(t, 'cellos_pizz', oc(bb, 1) if bb[-1] == '1' else bb, .8, .5, -.2, .25)
            if t < sad and i % 4 == 1: theme(t, 'vibraphone', (1, 2), v=.45, g=.2, oct_=0)
    elif name == 'f6':
        for t, i in bars_in(m0, b - .5):
            ch = ['F', 'Dm', 'Bb', 'C'][i % 4]; bb, cc = CH[ch]
            for j, p in enumerate(cc): E(t, ('violas', 'violins', 'violins')[j], oc(p, 0), BAR + .3, .45, -.3 + .3 * j, .14, attack=.4)
            E(t, 'cellos', bb if bb[-1] != '1' else oc(bb, 1), BAR + .3, .45, -.2, .18, attack=.3)
            for k in range(4): E(t + k * BEAT, 'vibraphone', cc[k % 3], 1.5, .32, .2, .12)
        theme(m0 + BAR * 2, 'horn', (1, 4), v=.5, g=.22, oct_=-1); theme(m0 + BAR * 10, 'vibraphone', (1, 4), v=.5, g=.2)
    elif name == 'f5':
        q = line('q02')[0]
        for t, i in bars_in(m0, b - .5):
            cool = t > q; ch = (['Fmaj7#11', 'Fmaj7#11', 'Dm', 'C'] if not cool else ['Dm', 'Bb', 'Dm', 'A'])[i % 4]; bb, cc = CH[ch]
            for k in range(4): E(t + k * BEAT, 'contrabass_pizz', oc(bb, 1) if k % 2 == 0 and bb[-1] == '1' else bb if k % 2 == 0 else cc[0][:-1] + '2', .6, .5, -.15, .32 if not cool else .2)
            for j, p in enumerate(cc): E(t, 'vibraphone_bowed', p, BAR, .35, -.2 + .2 * j, .1)
            if not cool and i % 2 == 0:
                for k, p in enumerate(['C6', 'E6', 'B5', 'G5', 'E6']): E(t + BEAT * (1.5 + k * .5), 'glockenspiel', p, .4, .3, .35, .1)
        theme(line('g06')[0], 'glockenspiel', (1, 2), v=.4, g=.14, oct_=1, stac=True)
    elif name == 'f4':
        for t, i in bars_in(m0, b - .5):
            ch = ['F', 'Dm', 'Bb', 'C7'][i % 4]; bb, cc = CH[ch]
            for j, p in enumerate(cc): E(t, ('violas', 'violins', 'violins')[j], p, BAR + .4, .45, -.3 + .3 * j, .15, attack=.5)
            E(t, 'cellos', bb if bb[-1] != '1' else oc(bb, 1), BAR + .4, .45, -.2, .2, attack=.4)
            for k, p in enumerate([bb if bb[-1] != '1' else oc(bb, 1)] + cc + [oc(cc[1], 1), oc(cc[2], 1)]): E(t + k * BEAT * .5, 'harp', oc(p, 1) if k else p, 2.0, .4, -.2 + .08 * k, .2)
        theme(m0 + BAR * 4, 'clarinet', (1, 6), v=.5, g=.26, oct_=-1)
    elif name == 'f3':
        dth = line('k06'); whistle = line('k11')[0]
        for t, i in bars_in(m0, b - .5):
            if dth[0] - 1.5 < t + BAR and t < dth[1] + 1.0: continue
            ch = ['F', 'Am', 'Bb', 'C'][i % 4]; bb, cc = CH[ch]
            E(t, 'cellos', bb if bb[-1] != '1' else oc(bb, 1), BAR + .3, .4, -.25, .2, attack=.4); E(t, 'violas', cc[0], BAR + .3, .38, .05, .12, attack=.4)
            for k in (0, 2): E(t + k * BEAT, 'piano', oc(cc[1], 0), 1.5, .32, .2, .13); E(t + k * BEAT + BEAT, 'piano', oc(cc[2], 0), 1.0, .28, .25, .1)
        E(dth[0] - .5, 'cellos', 'F2', dth[1] - dth[0] + 2.5, .3, -.1, .16, attack=1.5)   # Eastman's death: one low note, no swell
        theme(m0 + BAR * 2, 'violin', (1, 4), v=.45, g=.2)
        theme(whistle, 'flute', (1, 2), v=.45, g=.22, oct_=0)
    elif name == 'f2':
        tt0 = m0; last = None
        for t, i in bars_in(m0, b - .5):
            ch = ['F', 'Bb', 'F', 'C7'][i % 4]; bb, cc = CH[ch]
            E(t, 'contrabass_pizz', bb if bb[-1] != '1' else oc(bb, 1), .9, .5, -.1, .4); E(t + 2 * BEAT, 'contrabass_pizz', oc(bb, 1) if bb[-1] == '1' else bb, .9, .45, -.1, .34)
            for k in (1, 3):
                for j, p in enumerate(cc): E(t + k * BEAT, 'upright', p, .5, .48, -.2 + .2 * j, .26)
        theme(m0 + BAR * 3, 'clarinet', (1, 7), v=.5, g=.26, oct_=-1)
    elif name == 'f1':
        end1 = line('p12')[1] + 1.0; ts = end1 - 7 * BAR
        for t, i in bars_in(m0, ts - .2, BAR):
            ch = ['F', 'Dm', 'Bb', 'C'][i % 4]; bb, cc = CH[ch]
            for k, p in enumerate(cc + [oc(cc[0], 1)]): E(t + k * BEAT, 'glockenspiel', oc(p, 1), 1.2, .28, .3, .1)
            E(t, 'upright', oc(bb, 1) if bb[-1] == '1' else bb, BAR, .4, -.2, .22)
        for i, ch in enumerate(THEME_CH):   # the whole theme, resolved at last
            bb, cc = CH[ch]; t = ts + i * BAR; E(t, 'upright', oc(bb, 1) if bb[-1] == '1' else bb, BAR, .42, -.2, .24)
            for k in (1, 2, 3): E(t + k * BEAT, 'upright', cc[k - 1], .7, .34, .1, .16)
        theme(ts, 'glockenspiel', (1, 8), v=.5, g=.22, oct_=0); theme(ts, 'upright', (1, 8), v=.5, g=.2, oct_=0)
        E(end1 + BAR - .1, 'upright', 'F2', 4, .5, -.1, .26); E(end1 + BAR - .1, 'upright', 'C4', 4, .4, .1, .18); E(end1 + BAR - .1, 'upright', 'A4', 4, .4, .2, .16)
    elif name == 'end':
        ts = m0 + 1.0; slow = .82
        for i in range(16):
            ch = THEME_CH[i % 8]; bb, cc = CH[ch]; t = ts + i * BAR / slow
            if t > endcard['t0'] + 1: break
            E(t, 'piano', oc(bb, 1) if bb[-1] == '1' else bb, BAR / slow, .4, -.2, .22)
            for j, p in enumerate(cc): E(t, ('violas', 'violins', 'violins')[j], p, BAR / slow + .4, .4, -.3 + .3 * j, .12, attack=.6)
        theme(ts, 'piano', (1, 8), tempo=slow, v=.5, g=.24); theme(ts + 8 * BAR / slow, 'piano', (1, 8), tempo=slow, v=.45, g=.2)
        te = endcard['t0']
        theme(te + .5, 'glockenspiel', (1, 4), tempo=.9, v=.45, g=.2)
        E(te + .5 + 16 * BEAT / .9, 'piano', 'F2', 6, .45, -.1, .22); E(te + .5 + 16 * BEAT / .9, 'piano', 'A3', 6, .4, .05, .16); E(te + .5 + 16 * BEAT / .9, 'piano', 'F4', 6, .4, .15, .14)

# keep each frame's score inside its frame (the card starts a new one), and render
spans_t = [(a, b) for _, a, b in spans]
def inside(t):
    for a, b in spans_t:
        if a <= t < b: return b
    return DUR
ev = [e for e in ev if e['t'] < DUR - 1]
for e in ev:   # notes that would ring into the next frame's card are shortened
    b = inside(e['t']); e['dur'] = None if e['dur'] is None else max(.1, min(e['dur'], b - e['t'] - .2))
mus = S.render(ev, dur=DUR, master=False)[:N]
if len(mus) < N: mus = np.pad(mus, ((0, N - len(mus)), (0, 0)))
for (te, inst, p, d, v, pan, g) in rev_notes:   # reverse piano: rendered, reversed, ending at te
    y = S.note(inst, p, d, v)[::-1].copy(); add(mus, y, te - len(y) / SR, g, pan)
for t0, y in PADS: add(mus, y, t0, 1.0, 0)
mus = S.room(mus, size=.6, mix=.24)
# fade the score out just before each card (the card brings the rewind)
for c in cards:
    i0, i1 = int((c['t0'] - .35) * SR), int((c['t0'] + 2.0) * SR); n = i1 - i0
    env = np.ones(n); k = int(.35 * SR); env[:k] = np.linspace(1, 0, k); env[k:] = 0; env[-int(.25 * SR):] = 0
    mus[i0:i1] *= env[:, None]

# ── the rewind: the last 1.8 s of music, reversed and accelerating, under a motor whir and sprocket chatter ──
fx = np.zeros((N, 2), np.float32)
def varispeed(y, s0, s1):   # read y with speed rising s0 → s1
    n = len(y); out = []; pos = 0.0; i = 0; L = int(n / ((s0 + s1) / 2))
    idx = np.cumsum(np.linspace(s0, s1, L)); idx = idx[idx < n - 1]; i0 = idx.astype(int); fr = idx - i0
    return (y[i0] * (1 - fr)[:, None] + y[i0 + 1] * fr[:, None]).astype(np.float32)
def whir(d, f0, f1):
    tt = t_(d); f = np.linspace(f0, f1, len(tt)); ph = 2 * np.pi * np.cumsum(f) / SR
    y = (np.sin(ph) * .5 + np.sign(np.sin(ph * 2)) * .12) * .5 + bp(noise(d), 600, 3500) * .25
    rate = np.linspace(f0 / 6, f1 / 6, len(tt)); clk = np.zeros(len(tt)); ph2 = np.cumsum(rate) / SR
    hits = np.where(np.diff(np.floor(ph2)) > 0)[0]
    for h in hits: clk[h:h + 300] += np.exp(-np.arange(min(300, len(clk) - h)) / 40) * (.8 + .4 * np.random.rand())
    y = y + hp(clk, 1500) * .6
    env = np.minimum(1, tt / .08) * np.minimum(1, (tt[-1] - tt) / .25 + 1e-6)
    return (y * env).astype(np.float32)
for c in cards:
    t0 = c['t0']; ff = c.get('dir') == 'ff'
    a, b = int((t0 - 1.8) * SR), int((t0 - .05) * SR); seg_ = mus[a:b].copy() if a > 0 else None
    if seg_ is not None and len(seg_):
        r = varispeed(seg_ if ff else seg_[::-1], 1.0, 4.5); r *= np.linspace(1, 0, len(r))[:, None] ** .7
        for ch in range(2): fx[int(t0 * SR):int(t0 * SR) + len(r), ch] += r[:N - int(t0 * SR), ch] * 3.6 if int(t0 * SR) + len(r) <= N else 0
    w = whir(1.55, 900 if not ff else 300, 120 if not ff else 1400); add(fx, w, t0, .2, 0)
    add(fx, thump(.5, 55), t0 + 2.2, .3, 0)                                 # the year lands: the series' low thump
    for k in range(5): add(fx, click(.55, .5), t0 + 1.3 + k * .17, .05, .1)  # counter drums
# ── foley, the series' set ──
def shutter(v=1.0):
    d = .09; a_ = hp(noise(d), 2000) * env_exp(d, .006); b_ = np.pad(hp(noise(.05), 1500) * env_exp(.05, .005), (int(.045 * SR), 0))[:len(a_)]; return norm(a_ + b_ * .8) * v
def paper(v=1.0):
    d = .25; return bp(noise(d), 1200, 6000) * env_exp(d, .05) * (1 - np.exp(-t_(d) / .01)) * v
def boom():
    d = 4.0; tt = t_(d); y = np.sin(2 * np.pi * 38 * tt * (1 - .2 * tt / d)) * env_exp(d, .7) + lp(noise(d), 180) * env_exp(d, 1.2) * .8 + lp(noise(d), 900) * env_exp(d, .25) * .3
    return norm(y).astype(np.float32)
def at_(s, v): return s['t0'] + .4 if v is None else s['t0'] + (-v) * s.get('vd', s['t1'] - s['t0']) if v < 0 else s['t0'] + v
PIC = ('hero', 'portrait', 'clip', 'pair', 'strip')
for s in SC:
    ty = s['type']
    if ty in PIC and not s.get('noflash'): add(fx, shutter(.6), s['t0'], .14, -.2)
    if ty == 'pair': add(fx, shutter(.6), at_(s, s['R'].get('at', .4)), .14, .2)
    if ty == 'strip':
        for f in s['frames'][1:]: add(fx, shutter(.6), at_(s, f.get('at', .4)), .12, .1); add(fx, click(.4, .6), at_(s, f.get('at', .4)) + .05, .05)
    if ty in ('quote', 'filing', 'envelope', 'title', 'myth', 'board'): add(fx, paper(.8), s['t0'] + .25, .22, .2)
    if ty == 'filing':
        for i in range(60): add(fx, click(1.6, .3), s['t0'] + .6 + i * .04 + np.random.rand() * .01, .02, .15)
    if ty == 'slides':
        t = s['t0'] + 1.1
        while t < s['t1'] - .3: add(fx, click(.35, .9), t, .1, .25); add(fx, thump(.3, 120), t + .02, .05, .25); t += 1 / 1.6
    if ty == 'implode':
        tb = at_(s, s.get('boom', -.35)); add(fx, boom(), tb + .35, .55, 0); add(fx, hp(noise(.6), 800) * env_exp(.6, .1) * .5, tb - .55, .1, 0)
    if ty == 'cassette':
        d = s['t1'] - s['t0']; y = (lp(noise(d), 400) * .3 + np.sin(2 * np.pi * 50 * t_(d)) * .2) * np.minimum(1, t_(d) / .3); add(fx, y.astype(np.float32), s['t0'], .05, .3)
    if ty == 'tv': d = s['t1'] - s['t0']; add(fx, (np.sin(2 * np.pi * 60 * t_(d)) * .2 + hp(noise(d), 9000) * .05).astype(np.float32), s['t0'], .05, 0)
    if ty == 'black': add(fx, shutter(1.0), s['t0'] + .36, .3, 0); add(fx, whir(1.8, 1100, 300), s['t0'] + .9, .12, 0)
    for it in s.get('items', []):
        if it['k'] == 'stamp': a = at_(s, it.get('at', .4)) if it.get('at', .4) < 0 or s['type'] != 'map' else s['t0'] + it['at']; add(fx, thump(.25, 140), a, .06, .2)
fx += np.repeat(lp(brown(DUR), 400)[:N, None] * .008, 2, axis=1).astype(np.float32)   # room tone
# ── narration ──
voc = np.zeros((N, 2), np.float32); spans_v = []
for k, v in VO.items():
    y, sr = sf.read(os.path.join(D, f'audio/vo/{k}.wav')); y = y if y.ndim == 1 else y.mean(1)
    y = soxr.resample(y, sr, SR); y = y / (np.sqrt(np.mean(y[np.abs(y) > .01] ** 2)) + 1e-9) * .11
    add(voc, y.astype(np.float32), v['t'], 1.0, 0); spans_v.append((v['t'], v['t'] + len(y) / SR))
g = np.ones(N)
for a, b in spans_v: g[int(a * SR):int(b * SR)] = np.minimum(g[int(a * SR):int(b * SR)], .4)
from scipy.ndimage import uniform_filter1d
g = uniform_filter1d(g, int(.5 * SR)); mus *= g[:, None]; fx *= (.6 + .4 * g)[:, None]
out = mus * 3.0 + fx * .7 + voc
tail = int(3.0 * SR); out[-tail:] *= np.linspace(1, 0, tail)[:, None]
def tp_limit(x, ceil):
    from scipy.signal import resample_poly
    from scipy.ndimage import maximum_filter1d, minimum_filter1d
    up = resample_poly(x, 4, 1); n = int(.004 * SR * 4)
    gg = np.minimum(1, ceil / np.maximum(maximum_filter1d(np.abs(up), 2 * n + 1), 1e-9)); gg = uniform_filter1d(minimum_filter1d(gg, 2 * n + 1), n)
    return resample_poly(up * gg, 1, 4)[:len(x)]
out = np.stack([tp_limit(limit(out[:, c], .5), .45) for c in range(2)], 1)
os.makedirs(os.path.join(D, 'out'), exist_ok=True); sf.write(os.path.join(D, 'out/mix.wav'), out.astype(np.float32), SR)
def db(a): return 20 * np.log10(np.sqrt(np.mean(a ** 2)) + 1e-12)
vm = np.zeros(N, bool)
for a, b in spans_v: vm[int(a * SR):int(b * SR)] = True
print('mix', round(DUR, 1), 's | voice', round(db(voc[vm]), 1), 'bed under voice', round(db((mus * 3 + fx * .7)[vm]), 1), 'music alone', round(db((mus * 3)[~vm]), 1))
