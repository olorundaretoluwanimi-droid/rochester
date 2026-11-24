#!/usr/bin/env python3
"""lines.json + cleaned narration durations + the shot list below → film.json (scenes, voice starts, subtitles, credits) and audio/cues.json.
Each frame opens on a rewind card (counter) that carries its "Frame n" line. Every scene lasts until the next starts.
Shot values: a dict (one scene for the line), or {'cont': True, 'items': [...]} to keep the previous scene and add overlays.
Overlay 'at' values: seconds after the line starts, or a negative fraction of the line (converted to scene-relative seconds here)."""
import json, os, copy
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
L = json.load(open(os.path.join(D, 'audio/lines.json'), encoding='utf-8'))
DUR = json.load(open(os.environ.get('DURFILE') or os.path.join(D, 'audio/vo/dur.json')))
GAP, QGAP, OPEN, TITLE, END = 0.6, 1.3, 2.9, 5.2, 17.0
ERA = {'hook': 10, 'f10': 10, 'f9': 9, 'f8': 8, 'f7': 7, 'f6': 6, 'f5': 5, 'f4': 4, 'f3': 3, 'f2': 2, 'f1': 1, 'end': 0}
CARD = {'f10': (10, '2012', 'The bankruptcy', 'the end of the roll'), 'f9': (9, '2010', 'The last roll', 'Kodachrome'),
        'f8': (8, '2007', 'The implosions', 'Kodak Park'), 'f7': (7, '2004', 'Number one', 'the part most people get wrong'),
        'f6': (6, '1982', 'The peak', 'sixty thousand jobs'), 'f5': (5, '1975', 'The camera with no film', 'a lab in Rochester'),
        'f4': (4, '1950', 'The city at its height', 'Rochester, at its biggest'), 'f3': (3, '1932–35', 'The founder, and the colour', 'George Eastman · Kodachrome'),
        'f2': (2, '1900–12', 'A dollar, and a dividend', 'the Brownie · the wage dividend'), 'f1': (1, '1888', 'You press the button', 'a bank clerk’s box camera'),
        'end': (0, 'TODAY', 'Fast-forward', 'Rochester now')}
THUMBS = {'f10': ['tower2012night', 'tower2012gorge', 'easyshare4', 'kodak2022'], 'f9': ['kc64', 'kc_slide', 'carousel', 'kc40box'],
          'f8': ['park2010', 'aerial2007', 'park2010'], 'f7': ['easyshare1', 'easyshare4', 'dcs100'], 'f6': ['balloon1980', 'roc1987', 'centennial1980'],
          'f5': ['sasson', 'roc1987'], 'f4': ['colorama', 'kc_ad1940', 'map1946'], 'f3': ['eastman1917', 'kc_ad1940', 'eastman_house', 'mannes'],
          'f2': ['kodak_girl', 'kp1906_n13', 'hq1900', 'brownies'], 'f1': ['eastman1884', 'ad1888', 'eastman_gallia', 'map1882'], 'end': ['tower2025', 'park2010', 'statue']}

