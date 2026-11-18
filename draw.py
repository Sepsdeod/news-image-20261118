#!/usr/bin/env python3
"""Draw the front page of 18 November 2026's world news.

Original work: a newspaper-style poster drawn with Pillow from simple
shapes and text only (no photos, no copied art). Deterministic: the same
code always writes the same bytes.

Run:  python3 draw.py            -> writes entry.png next to this file
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 231)
INK = (24, 24, 22)
RED = (158, 28, 28)
BLUE = (31, 78, 121)
TEAL = (44, 110, 120)
SEA = (188, 214, 226)
LAND = (232, 214, 176)
GREY = (96, 96, 90)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, leading, fill=INK):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def hrule(draw, x0, x1, y, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def kicker(draw, x, y, text, fnt, fill=RED):
    draw.text((x, y), text, font=fnt, fill=fill)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------------------------------------------------------------- masthead
d.rectangle([0, 0, W, 118], fill=(30, 30, 28))
mast = font(SERIF_B, 92)
d.text((32, 6), "THE WORLD", font=mast, fill=(246, 241, 231))
d.text((700, 34), "ONE DAY", font=font(SANS_B, 26), fill=(246, 241, 231))
d.text((700, 64), "ONE PICTURE", font=font(SANS_B, 26), fill=(246, 241, 231))
hrule(d, 0, W, 118, 3, RED)

# date banner — the day this poster sums up, named loud and clear
d.rectangle([0, 118, W, 168], fill=RED)
date_f = font(SERIF_B, 30)
d.text((32, 130), "WEDNESDAY  18  NOVEMBER  2026", font=date_f,
       fill=(255, 255, 255))
d.text((712, 134), "WORLD NEWS IN ONE IMAGE", font=font(SANS_B, 15),
       fill=(255, 220, 210))

# ---------------------------------------------------------------- lead story
LX, LY, LW = 32, 190, 560
kicker(d, LX, LY, "LEAD  •  THE GULF", font(SANS_B, 20))
y = LY + 30
y = para(d, LX, y, "Gulf flares again", font(SERIF_B, 52), LW, 58)
y = para(d, LX, y + 4,
         "Iranian drones target a US radar base in Bahrain; US jets answer "
         "with a strike on Qeshm Island.",
         font(SERIF, 24), LW, 31)
y += 6
y = para(d, LX, y,
         "Tehran's third attack in five days on American targets in the "
         "island kingdom, host of the US Navy's 5th Fleet. Bahrain and US "
         "Central Command say the drones were intercepted: no damage, no "
         "injuries. Hours later, US jets hit a Guard missile site on "
         "Qeshm Island.",
         font(SANS, 20), LW, 26)
y += 10
hrule(d, LX, LX + LW, y, 2, RED)
y += 12
d.text((LX, y), "A two-month lull in fighting ends.",
       font=font(SANS_B, 20), fill=RED)

# schematic map of the Gulf (right of the lead text)
MX, MY, MW, MH = 624, 190, 368, 330
d.rectangle([MX, MY, MX + MW, MY + MH], outline=INK, width=3, fill=SEA)
d.text((MX + 12, MY + 8), "THE GULF — SCHEMATIC", font=font(SANS_B, 16),
       fill=BLUE)
# land masses: Arabia (left/bottom), Iran (top/right)
d.polygon([(MX, MY + 150), (MX + 150, MY + 120), (MX + 170, MY + 330),
           (MX, MY + 330)], fill=LAND)
d.polygon([(MX + 150, MY + 40), (MX + 368, MY + 40), (MX + 368, MY + 150),
           (MX + 250, MY + 170), (MX + 190, MY + 120)], fill=LAND)
# Strait of Hormuz label + Qeshm Island
d.ellipse([MX + 250, MY + 168, MX + 330, MY + 196], fill=(210, 120, 60),
          outline=INK, width=2)
d.text((MX + 236, MY + 200), "QESHM ISLAND", font=font(SANS_B, 14), fill=INK)
d.text((MX + 218, MY + 224), "Strait of Hormuz", font=font(SANS, 15), fill=BLUE)
# Bahrain dot
d.ellipse([MX + 118, MY + 148, MX + 134, MY + 164], fill=RED, outline=INK,
          width=2)
d.text((MX + 60, MY + 170), "BAHRAIN", font=font(SANS_B, 14), fill=RED)
d.text((MX + 30, MY + 190), "US 5th Fleet", font=font(SANS, 14), fill=INK)
# drone flight arrows: Iran -> Bahrain, US -> Qeshm
for (x0, y0, x1, y1) in [(MX + 280, MY + 90, MX + 140, MY + 150),
                         (MX + 60, MY + 300, MX + 270, MY + 185)]:
    d.line([(x0, y0), (x1, y1)], fill=RED, width=3)
    d.polygon([(x1, y1), (x1 - 12, y1 - 2), (x1 - 2, y1 - 12)], fill=RED)


def tag(x, y, text, fnt, fill=RED):
    w = d.textlength(text, font=fnt)
    d.rectangle([x - 3, y - 2, x + w + 3, y + 20], fill=(246, 241, 231))
    d.text((x, y), text, font=fnt, fill=fill)


tag(MX + 215, MY + 58, "drones", font(SANS_B, 14))
tag(MX + 16, MY + 252, "US jets strike back", font(SANS_B, 14))
d.text((MX + 150, MY + MH - 24), "IRAN (top)  •  ARABIA (left)",
       font=font(SANS, 13), fill=GREY)

# ---------------------------------------------------------------- three panels
PY = 572
PW = (W - 64 - 2 * 24) // 3  # 296
PX = [32, 32 + PW + 24, 32 + 2 * (PW + 24)]


def panel(x, y, w, h, kick, head, body, accent=BLUE):
    d.rectangle([x, y, x + w, y + h], outline=INK, width=2, fill=(255, 252, 245))
    d.rectangle([x, y, x + w, y + 6], fill=accent)
    yy = y + 16
    d.text((x + 14, yy), kick, font=font(SANS_B, 15), fill=accent)
    yy += 24
    yy = para(d, x + 14, yy, head, font(SERIF_B, 25), w - 28, 30)
    yy += 6
    para(d, x + 14, yy, body, font(SANS, 18), w - 28, 23)


panel(PX[0], PY, PW, 212, "DIPLOMACY  •  MANILA",
      "Trump lands in Manila for Quad talks",
      "The US president arrives in the Philippines for talks with Japan, "
      "India and Australia.",
      accent=BLUE)
panel(PX[1], PY, PW, 212, "TECH  •  SILICON VALLEY",
      "Nvidia board says no to Huang return",
      "Days after the founder quit, the board rules out bringing Jensen "
      "Huang back as chief executive.",
      accent=TEAL)
panel(PX[2], PY, PW, 212, "WAR  •  UKRAINE",
      "Crimea bridge hit for a second day",
      "Ukraine strikes the Kerch bridge again as Russia pounds bridges in "
      "Kyiv. Moscow claims 1,441 drones downed.",
      accent=RED)

# ---------------------------------------------------------------- two panels
QY = 798
QW = (W - 64 - 24) // 2  # 464
panel(32, QY, QW, 146, "WEATHER  •  BAY OF BENGAL",
      "Cyclone Akvan bears down",
      "The storm over the Bay of Bengal is set to strengthen into a severe "
      "cyclonic storm by Thursday, India warns.",
      accent=TEAL)
panel(32 + QW + 24, QY, QW, 146, "SPORT  •  CRICKET",
      "Dhoni calls time on the IPL",
      "MS Dhoni ends his playing career and becomes Chennai Super Kings' "
      "mentor — closing one of cricket's great chapters.",
      accent=BLUE)

# ---------------------------------------------------------------- footer ticker
FY = 956
hrule(d, 32, W - 32, FY, 3, RED)
para(d, 32, FY + 12,
     "ALSO TODAY:  EU plans a €45bn loan to keep Ukraine funded  •  Britain "
     "and Australia sanction West Bank settlement firms  •  Estonia to shut "
     "its Russia border after a sabotage bid",
     font(SANS_B, 18), W - 64, 24, fill=INK)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
