from PIL import Image, ImageDraw, ImageFont
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
F = ROOT/"fonts"; OUT = ROOT/"titles"; OUT.mkdir(exist_ok=True)
W, H = 1920, 1080
INK   = (242, 241, 236, 255)
AMBER = (242, 84, 27, 255)
STEEL = (178, 184, 188, 255)

def gothic(sz): return ImageFont.truetype(str(F/"LeagueGothic.ttf"), sz)
def black(sz):  return ImageFont.truetype(str(F/"ArchivoBlack-Regular.ttf"), sz)
def mono(sz):   return ImageFont.truetype(str(F/"IBMPlexMono-Medium.ttf"), sz)

def scrim(img, to_x=1250, alpha=200):
    """Dark gradient from the left so type holds over any footage."""
    g = Image.new("L", (W, 1))
    for x in range(W):
        t = min(1.0, max(0.0, x / to_x))
        g.putpixel((x, 0), int(alpha * (1 - t) ** 1.5))
    g = g.resize((W, H))
    layer = Image.new("RGBA", (W, H), (10, 12, 13, 255)); layer.putalpha(g)
    img.alpha_composite(layer)

def card():
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))

def lines(d, items, x, y):
    for text, font, fill, gap in items:
        d.text((x, y), text, font=font, fill=fill)
        y += gap

# --- 1. the name ---
img = card(); scrim(img); d = ImageDraw.Draw(img)
d.text((140, 620), "ANVIL", font=gothic(300), fill=INK)
d.rectangle([144, 905, 144 + 96, 905 + 9], fill=AMBER)
d.text((144, 946), "NUCLEIC ACID SYNTHESIS", font=mono(31), fill=STEEL)
d.text((144, 988), "MADE IN AMERICA", font=mono(31), fill=STEEL)
img.save(OUT/"01-name.png")

# --- 2. the argument ---
img = card(); scrim(img); d = ImageDraw.Draw(img)
lines(d, [("EVERY PLATE TAKES", black(92), INK, 104),
          ("ITS OWN ROUTE.",    black(92), INK, 104)], 140, 700)
img.save(OUT/"02-route.png")

# --- 3. no changeover ---
img = card(); scrim(img); d = ImageDraw.Draw(img)
lines(d, [("96 DIFFERENT SEQUENCES.", black(78), INK, 92),
          ("NO CHANGEOVER.",          black(78), INK, 92)], 140, 716)
img.save(OUT/"03-nochange.png")

# --- 4. the screening rule ---
img = card(); scrim(img); d = ImageDraw.Draw(img)
lines(d, [("NO VERIFIED SCREEN.", black(86), INK, 98),
          ("NO SYNTHESIS.",       black(86), INK, 98)], 140, 652)
d.rectangle([144, 862, 144 + 560, 862 + 10], fill=AMBER)
d.text((144, 904), "NSTM-6 · SCREENING ENFORCED IN HARDWARE", font=mono(29), fill=STEEL)
img.save(OUT/"04-screen.png")

# --- 5. built here ---
img = card(); scrim(img); d = ImageDraw.Draw(img)
d.text((140, 736), "BUILT HERE.", font=black(104), fill=INK)
img.save(OUT/"05-built.png")

# --- 6. end card, full frame ---
img = Image.new("RGBA", (W, H), (185, 182, 174, 255)); d = ImageDraw.Draw(img)
px, py, pw, ph = 610, 300, 700, 282
from PIL import ImageFilter                                            # soft drop shadow
sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(sh).rectangle([px + 16, py + 24, px + pw + 16, py + ph + 24], fill=(14, 16, 17, 150))
img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(18)))
for i in range(ph):                                                   # brushed plate
    t = i / ph; v = int(214 - 66 * t)
    d.rectangle([px, py + i, px + pw, py + i], fill=(v, v, max(0, v - 4)))
d.rectangle([px, py, px + pw, py + ph], outline=(126, 133, 138), width=3)
d.rectangle([px + 3, py + 3, px + pw - 3, py + 5], fill=(242, 241, 236))

ANVIL_MARK = [(3,38),(12,30),(24,24),(38,20),(112,20),(112,40),(78,42),(76,70),
              (104,74),(104,92),(32,92),(32,74),(60,70),(58,42),(24,40)]
s, mx, my = 1.30, px + 58, py + 86
d.polygon([(mx + x * s, my + y * s) for x, y in ANVIL_MARK], fill=AMBER)
d.text((px + 240, py + 62), "ANVIL", font=gothic(190), fill=(42, 46, 49))

d.text((px + 4, 614), "ADHERENT BY DESIGN", font=mono(29), fill=(21, 24, 26))
d.rectangle([px, 676, px + 404, 676 + 92], fill=AMBER)
d.text((px + 38, 704), "REQUEST A QUOTE", font=mono(33), fill=(27, 13, 6))
d.text((px + 4, 800), "YOUR-DOMAIN.COM", font=mono(28), fill=(74, 80, 84))
img.convert("RGB").save(OUT/"06-endcard.png")

for p in sorted(OUT.glob("*.png")):
    print(f"{p.name:18} {p.stat().st_size//1024}KB")

# --- 7. end lockup, transparent, to sit over darkened hero footage ---
img = card(); d = ImageDraw.Draw(img)
s, mx, my = 1.55, 142, 452
d.polygon([(mx + x * s, my + y * s) for x, y in ANVIL_MARK], fill=AMBER)
d.text((348, 404), "ANVIL", font=gothic(236), fill=INK)
d.rectangle([352, 646, 352 + 112, 646 + 9], fill=AMBER)
d.text((352, 690), "ADHERENT BY DESIGN", font=mono(31), fill=STEEL)
d.rectangle([352, 762, 352 + 412, 762 + 94], fill=AMBER)
d.text((352 + 40, 791), "REQUEST A QUOTE", font=mono(33), fill=(27, 13, 6))
d.text((356, 888), "YOUR-DOMAIN.COM", font=mono(28), fill=STEEL)
img.save(OUT/"07-endlockup.png")
print("07-endlockup.png written")
