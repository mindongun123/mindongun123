"""Generate unified 16:10 showcase thumbnails into assets/games/thumbs/.

Usage: python assets/games/make_thumbs.py
Icons are cropped from the original banner images in assets/games/.
"""
import math
import os
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "thumbs")
W, H = 1200, 750
FONTS = "C:/Windows/Fonts/"
F_BLACK = FONTS + "seguibl.ttf"
F_BOLD = FONTS + "segoeuib.ttf"
F_SEMI = FONTS + "seguisb.ttf"

# id, title, genre, tagline, gradient (top-left, bottom-right), source crop (file, l, t, r, b as fractions)
GAMES = [
    ("matchkit", "Match Kit", "MATCH-3", "Combo, pop, repeat!", ("#FF8FB1", "#8B5CF6"), ("matchkit.png", .02, .08, .18, .92)),
    ("merge", "Merge Restaurant", "MERGE", "Bake, merge & grow your cafe", ("#FDBA74", "#F43F5E"), ("merge.png", 0, 0, 1, 1)),
    ("tapmusic", "Tap Music", "MUSIC · TAP", "Tap to the beat", ("#A855F7", "#2563EB"), ("tapmusic.png", .02, .08, .18, .9)),
    ("block", "Block Puzzle", "PUZZLE", "Place, clear, chill", ("#2DD4BF", "#0EA5E9"), ("block.png", .02, .1, .185, .94)),
    ("emoji", "Emoji Riddles", "PUZZLE", "Match the feelings", ("#FDE047", "#FB923C"), ("emoji.png", .02, .08, .185, .92)),
    ("runner", "Runner 3D", "HYPER-CASUAL", "One thumb, endless run", ("#38BDF8", "#6366F1"), ("runner3d.png", .05, .08, .27, .94)),
    ("connect", "Dot Connect", "PUZZLE", "Connect & fill the board", ("#4ADE80", "#0D9488"), ("gconnect.png", .045, .08, .225, .94)),
    ("jump", "Jump Adventure", "CASUAL", "Bounce through bright worlds", ("#7DD3FC", "#22C55E"), ("mario.png", .02, .08, .18, .92)),
]

LOGO = [
    [(0, 571), (266, 571), (266, 2672), (0, 2672)],
    [(266, 571), (761, 1255), (761, 1708), (266, 1024)],
    [(761, 0), (1027, 0), (1027, 2081), (761, 2081)],
    [(483, 158), (2253, 158), (2253, 424), (483, 424)],
    [(1027, 1262), (1524, 571), (1524, 1034), (1027, 1716)],
    [(1524, 571), (1790, 571), (1790, 2672), (1524, 2672)],
    [(1987, 424), (2253, 424), (2253, 1199), (1987, 1235)],
    [(2253, 1199), (1172, 2685), (956, 2528), (1987, 1109)],
]


def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def gradient(c1, c2, size):
    a, b = hex2rgb(c1), hex2rgb(c2)
    w, h = size
    small = Image.new("RGB", (64, 40))
    px = small.load()
    for y in range(40):
        for x in range(64):
            t = (x / 63 * 0.6 + y / 39 * 0.4)
            px[x, y] = tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))
    return small.resize(size, Image.BICUBIC).convert("RGBA")


def rounded(im, r):
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, *im.size), r, fill=255)
    out = im.copy()
    out.putalpha(mask)
    return out


def shadow(size, r, blur, alpha=90):
    pad = blur * 3
    sh = Image.new("RGBA", (size[0] + pad * 2, size[1] + pad * 2), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((pad, pad, pad + size[0], pad + size[1]), r, fill=(15, 23, 42, alpha))
    return sh.filter(ImageFilter.GaussianBlur(blur)), pad


def star(cx, cy, r):
    pts = []
    for i in range(10):
        a = math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(a), cy - rr * math.sin(a)))
    return pts


def logo_mark(height):
    s = height / 2686
    w = int(2254 * s) + 2
    mask = Image.new("L", (w, height + 2), 0)
    d = ImageDraw.Draw(mask)
    for poly in LOGO:
        d.polygon([(x * s, y * s) for x, y in poly], fill=255)
    mark = Image.new("RGBA", mask.size, (255, 255, 255, 0))
    mark.putalpha(mask)
    return mark


def fit_font(text, path, size, max_w):
    while size > 30:
        f = ImageFont.truetype(path, size)
        if f.getlength(text) <= max_w:
            return f
        size -= 4
    return ImageFont.truetype(path, size)


