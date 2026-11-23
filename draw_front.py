#!/usr/bin/env python3
"""Draw the news image for Sunday 22 November 2026.

One 1024x1024 PNG: a header naming the day, a lead panel on the COP31
collapse, eight numbered story tiles, and an "Also today" wire strip.
Deterministic: no network, no randomness, fixed fonts and colours.
Run: python3 draw_front.py  ->  writes entry.png next to this file.
"""
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

NAVY = (20, 33, 61)
INK = (26, 26, 46)
PAPER = (255, 255, 255)
AMBER = (244, 162, 97)
RED = (201, 42, 42)
LEAD_BG = (255, 243, 214)
LEAD_EDGE = (230, 111, 81)
WIRE_BG = (31, 41, 55)
MUTED = (90, 90, 110)


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_TITLE = font("DejaVuSans-Bold.ttf", 34)
F_DATE = font("DejaVuSans-Bold.ttf", 25)
F_SUB = font("DejaVuSans.ttf", 15)
F_LEAD_HEAD = font("DejaVuSans-Bold.ttf", 40)
F_LEAD_BODY = font("DejaVuSans.ttf", 20)
F_TILE_HEAD = font("DejaVuSans-Bold.ttf", 17)
F_TILE_BODY = font("DejaVuSans.ttf", 14)
F_WIRE_HEAD = font("DejaVuSans-Bold.ttf", 18)
F_WIRE = font("DejaVuSans.ttf", 14)
F_NUM = font("DejaVuSans-Bold.ttf", 20)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, xy, text, fnt, max_w, fill, leading):
    x, y = xy
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def draw_header(d):
    d.rectangle([0, 0, W, 96], fill=NAVY)
    d.rectangle([0, 96, W, 100], fill=AMBER)
    d.text((16, 16), "THE WORLD IN ONE IMAGE", font=F_TITLE, fill=PAPER)
    d.text((16, 62), "make.fun daily news picture", font=F_SUB,
           fill=(180, 190, 210))
    date = "SUNDAY 22 NOVEMBER 2026"
    dw = d.textlength(date, font=F_DATE)
    d.text((W - 16 - dw, 20), date, font=F_DATE, fill=AMBER)
    d.text((W - 16 - d.textlength("Antalya  •  Kyiv  •  Benghazi  •  the Gulf",
                                  font=F_SUB), 62),
           "Antalya  •  Kyiv  •  Benghazi  •  the Gulf",
           font=F_SUB, fill=(180, 190, 210))


def draw_globe(d, cx, cy, r, sea, land):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=sea, outline=INK, width=3)
    d.ellipse([cx - r + 14, cy - r + 20, cx - r + 58, cy - r + 52], fill=land)
    d.ellipse([cx + 8, cy + 18, cx + 52, cy + 46], fill=land)
    d.ellipse([cx - 30, cy + 44, cx + 6, cy + 66], fill=land)
    d.arc([cx - r, cy - r, cx + r, cy + r], 200, 340, fill=INK, width=2)
    d.arc([cx - r, cy - r, cx + r, cy + r], 20, 160, fill=INK, width=2)


def draw_lead(d):
    d.rectangle([0, 100, W, 336], fill=LEAD_BG)
    d.rectangle([0, 100, 10, 336], fill=LEAD_EDGE)
    d.text((28, 116), "1  •  LEAD STORY", font=F_WIRE_HEAD, fill=RED)
    d.text((28, 146), "COP31 COLLAPSES — NO DEAL",
           font=F_LEAD_HEAD, fill=INK)
    para(d, (28, 200),
         "Two days into overtime, the Antalya climate summit ends with "
         "no agreement — the longest UN climate talks on record.",
         F_LEAD_BODY, 640, INK, 27)
    para(d, (28, 262),
         "The EU and about 130 parties rejected a draft that never "
         "mentioned fossil fuels.",
         F_LEAD_BODY, 640, MUTED, 27)
    draw_globe(d, 880, 218, 82, (116, 165, 205), (96, 160, 110))
    # red slash across the globe: no deal
    d.line([812, 150, 948, 286], fill=RED, width=10)
    d.line([812, 150, 948, 286], fill=(255, 255, 255), width=3)