def T(**k): return k
def I(k, **o): return dict(k=k, **o)
def hero(img, tag, **k): return dict(type='hero', img=img, tag=tag, **k)
def clip(clips, **k): return dict(type='clip', clips=clips if isinstance(clips, list) else [clips], **k)
def strip(frames, **k): return dict(type='strip', frames=frames, **k)
def cont(*its): return {'cont': True, 'items': list(its)}
PORT = [460, 50, 1000, 880]   # a tall picture, centred
PL = 'PHOTO: LARRY (CC BY-SA 3.0)'
F63 = 'FILM · ROCHESTER: A CITY OF QUALITY · 1963 (PRELINGER ARCHIVES, PUBLIC DOMAIN)'
KP06 = 'THE KODAK PROPERTIES · EASTMAN KODAK CO. · 1906 (INTERNET ARCHIVE, PUBLIC DOMAIN)'
S = {
 # ── hook ──
 'h01': hero('tower2012night', 'KODAK TOWER, ROCHESTER · JULY 2012 · ' + PL, box=PORT, fy=.25, items=[I('stamp', text='19 JAN 2012', x=1580, y=260, s=64, at=-.25)]),
 'h02': dict(type='hero', clip='c_tower', tag='KODAK TOWER TIME-LAPSE · BEACHFRONT B-ROLL (CC BY 3.0)', items=[I('drop', text='EASTMAN KODAK', x=240, y=780, s=96, at=.1),
             I('txt', text='ROCHESTER, NEW YORK', x=244, y=850, s=40, f='Mono', w=600, at=.9)]),
 'h03': dict(type='dots', **{'from': 604, 'to': 604}, at=.1, fallAt=99, label='EACH DOT = 100 KODAK JOBS IN ROCHESTER · AT THE PEAK, 1982', items=[I('stamp', text='60,000+', x=1650, y=900, s=70, at=-.5)]),
 'h04': dict(type='line', at=.1, draw=3.0, marks=[[1950, 'PEAK · 1950'], [2020, '2020']]),
 'h05': strip([dict(img='tower2012falls', tag='KODAK TOWER AND HIGH FALLS · DEC 2012 · ' + PL, edge='ROC 2012'), dict(img='kc64', at=-.5, tag='KODACHROME 64 · PHOTO: DNALOR 01 (CC BY-SA 3.0 AT)', edge='ROC 2010')]),
 'h06': clip('c_main', rev=True, tag=F63),
 'h07': strip([dict(img='kp1906_n13', tag=KP06, edge='ROC 1906'), dict(img='eastman1884', at=-.55, fy=.25, tag='GEORGE EASTMAN · c. 1884 (PUBLIC DOMAIN)', edge='ROC 1884')], era=1),
 'h08': dict(type='draw', img='sasson_cam', w=560, y=70, at=.0, until=-.7, tag='KODAK’S FIRST DIGITAL CAMERA, 1975 · DRAWING: BERTRAND LABÉVUE (CC BY-SA 4.0)', era=5),
 'h09': dict(type='type', lines=['This is Mill Town.'], s=90, img='c_kodak'),
 # ── frame 10 · 2012 ──
 'a02': dict(type='filing', img='tower2012night', stampAt=-.75, tag='CHAPTER 11 PETITION · 19 JAN 2012 · TYPESET FROM COURT RECORDS'),
 'a03': hero('tower2012gorge', 'KODAK TOWER · OCT 2012 · ' + PL, box=PORT, fy=.2, items=[I('stamp', text='$950 MILLION', x=1580, y=300, s=60, at=-.25), I('txt', text='CITIGROUP · TO KEEP RUNNING', x=1400, y=420, s=28, f='Mono', w=600, at=-.3)]),
 'a04': dict(type='dots', **{'from': 604, 'to': 71}, at=.1, fallAt=-.45, label='EACH DOT = 100 KODAK JOBS IN ROCHESTER · 1982 → 2012', left='', right='60,400  →  ≈ 7,000'),
 'a05': clip('c_midtown', tag=F63, caps=['ROCHESTER · 1963'], items=[I('count', to=38000, x=1450, y=300, s=110, at=-.45, dur=1.4, label='KODAK RETIREES · 2012')]),
 'a06': hero('tower2012falls', 'KODAK TOWER AND HIGH FALLS · DEC 2012 · ' + PL, fx=.6),
 'a07': dict(type='pair', L=dict(img='easyshare4', box=[120, 80, 1060, 707], tag='KODAK EASYSHARE CAMERAS · PHOTO: JJ HARRISON (CC BY-SA 3.0)'),
             R=dict(img='easyshare1', box=[1060, 460, 740, 490], at=-.5, tag='EASYSHARE CX7330 · PHOTO: SGROEY (CC BY-SA 4.0)'), items=[I('stamp', text='9 FEB 2012', x=1500, y=220, s=60, at=-.55)]),
 'a08': dict(type='marquee', at=-.55),
 'a09': dict(type='scale', at1=.3, at2=999),
 'a10': {'cont': True, 'set': {'at2': .2, 'tilt': 1}},
 'a11': hero('kodak2022', 'KODAK HEADQUARTERS, ROCHESTER · APRIL 2022 · PHOTO: TED SHAFFREY (CC BY-SA 4.0)', items=[I('stamp', text='2013', x=1560, y=200, s=70, at=.2)]),
 'a12': dict(type='hero', clip='c_tower', rev=True, tag='KODAK TOWER TIME-LAPSE · BEACHFRONT B-ROLL (CC BY 3.0)', items=[I('txt', text='◀◀  REWIND', x=1700, y=140, s=40, f='Mono', w=600, c='#E5512F', al='right', at=-.4)]),
 # ── frame 9 · 2010 ──
 'b02': dict(type='map', cam=[[0, 960, 520, 1.0, 0], [2.5, 780, 520, 2.4, 0]], towns=[['Parsons', .3, {'big': 1, 'label': 'Parsons, Kansas'}]], note=dict(a='PARSONS, KANSAS', b='ABOUT 10,000 PEOPLE', at=-.5)),
 'b03': {'cont': True, 'items': [I('txt', text='DWAYNE’S PHOTO', x=120, y=320, s=54, w=700, at=.3), I('txt', text='THE LAST KODACHROME LAB ON EARTH', x=120, y=370, s=28, f='Mono', w=600, c='#AE9F86', at=-.5)]},
 'b04': hero('kc64', 'KODACHROME 64 · PHOTO: DNALOR 01 (CC BY-SA 3.0 AT)', box=[610, 60, 700, 860], fy=.3, items=[I('drop', text='Kodachrome.', x=960, y=560, s=130, al='center', at=.1)]),
 'b05': dict(type='slides', img='kc_slide', tag='A KODACHROME SLIDE · PHOTO: JERZY STRZELECKI (CC BY-SA 4.0)', clips=['c_midtown', 'c_main', 'c_falls', 'c_audience', 'c_aerial', 'c_orch'],
             items=[I('stamp', text='1935 – 2009', x=1180, y=110, s=56, at=-.2)]),
 'b06': hero('kc_slide', 'A KODACHROME SLIDE IN ITS PAPER MOUNT · PHOTO: JERZY STRZELECKI (CC BY-SA 4.0)', box=[460, 60, 1000, 860], z=[1.0, 1.25], fy=.45),
 'b07': hero('kc40box', 'KODACHROME 40 MOVIE FILM · PHOTO: DNALOR 01 (CC BY-SA 3.0 AT)', items=[I('typed', text='PROCESS K-14', x=260, y=200, s=54, at=-.35, dur=.6), I('txt', text='ONLY A FEW LABS EVER RAN IT', x=262, y=250, s=26, f='Mono', w=600, at=-.6)]),
 'b08': hero('carousel', 'KODAK CAROUSEL PROJECTOR · PHOTO: STEVE MORGAN (CC BY-SA 4.0)', items=[I('stamp', text='2009', x=1560, y=220, s=80, at=-.4)]),
 'b09': dict(type='map', cam=[[0, 960, 520, 1.0, 0], [3, 1100, 470, 1.6, 0]], towns=[['New York', .1, {}], ['Parsons', .1, {'big': 1}]],
             routes=[dict(a='New York', b='Parsons', at=-.55, dur=1.6, bend=-.25, label='ONE OF THE LAST ROLLS', dx=-20, dy=-30)], note=dict(a='STEVE McCURRY', b='SHOT ONE OF THE LAST ROLLS', at=.2)),
 'b10': dict(type='map', cam=[[0, 960, 520, 1.0, 0]], towns=[['Parsons', 0, {'big': 1}]], swarm=dict(to='Parsons', n=140, at=.2, until=-.9, count=0), note=dict(a='FROM EVERYWHERE', b='ROLLS SENT TO PARSONS · 2010', at=.4)),
 'b11': cont(I('stamp', text='30 DEC 2010', x=1500, y=240, s=70, at=.4), I('txt', text='LAST ROLLS ACCEPTED', x=1500, y=330, s=28, f='Mono', w=600, al='center', at=.7)),
 'b12': hero('kc64', 'KODACHROME 64 · PHOTO: DNALOR 01 (CC BY-SA 3.0 AT)', box=[610, 60, 700, 860], fy=.6, z=[1.1, 1.3], items=[I('txt', text='UNDEVELOPED · FOR GOOD', x=960, y=560, s=50, f='Mono', w=600, al='center', at=-.6)]),
 'b13': clip(['c_falls', 'c_midtown'], tag=F63),
 # ── frame 8 · 2007 ──
 'c02': hero('aerial2007', 'ROCHESTER FROM THE AIR · 17 AUG 2007 · PHOTO: CHRIS TOMKINS-TINCH (CC BY-SA 3.0)', items=[I('stamp', text='30 JUN 2007', x=1560, y=200, s=64, at=.1)]),
 'c03': hero('park2010', 'KODAK PARK FROM SENECA PARK · 2010 · PHOTO: DANIELPENFIELD (CC BY-SA 3.0)', items=[I('count', to=1300, pre='≈ ', post=' ACRES', x=1350, y=220, s=80, at=.6, dur=1.2)]),
 'c04': dict(type='implode', label='BUILDING 9 · KODAK PARK', time='8:00 A.M.', boom=-.55, floors=6, img='park2010'),
 'c05': dict(type='implode', label='BUILDING 23 · ALMOST HALF A MILLION SQ FT', time='1 JULY', boom=-.5, floors=5, img='park2010'),
 'c06': hero('park2010', 'KODAK PARK FROM SENECA PARK · 2010 · PHOTO: DANIELPENFIELD (CC BY-SA 3.0)', fx=.8, z=[1.2, 1.3], items=[I('stamp', text='SINCE 2003', x=1560, y=200, s=60, at=-.6)]),
 'c07': hero('aerial2007', 'ROCHESTER FROM THE AIR · 17 AUG 2007 · PHOTO: CHRIS TOMKINS-TINCH (CC BY-SA 3.0)', fx=.3, z=[1.15, 1.3]),
 'q01': dict(type='quote', img='park2010', imgTag='KODAK PARK · 2010 · PHOTO: DANIELPENFIELD (CC BY-SA 3.0)', q=['I got to see one.', 'I didn’t want to', 'see any more.'], fy=.5),
 'c08': hero('park2010', 'EASTMAN BUSINESS PARK · 2010 · PHOTO: DANIELPENFIELD (CC BY-SA 3.0)', z=[1.0, 1.08], items=[I('drop', text='EASTMAN BUSINESS PARK', x=960, y=540, s=88, al='center', at=-.45), I('stamp', text='11 NOV 2008', x=1560, y=200, s=60, at=.3)]),
 'c09': dict(type='hero', clip='c_aerial2', rev=True, tag=F63),
 # ── frame 7 · 2004 ──
 'd02': hero('easyshare1', 'KODAK EASYSHARE CX7330 · PHOTO: SGROEY (CC BY-SA 4.0)'),
 'd03': dict(type='myth', lines=[['Kodak invented the digital camera.', 1], ['It got scared, and hid it.', 0], ['When digital came, it was left behind.', 0]], at=[.1, -.35, -.65], mark=-.88),
 'd04': hero('easyshare4', 'KODAK EASYSHARE CAMERAS · PHOTO: JJ HARRISON (CC BY-SA 3.0)', items=[I('stamp', text='2004', x=1560, y=220, s=90, at=.1)]),
 'd05': dict(type='pair', L=dict(img='easyshare1', box=[120, 80, 980, 649], tag='EASYSHARE CX7330 · PHOTO: SGROEY (CC BY-SA 4.0)'),
             R=dict(img='easyshare4', box=[1000, 420, 800, 534], at=-.5, tag='EASYSHARE Z700 · PHOTO: JJ HARRISON (CC BY-SA 3.0)'), items=[I('stamp', text='SINCE 2001', x=1450, y=230, s=56, at=.4)]),
 'd06': dict(type='bars', title='KODAK’S SHARE OF U.S. DIGITAL CAMERA SALES (IDC)', max=30, data=[['2004 · No. 1', 21.9, '21.9%'], ['2005 · No. 1', 24.9, '24.9%']], at=[.3, 999],
             note='SOURCE · IDC, VIA NBC NEWS / AP AND ROCHESTER BUSINESS JOURNAL', items=[I('stamp', text='No. 1', x=1640, y=300, s=80, at=-.4)]),
 'd07': {'cont': True, 'set_at': [1, .1]},
 'd08': hero('dcs100', 'KODAK DCS 100 (1991) · PHOTO: JOHN (CC BY 2.0)', box=PORT, fy=.4),
 'd09': hero('kc64', 'KODACHROME 64 · PHOTO: DNALOR 01 (CC BY-SA 3.0 AT)', box=[610, 60, 700, 860], fy=.4, items=[I('drop', text='FILM', x=960, y=560, s=180, al='center', at=-.55)]),
 'd10': dict(type='margin', at1=.2, at2=999),
 'd11': {'cont': True, 'set': {'at2': .2}},
 'd12': hero('easyshare4', 'KODAK EASYSHARE CAMERAS · PHOTO: JJ HARRISON (CC BY-SA 3.0)', fx=.3, z=[1.1, 1.25]),
 'd13': dict(type='board'),
 'd14': dict(type='phone', at=.6),
 'd15': dict(type='hero', clip='c_industry', rev=True, tag=F63),
 # ── frame 6 · 1982 ──
 'e02': hero('balloon1980', 'KODAK’S 100TH-BIRTHDAY BALLOON · ROCHESTER, MAY 1980 · RIT NEWS & EVENTS (PUBLIC DOMAIN)', box=[560, 60, 800, 860], fy=.3),
 'e03': dict(type='dots', **{'from': 604, 'to': 604}, at=.1, fallAt=99, label='EACH DOT = 100 KODAK JOBS IN ROCHESTER · 1982', items=[I('count', to=60400, x=960, y=930, s=96, at=-.6, dur=1.2)]),
 'e04': clip(['c_audience', 'c_midtown'], tag=F63, caps=['ROCHESTER · 1963', 'ROCHESTER · 1963']),
 'e05': hero('centennial1980', 'KODAK ADVERTISEMENT · DEMOCRAT AND CHRONICLE, 11 MAY 1980 (PUBLIC DOMAIN)', box=[560, 60, 800, 860], fy=.2, items=[I('stamp', text='WAGE DIVIDEND', x=1600, y=300, s=48, at=-.5), I('txt', text='PAID EVERY MARCH', x=1600, y=380, s=26, f='Mono', w=600, al='center', at=-.6)]),
 'e06': dict(type='icons'),
 'e07': hero('roc1987', 'ROCHESTER FROM THE GENESEE · 1987 · PHOTO: DANIEL CHRISTENSEN (CC BY-SA 3.0)', items=[I('drop', text='The World’s Image Centre', x=960, y=860, s=72, al='center', at=-.5)]),
 'e08': dict(type='floppy'),
 'e09': dict(type='draw', img='sasson_cam', w=560, y=70, at=.1, until=-.6, tag='DRAWING: BERTRAND LABÉVUE (CC BY-SA 4.0)', items=[I('stamp', text='1975', x=1480, y=260, s=90, at=-.5)]),
 # ── frame 5 · 1975 ──
 'g02': dict(type='portrait', img='sasson', name='Steve Sasson', sub='ELECTRICAL ENGINEER · KODAK FROM 1973', tag='STEVE SASSON IN 2010 · PHOTO: ALJAWAD (CC BY 3.0)', fy=.2),
 'g03': dict(type='draw', img='pat75_1', w=700, x=260, y=70, at=.1, until=-.4, tag='U.S. PATENT 4,131,919 · SASSON AND LLOYD (PUBLIC DOMAIN)',
             items=[I('txt', text='GARETH LLOYD, SUPERVISOR', x=1340, y=300, s=34, w=700, at=.3), I('txt', text='A CHARGE-COUPLED DEVICE:', x=1340, y=420, s=28, f='Mono', w=600, at=-.6), I('txt', text='LIGHT IN, NUMBERS OUT', x=1340, y=460, s=28, f='Mono', w=600, at=-.7)]),
 'g04': dict(type='draw', img='sasson_cam', w=600, x=200, y=60, at=.0, until=-.3, tag='KODAK’S FIRST DIGITAL CAMERA · DRAWING: BERTRAND LABÉVUE (CC BY-SA 4.0)',
             items=[I('typed', text='LENS · FROM A KODAK MOVIE CAMERA', x=940, y=330, s=32, at=-.3, dur=.6), I('typed', text='MEMORY · AN AUDIO CASSETTE', x=940, y=410, s=32, at=-.55, dur=.6), I('typed', text='POWER · 16 AA BATTERIES', x=940, y=490, s=32, at=-.8, dur=.5)]),
 'g05': cont(I('stamp', text='8 LB', x=1180, y=680, s=90, at=.2), I('txt', text='ABOUT THE SIZE OF A TOASTER', x=1180, y=790, s=28, f='Mono', w=600, al='center', at=-.6)),
 'g06': dict(type='pixels', clip='c_kodak', fr=70, fy=.3, at=.3, until=-.9),
 'g07': dict(type='cassette', art='sasson_cam', artTag='DRAWING: BERTRAND LABÉVUE (CC BY-SA 4.0)'),
 'g08': dict(type='tv', at=.3),
 'g09': dict(type='type', lines=['FILMLESS', 'PHOTOGRAPHY'], redLine=0, s=130, sub='shown to a company that lived on film', img='kp1906_n9', at=-.3),
 'q02': dict(type='quote', img='sasson', imgTag='STEVE SASSON IN 2010 · PHOTO: ALJAWAD (CC BY 3.0)', q=['That’s cute —', 'but don’t tell anyone', 'about it.'], fy=.2),
 'g10': dict(type='type', lines=['15 – 20 YEARS'], redLine=0, s=150, sub='Sasson’s own guess, before digital could compete with film', at=-.55),
 'g11': dict(type='draw', img='pat75_1', w=700, y=70, at=.0, until=.6, tag='U.S. PATENT 4,131,919 · GRANTED 26 DEC 1978 (PUBLIC DOMAIN)', items=[I('stamp', text='PATENT · 1978', x=1480, y=300, s=60, at=-.3)]),
 'g12': dict(type='hero', clip='c_kodak', tag=F63),
 'g13': hero('colorama', 'THE KODAK COLORAMA, GRAND CENTRAL TERMINAL · 1960 (PUBLIC DOMAIN)', box=[400, 60, 1120, 860]),
 # ── frame 4 · 1950 ──
 'j02': dict(type='line', at=.1, draw=2.4, marks=[[1950, 'PEAK · 1950']]),
 'j03': clip(['c_main'], tag=F63, caps=['MAIN STREET · 1963']),
 'j04': strip([dict(clip='c_midtown', tag=F63, edge='ROC 1963'), dict(clip='c_audience', at=-.5, tag=F63, edge='ROC 1963')]),
 'j05': dict(type='hero', clip='c_aerial', tag=F63),
 'j06': clip(['c_aerial2', 'c_skyline'], tag=F63, items=[I('stamp', text='1963', x=1640, y=160, s=70, at=.3)]),
 'j07': clip(['c_main', 'c_midtown'], tag=F63, caps=['MAIN STREET · 1963', 'MIDTOWN PLAZA · 1963']),
 'j08': clip(['c_orch', 'c_audience'], tag=F63, caps=['A CONCERT · ROCHESTER · 1963', 'ROCHESTER · 1963']),
 'j09': dict(type='hero', clip='c_kodak', tag=F63, items=[I('txt', text='KODAK OFFICE · STATE STREET', x=1720, y=880, s=30, f='Mono', w=600, al='right', at=.4)]),
 # ── frame 3 · 1932–1935 ──
 'k02': dict(type='portrait', img='eastman1917', name='George Eastman', sub='1854–1932 · FOUNDER OF KODAK', tag='GEORGE EASTMAN · B. C. FORBES PUBLISHING, 1917 (PUBLIC DOMAIN)', fy=.25),
 'k03': dict(type='map', cam=[[0, 1250, 430, 1.55, 0]], towns=[['Rochester', 0, {'big': 1}]],
             routes=[dict(a='Rochester', b='Cambridge', at=-.38, dur=1.0, label='MIT · “MR. SMITH”', dx=16, dy=-14), dict(a='Rochester', b='Tuskegee', at=-.7, dur=1.2, label='TUSKEGEE', dx=-150, dy=40),
                     dict(a='Rochester', b='Hampton', at=-.74, dur=1.1, label='HAMPTON', dx=16, dy=30)], note=dict(a='GIVING IT AWAY', b='GEORGE EASTMAN’S GIFTS', at=.2, y=900)),
 'k04': hero('eastman_theatre', 'THE EASTMAN THEATRE · 2007 · PHOTO: MATTHEW D. WILSON (CC BY-SA 2.5)', items=[I('count', to=3000, post='+', x=1560, y=240, s=90, at=-.6, dur=1.0, label='SEATS')]),
 'k05': hero('eastman1915', 'GEORGE EASTMAN · BAIN NEWS SERVICE, 1915 (LIBRARY OF CONGRESS, PUBLIC DOMAIN)', box=[560, 60, 800, 860], fy=.25, items=[I('count', to=75, pre='$', post=' MILLION+', x=960, y=930, s=80, at=.2, dur=1.4)]),
 'k06': hero('eastman_house', 'GEORGE EASTMAN’S HOUSE, EAST AVENUE · CAROL M. HIGHSMITH, 2018 (PUBLIC DOMAIN)', z=[1.0, 1.04], noflash=1),
 'k07': hero('kc_ad1940', 'KODACHROME ADVERTISEMENT · 1940 (PUBLIC DOMAIN)', box=[560, 60, 800, 860], fy=.3, items=[I('drop', text='Colour.', x=1560, y=560, s=110, al='center', at=-.35)]),
 'k08': dict(type='layers', img='kc_ad1940', tag='KODACHROME ADVERTISEMENT · 1940 (PUBLIC DOMAIN)', at=-.4),
 'k09': dict(type='portrait', img='mannes', name='Leopold Mannes', sub='PIANIST · 1899–1964', tag='LEOPOLD MANNES · THE VIOLINIST, MAY 1926 (PUBLIC DOMAIN)', fy=.3,
             items=[I('txt', text='and Leopold Godowsky Jr.', x=900, y=640, s=48, it=1, at=-.45), I('txt', text='VIOLINIST · 1900–1983', x=900, y=690, s=26, f='Mono', w=600, c='#AE9F86', at=-.5)]),
 'k10': dict(type='portrait', img='mees', name='Kenneth Mees', sub='HEAD OF KODAK RESEARCH · 1882–1960', tag='C. E. KENNETH MEES · c. 1912 (PUBLIC DOMAIN)', fy=.3, items=[I('stamp', text='1930', x=1500, y=700, s=70, at=-.5)]),
 'k11': dict(type='type', lines=['♪  Brahms,', 'in the dark'], s=110, sub='as the story is told', at=.2),
 'k12': hero('eastman_edison', 'GEORGE EASTMAN AND THOMAS EDISON · 31 JULY 1928 (PUBLIC DOMAIN)', items=[I('stamp', text='1935', x=1580, y=200, s=80, at=.2)]),
 'k13': hero('eastman_desk', 'GEORGE EASTMAN AT HIS DESK · DUDLEY HOYT, c. 1903 (PUBLIC DOMAIN)', box=[560, 60, 800, 860], fy=.3),
 # ── frame 2 · 1900–1912 ──
 'm02': dict(type='brownie', img='brownie_a', tag='A KODAK BROWNIE · PHOTO: ZEWAN (CC BY-SA 3.0)', priceAt=-.25, label='CARDBOARD · IMITATION LEATHER · SIMPLE LENS'),
 'm03': dict(type='pair', L=dict(img='kodak_girl', box=[200, 80, 600, 864], fy=.3, tag='“THE KODAK GIRL” · 1909 (LIBRARY OF CONGRESS, PUBLIC DOMAIN)'),
             R=dict(img='brownie_hand', box=[1180, 80, 250, 873], at=-.45, tag='ADVERTISEMENT · 1904 (PUBLIC DOMAIN)')),
 'm04': hero('brownies', 'KODAK BROWNIES · PHOTO: CLÉMENT BUCCO-LECHAT (CC BY-SA 3.0)', items=[I('count', to=150000, x=960, y=850, s=96, at=.3, dur=1.6, label='SOLD IN THE FIRST YEAR (ABOUT)')]),
 'm05': strip([dict(img='kp1906_n31', tag=KP06, edge='ROC 1906'), dict(img='hq1900', at=-.45, tag='KODAK, STATE STREET · DETROIT PUBLISHING CO., c. 1900 (LIBRARY OF CONGRESS)', edge='ROC 1900')]),
 'm06': strip([dict(img='kp1906_n18', tag=KP06, edge='ROC 1906'), dict(img='kp1906_n13', at=-.35, tag=KP06, edge='ROC 1906'), dict(img='kp1906_n14', at=-.6, tag=KP06, edge='ROC 1906'),
               dict(img='kp1906_n24', at=-.82, tag=KP06, edge='ROC 1906')]),
 'm07': hero('kp1906_n26', KP06, items=[I('stamp', text='1912', x=1580, y=200, s=80, at=.3)]),
 'm08': dict(type='envelope', img='kp1906_n23', tag=KP06),
 'm09': hero('kp1906_n25', KP06, z=[1.05, 1.15]),
 'm10': hero('kp1906_n12', KP06, fx=.4),
 'm11': hero('ad1909', 'KODAK ADVERTISEMENT · 1909 (PUBLIC DOMAIN)', box=[560, 60, 800, 860], fy=.3),
 # ── frame 1 · 1888 ──
 'p02': dict(type='portrait', img='eastman1884', name='George Eastman', sub='BORN 1854 · WATERVILLE, N.Y.', tag='GEORGE EASTMAN · c. 1884 (PUBLIC DOMAIN)', fy=.2,
             items=[I('stamp', text='$3 A WEEK', x=1500, y=720, s=60, at=-.6)]),
 'p03': hero('map1882', 'MAP OF THE CITY OF ROCHESTER · DREW, ALLIS & CO., 1882 (BNF GALLICA, PUBLIC DOMAIN)', fx=.5, fy=.45, z=[1.6, 1.9], items=[I('stamp', text='1877', x=1560, y=200, s=80, at=-.45)]),
 'p04': dict(type='type', lines=['GLASS PLATES · CHEMICALS', 'A DARK TENT · A TRIPOD'], s=64, sub='“a pack-horse load”', img='map1882', at=.2),
 'p05': hero('map1882', 'MAP OF THE CITY OF ROCHESTER · 1882 (BNF GALLICA, PUBLIC DOMAIN)', fx=.3, fy=.6, z=[2.2, 2.4], items=[I('stamp', text='1881', x=1560, y=200, s=80, at=-.4), I('txt', text='DRY PLATES, READY TO USE', x=1560, y=300, s=30, f='Mono', w=600, al='center', at=-.5)]),
 'p06': dict(type='draw', img='patent2', w=560, y=60, at=.0, until=-.2, tag='U.S. PATENT 388,850 · GEORGE EASTMAN · 4 SEPT 1888 (PUBLIC DOMAIN)'),
 'p07': dict(type='draw', img='patent1', w=560, y=60, at=.0, until=-.5, tag='U.S. PATENT 388,850 · GEORGE EASTMAN · 4 SEPT 1888 (PUBLIC DOMAIN)',
             items=[I('drop', text='K', x=1450, y=600, s=300, at=-.7), I('drop', text='KODAK', x=1450, y=760, s=110, al='center', at=-.85)]),
 'q03': dict(type='quote', img='eastman1884', imgTag='GEORGE EASTMAN · c. 1884 (PUBLIC DOMAIN)', q=['The letter K had been', 'a favorite with me.', 'It seems a strong,', 'incisive sort of letter.'], fy=.2, qs=58),
 'p08': dict(type='rounds', at=.3, until=-.15, items=[I('stamp', text='$25', x=1650, y=300, s=90, at=.1)]),
 'p09': dict(type='map', cam=[[0, 960, 520, 1.0, 0]], towns=[['Rochester', 0, {'big': 1}], ['Chicago', 0, {}], ['Boston', 0, {'hide': 1}], ['Atlanta', 0, {'hide': 1}], ['Denver', 0, {'hide': 1}], ['New Orleans', 0, {'hide': 1}], ['San Francisco', 0, {'hide': 1}]],
             routes=[dict(a=a, b='Rochester', at=-.3 - i * .06, dur=1.6, parcel=1) for i, a in enumerate(['Chicago', 'Atlanta', 'Denver', 'New Orleans', 'San Francisco', 'Boston'])],
             note=dict(a='BY MAIL, TO ROCHESTER', b='THE WHOLE CAMERA, FILM INSIDE', at=-.3)),
 'p10': {'cont': True, 'routes': [dict(a='Rochester', b=b, at=-.45 - i * .05, dur=1.6, parcel=1) for i, b in enumerate(['Chicago', 'Atlanta', 'Denver', 'New Orleans', 'San Francisco', 'Boston'])],
         'items': [I('stamp', text='$10', x=1600, y=880, s=90, at=-.85)]},
 'p11': hero('ad1888', 'KODAK ADVERTISEMENT · 1888 (PUBLIC DOMAIN)', box=[460, 60, 1000, 757]),
 'p12': hero('ad1891', 'KODAK ADVERTISEMENT · 1891 · TEKNISKA MUSEET (CC BY 2.0)', box=[260, 120, 1400, 796], noflash=1),
 # ── epilogue ──
 'r02': dict(type='line', at=.1, draw=1.6, marks=[[1950, 'PEAK · 1950'], [2020, '2020']]),
 'r03': hero('tower2025', 'KODAK TOWER · JULY 2025 · PHOTO: PEDRO TERRES (CC BY 4.0)'),
 'r04': hero('park2010', 'EASTMAN BUSINESS PARK · 2010 · PHOTO: DANIELPENFIELD (CC BY-SA 3.0)', items=[I('count', to=100, post='+', x=1500, y=240, s=110, at=.3, dur=1.2, label='COMPANIES')]),
 'r05': dict(type='portrait', img='sasson', name='Steve Sasson', sub='NATIONAL MEDAL OF TECHNOLOGY AND INNOVATION', tag='STEVE SASSON IN 2010 · PHOTO: ALJAWAD (CC BY 3.0)', fy=.2),
 'r06': strip([dict(img='eastman_gallia', tag='TAKEN WITH A KODAK · FREDERICK CHURCH, 1890 (PUBLIC DOMAIN)', edge='ROC 1890'), dict(img='kodak_girl', at=-.4, fy=.3, tag='“THE KODAK GIRL” · 1909 (LIBRARY OF CONGRESS)', edge='ROC 1909'),
               dict(clip='c_audience', at=-.75, tag=F63, edge='ROC 1963')]),
 'r07': dict(type='hero', clip='c_kodak', tag=F63),
 'r08': hero('statue', 'GEORGE EASTMAN, UNIVERSITY OF ROCHESTER · PHOTO: TOMWSULCER (CC0)', box=[360, 60, 1200, 860]),
}
QUOTE_META = {l['id']: l.get('quote') for l in L}