def load_icon(spec):
    f, l, t, r, b = spec
    im = Image.open(os.path.join(HERE, f)).convert("RGBA")
    w, h = im.size
    return im.crop((int(l * w), int(t * h), int(r * w), int(b * h)))


def make(game):
    gid, title, genre, tagline, (c1, c2), spec = game
    rnd = random.Random(gid)
    img = gradient(c1, c2, (W, H))

    # soft blobs
    deco = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(deco)
    d.ellipse((W - 380, -220, W + 220, 380), fill=(255, 255, 255, 46))
    d.ellipse((-200, H - 260, 300, H + 240), fill=(255, 255, 255, 34))
    d.ellipse((560, H - 140, 820, H + 120), fill=(255, 255, 255, 22))
    img.alpha_composite(deco.filter(ImageFilter.GaussianBlur(2)))

    # confetti
    conf = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(conf)
    spots = [(540, 70), (980, 60), (1150, 150), (640, 640), (60, 60), (800, 600), (1150, 570)]
    for i, (x, y) in enumerate(spots):
        k = (i + rnd.randint(0, 2)) % 3
        s = rnd.randint(12, 22)
        col = (255, 255, 255, rnd.randint(150, 220))
        if k == 0:
            d.ellipse((x - s, y - s, x + s, y + s), fill=col)
        elif k == 1:
            d.rounded_rectangle((x - s, y - s, x + s, y + s), s // 2, fill=col)
        else:
            d.polygon(star(x, y, s * 1.4), fill=(253, 224, 71, 235))
    img.alpha_composite(conf)

    # icon card (white frame, slight tilt)
    icon = load_icon(spec)
    side = 380
    icon = icon.resize((side, side), Image.LANCZOS)
    pad = 18
    card = Image.new("RGBA", (side + pad * 2, side + pad * 2), (255, 255, 255, 255))
    card = rounded(card, 64)
    card.alpha_composite(rounded(icon, 48), (pad, pad))
    card = card.rotate(-5, resample=Image.BICUBIC, expand=True)
    sh, sp = shadow((side + pad * 2, side + pad * 2), 64, 28, 110)
    sh = sh.rotate(-5, resample=Image.BICUBIC, expand=True)
    cx, cy = 70, (H - card.height) // 2 - 10
    img.alpha_composite(sh, (cx - sp + 6, cy - sp + 26))
    img.alpha_composite(card, (cx, cy))

    # text block
    d = ImageDraw.Draw(img)
    tx = 560
    f_pill = ImageFont.truetype(F_BOLD, 30)
    pw = int(f_pill.getlength(genre)) + 48
    d.rounded_rectangle((tx, 200, tx + pw, 254), 27, fill=(255, 255, 255, 255))
    d.text((tx + 24, 227), genre, font=f_pill, fill=hex2rgb(c2), anchor="lm")

    f_title = fit_font(title, F_BLACK, 104, W - tx - 50)
    words = title.split()
    lines = [title]
    if f_title.size < 84 and len(words) > 1:
        lines = [" ".join(words[:-1]), words[-1]]
        f_title = fit_font(max(lines, key=len), F_BLACK, 104, W - tx - 50)
    y = 280
    for ln in lines:
        d.text((tx + 3, y + 5), ln, font=f_title, fill=(15, 23, 42, 60))
        d.text((tx, y), ln, font=f_title, fill=(255, 255, 255))
        y += int(f_title.size * 1.08)

    f_tag = ImageFont.truetype(F_SEMI, 38)
    d.text((tx + 2, y + 16), tagline, font=f_tag, fill=(255, 255, 255, 235))

    # brand mark bottom-right
    mark = logo_mark(46)
    f_brand = ImageFont.truetype(F_BLACK, 30)
    bw = mark.width + 14 + int(f_brand.getlength("MJ GAME"))
    bx, by = W - bw - 48, H - 84
    img.alpha_composite(mark, (bx, by))
    d.text((bx + mark.width + 14, by + 24), "MJ GAME", font=f_brand, fill=(255, 255, 255), anchor="lm")

    img = rounded(img, 40)
    os.makedirs(OUT, exist_ok=True)
    img.save(os.path.join(OUT, f"{gid}.png"), optimize=True)
    print("wrote", gid)


if __name__ == "__main__":
    for g in GAMES:
        make(g)