TILES = [
    # (accent, headline, body, pictogram)
    ("blue", "DRONE HITS FLATS NEAR KYIV",
     "A Russian drone partly destroys a five-storey block in Dymer. "
     "Zelensky: 14 people missing; nine evacuated.", "building"),
    ("teal", "RUSSIAN WARSHIP HIT IN LIBYA",
     "Suspected Ukrainian sea drones hit the corvette Merkury at "
     "Benghazi. A second, Maltese-flagged ship is hit offshore.", "ship"),
    ("orange", "GULF STRIKES SPREAD",
     "Iran hits a civilian site in Bahrain — two hurt, one critically. "
     "Houthis say they struck the Rabigh refinery.", "flame"),
    ("indigo", "DEMOCRATS' BIGGEST HOUSE WIN SINCE 1992",
     "A recount win in North Carolina gives Democrats at least 258 "
     "seats. Hakeem Jeffries is set to be Speaker.", "dome"),
    ("crimson", "AI SELL-OFF DEEPENS",
     "S&P 500 −3.7%, Nikkei −5.1% as Nvidia slides on reports of an "
     "SEC accounting inquiry.", "chart"),
    ("green", "MEXICO CAPTURES 'EL CHAPO ISIDRO'",
     "FBI most-wanted cartel boss Fausto Isidro Meza Flores is seized "
     "in Sinaloa; gun battles and burning vehicles follow.", "badge"),
    ("purple", "BEPICOLOMBO REACHES MERCURY",
     "After eight years, the ESA–JAXA craft enters Mercury orbit — "
     "only the second mission to do so. A glitch cut a burn short.",
     "planet"),
    ("slate", "WORLD CHESS TITLE MATCH BEGINS",
     "Gukesh and Sindarov open their match for the world "
     "championship crown.", "chess"),
]

ACCENTS = {
    "blue": (37, 99, 235), "teal": (13, 148, 136),
    "orange": (234, 88, 12), "indigo": (79, 70, 229),
    "crimson": (190, 18, 60), "green": (21, 128, 61),
    "purple": (126, 34, 206), "slate": (71, 85, 105),
}