# ── timeline ──
scenes, subs, voice, t = [], [], [], 0.0
def add(sc, t0): sc = dict(sc); sc['t0'] = round(t0, 3); scenes.append(sc); return sc
add(dict(type='black'), 0.0); t = OPEN
prev_ch = None
for i, l in enumerate(L):
    lid, ch, d = l['id'], l['chapter'], DUR[l['id']]
    era = ERA[ch]
    if ch != prev_ch and ch in CARD:   # the rewind card carries this frame's first line
        n, yr, ti, sub = CARD[ch]
        t += .4; sc = add(dict(type='counter', n=n, year=yr, title=ti, sub=sub, era=era, dir='ff' if ch == 'end' else 'rew', thumbs=THUMBS[ch], frame=ch), t)
        vt = t + 2.0; voice.append(dict(id=lid, t=round(vt, 3), d=d)); subs += [dict(t0=round(vt, 3), t1=round(vt + d, 3), text=s) for s in l['subs'][:1]]
        t = vt + d + 1.5; prev_ch = ch; continue
    prev_ch = ch
    vt = t + (.3 if lid.startswith('q') else 0)
    sh = S.get(lid)
    if sh is None: raise SystemExit(f'no shot for {lid}')
    if sh.get('cont'):
        last = scenes[-1]
        for it in sh.get('items', []):
            it = dict(it); a = it.get('at', .4); it['at'] = round(vt - last['t0'] + (a if a >= 0 else -a * d), 3); last.setdefault('items', []).append(it)
        for k, v in sh.get('set', {}).items():
            last[k] = round(vt - last['t0'] + (v if v >= 0 else -v * d), 3) if k.startswith('at') else v
        if 'set_at' in sh: j, v = sh['set_at']; last['at'][j] = round(vt - last['t0'] + (v if v >= 0 else -v * d), 3)
        for r in sh.get('routes', []):
            r = dict(r); a = r['at']; r['at'] = round(vt - last['t0'] + (a if a >= 0 else -a * d), 3); last.setdefault('routes', []).append(r)
    else:
        sc = copy.deepcopy(sh); sc.setdefault('era', era); sc['line'] = lid; sc['vd'] = d
        if lid.startswith('q'): sc.update(QUOTE_META[lid] or {})
        add(sc, t if lid.startswith('q') else vt - .25)
        # negative/fractional 'at' values inside a fresh scene are relative to its line: keep them (renderer handles), they refer to vd
    voice.append(dict(id=lid, t=round(vt, 3), d=d))
    # captions: split the line's caption lines over its duration by length
    if any(l['subs']):
        tot = sum(len(s) for s in l['subs']); a = vt
        for s in l['subs']:
            b = a + d * len(s) / tot; subs.append(dict(t0=round(a, 3), t1=round(b, 3), text=s)); a = b
    q = lid in ('a12', 'b13', 'c09', 'd15', 'e09', 'g13', 'j09', 'k13', 'm11', 'h09')
    t = vt + d + (QGAP if q else GAP)
    if lid == 'h09':   # the title card after the hook
        add(dict(type='title', era=10), t); t += TITLE
    if lid == 'p12': t += 1.4   # the first frame breathes before the fast-forward