def draw_pictogram(d, kind, x, y, s, accent):
    """Small geometric pictogram inside a tile, top-right corner."""
    if kind == "building":
        d.rectangle([x, y + 14, x + s, y + s], fill=(120, 120, 140))
        d.rectangle([x + 6, y + 22, x + s - 6, y + 30], fill=(60, 60, 80))
        d.polygon([(x + s // 2, y + 12), (x + s, y + 24), (x, y + 24)],
                  fill=(60, 60, 80))
        d.ellipse([x + s - 12, y - 2, x + s - 2, y + 8], fill=INK)
        d.line([x + s - 14, y + 3, x + s - 20, y + 6], fill=INK, width=2)
    elif kind == "ship":
        d.polygon([(x, y + s - 8), (x + s, y + s - 8),
                   (x + s - 10, y + s), (x + 10, y + s)], fill=accent)
        d.rectangle([x + s // 2 - 4, y + 12, x + s // 2 + 4, y + s - 10],
                    fill=accent)
        d.polygon([(x + s // 2 + 4, y + 12), (x + s // 2 + 18, y + 16),
                   (x + s // 2 + 4, y + 20)], fill=RED)
        d.ellipse([x + 2, y, x + 14, y + 12], fill=AMBER)
    elif kind == "flame":
        d.polygon([(x + s // 2, y), (x + s, y + s - 8), (x, y + s - 8)],
                  fill=(234, 88, 12))
        d.polygon([(x + s // 2, y + 16), (x + s - 6, y + s - 8),
                   (x + 6, y + s - 8)], fill=(250, 204, 21))
    elif kind == "dome":
        d.rectangle([x, y + s - 10, x + s, y + s], fill=accent)
        d.rectangle([x + 4, y + s - 22, x + s - 4, y + s - 10], fill=accent)
        d.pieslice([x + 6, y + 2, x + s - 6, y + s - 12], 180, 360,
                   fill=accent)
        d.line([x + s // 2, y, x + s // 2, y - 6], fill=accent, width=3)
    elif kind == "chart":
        d.line([x, y + s - 6, x + s // 3, y + s // 2,
                x + 2 * s // 3, y + s // 2 + 8, x + s, y + s],
               fill=RED, width=4)
        d.polygon([(x + s - 2, y + s - 10), (x + s - 2, y + s + 2),
                   (x + s + 8, y + s - 2)], fill=RED)
    elif kind == "badge":
        d.ellipse([x, y, x + s, y + s], outline=accent, width=4)
        d.ellipse([x + 10, y + 10, x + s - 10, y + s - 10], fill=accent)
        d.text((x + s // 2 - 7, y + s // 2 - 10), "$", font=F_NUM,
               fill=PAPER)
    elif kind == "planet":
        d.ellipse([x, y, x + s, y + s], fill=(176, 141, 87),
                  outline=INK, width=2)
        d.ellipse([x + 8, y + 10, x + 18, y + 20], fill=(140, 110, 66))
        d.ellipse([x + s - 20, y + s - 22, x + s - 8, y + s - 10],
                  fill=(140, 110, 66))
        d.line([x - 12, y - 8, x + s // 2, y + s // 2], fill=INK, width=2)
        d.ellipse([x - 16, y - 12, x - 8, y - 4], fill=accent)
    elif kind == "chess":
        sq = s // 2
        d.rectangle([x, y, x + sq, y + sq], fill=INK)
        d.rectangle([x + sq, y + sq, x + s, y + s], fill=INK)
        d.rectangle([x + sq, y, x + s, y + sq], outline=INK, width=2)
        d.rectangle([x, y + sq, x + sq, y + s], outline=INK, width=2)
        d.ellipse([x + s // 2 - 5, y + s // 2 - 5, x + s // 2 + 5,
                   y + s // 2 + 5], fill=accent)
    elif kind == "globe":
        draw_globe(d, x + s // 2, y + s // 2, s // 2 - 2,
                   (116, 165, 205), (96, 160, 110))


def draw_tiles(d):
    x0, y0 = 8, 344
    tw, th, gap = 246, 228, 8
    for i, (accent_name, head, body, pic) in enumerate(TILES):
        col, row = i % 4, i // 4
        x = x0 + col * (tw + gap)
        y = y0 + row * (th + gap)
        accent = ACCENTS[accent_name]
        d.rectangle([x, y, x + tw, y + th], fill=PAPER,
                    outline=(200, 200, 210), width=1)
        d.rectangle([x, y, x + tw, y + 8], fill=accent)
        # number badge
        d.ellipse([x + 12, y + 20, x + 44, y + 52], fill=accent)
        num = str(i + 2)
        nw = d.textlength(num, font=F_NUM)
        d.text((x + 28 - nw / 2, y + 24), num, font=F_NUM, fill=PAPER)
        draw_pictogram(d, pic, x + tw - 62, y + 16, 44, accent)
        hy = para(d, (x + 12, y + 60), head, F_TILE_HEAD, tw - 24, INK, 21)
        para(d, (x + 12, hy + 4), body, F_TILE_BODY, tw - 24, MUTED, 18)


WIRE = [
    ("Indonesia", "candy factory fire kills at least 3; 36 missing."),
    ("Nigeria", "funeral boat capsizes; at least 24 dead."),
    ("West Bank", "settlers torch homes near Ramallah; inquiry opened."),
    ("EU–Indonesia", "sign trade deal after a decade of talks."),
    ("Health", "one-time CRISPR therapy cuts bad cholesterol 52%."),
    ("South Korea", "education minister quits over AI cheating scandal."),
    ("Poland", "three airspace objects were Russian Kh-101 missiles."),
    ("Sudan", "drone strikes hit homes and a UN building in Khartoum."),
    ("Maths", "AI 'helped prove' Riemann hypothesis, researcher says."),
    ("FBI", "crime database breach probed — second in two months."),
]


def draw_wire(d):
    d.rectangle([0, 812, W, H], fill=WIRE_BG)
    d.text((16, 824), "ALSO TODAY", font=F_WIRE_HEAD, fill=AMBER)
    d.line([16, 852, W - 16, 852], fill=(90, 100, 120), width=1)
    col_w = (W - 32) // 2
    for i, (tag, text) in enumerate(WIRE):
        col, row = i % 2, i // 2
        x = 16 + col * col_w
        y = 862 + row * 32
        d.ellipse([x, y + 5, x + 7, y + 12], fill=AMBER)
        d.text((x + 14, y), tag + ": ", font=F_WIRE, fill=AMBER)
        tw = d.textlength(tag + ": ", font=F_WIRE)
        para(d, (x + 14 + tw, y), text, F_WIRE, col_w - 14 - tw - 8,
             (220, 225, 235), 17)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    draw_header(d)
    draw_lead(d)
    draw_tiles(d)
    draw_wire(d)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "entry.png")
    img.save(out, format="PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