end = add(dict(type='end', era=1), t + .3); DURT = round(t + .3 + END, 3)
for a, b in zip(scenes, scenes[1:] + [None]): a['t1'] = b['t0'] if b else DURT
# negative 'at' values in scenes started for a line refer to that line's duration (renderer: AT uses vd); for scenes started 0.25 s early,
# positive 'at' values are seconds after the scene start — fine.
CREDITS = ['What Happened to Rochester? The City Kodak Built',
           'NARRATION · STORYTELLER OXLEY (ELEVENLABS VIA AI33)',
           'PICTURES · LIBRARY OF CONGRESS · NATIONAL ARCHIVES · INTERNET ARCHIVE · BNF GALLICA · NYPL',
           'FILM · ROCHESTER: A CITY OF QUALITY (1963) · PRELINGER ARCHIVES · KODAK TOWER TIME-LAPSE · BEACHFRONT B-ROLL (CC BY 3.0)',
           'PHOTOGRAPHS · WIKIMEDIA COMMONS CONTRIBUTORS, CREDITED ON SCREEN (CC BY / CC BY-SA)',
           'MAP · NATURAL EARTH · CENSUS FIGURES · U.S. CENSUS BUREAU',
           'MUSIC · ORIGINAL SCORE · SALAMANDER GRAND PIANO (CC BY 3.0) · VS CHAMBER ORCHESTRA CE (CC0)',
           'QUOTES · WXXI NEWS · THE NEW YORK TIMES (2008) · SYSTEM MAGAZINE (1920)',
           'In the U.S., if you are struggling, call or text 988 (Suicide & Crisis Lifeline).']
film = dict(dur=DURT, scenes=scenes, subs=subs, voice=voice, credits=CREDITS)
json.dump(film, open(os.path.join(D, 'film.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
json.dump(dict(dur=DURT, voice=voice, scenes=[dict(type=s['type'], t0=s['t0'], t1=s['t1'], era=s.get('era'), line=s.get('line'), frame=s.get('frame')) for s in scenes]),
          open(os.path.join(D, 'audio/cues.json'), 'w'), indent=0)
# chapters for the description (the frame names)
ch = [(s['t0'], s) for s in scenes if s['type'] == 'counter']
print(f'{len(scenes)} scenes, {DURT:.1f} s = {DURT / 60:.2f} min')
print('0:00 Hook'); [print(f'{int(t0 // 60)}:{int(t0 % 60):02d} ' + (f"Frame {s['n']} · {s['year']} · {s['title']}" if s['n'] else 'Fast-forward · Today')) for t0, s in ch]
