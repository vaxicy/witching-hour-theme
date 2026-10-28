"""Witching Hour Theme - icon candidates.

Code-drawn marks, a light/dark contact sheet and an inline strip.

Run from the project root:  py -3 scripts/generate-icon-candidates.py
"""

import io
import math
import os

from PIL import Image, ImageDraw, ImageFont

S = 3
W = 1024

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "logo-candidates")

INK = (62, 42, 74, 255)           # #3E2A4A deep plum ink
NIGHT = (30, 22, 38, 255)         # #1E1626
PUMPKIN = (232, 114, 42, 255)     # #E8722A
PUMPKIN_D = (176, 71, 42, 255)    # #B0472A
SLIME = (168, 208, 106, 255)      # #A8D06A
SLIME_D = (94, 122, 46, 255)      # #5E7A2E
BLOOD = (176, 48, 63, 255)        # #B0303F
GHOST = (242, 237, 228, 255)      # #F2EDE4
CANDLE = (232, 198, 106, 255)     # #E8C66A

LIGHT_BG = (250, 245, 236, 255)
DARK_BG = (26, 19, 34, 255)
LIGHT_INK = (46, 30, 52, 255)
DARK_INK = (240, 232, 220, 255)

FONT_DIR = r"C:\Windows\Fonts"


def font(name, size):
    try:
        return ImageFont.truetype(os.path.join(FONT_DIR, name), size)
    except Exception:
        return ImageFont.load_default()


def scr(p):
    return (p[0] * S, p[1] * S)


def wd(v):
    return max(1, int(round(v * S)))


def canvas():
    return Image.new("RGBA", (W * S, W * S), (0, 0, 0, 0))


def finish(img):
    return img.resize((W, W), Image.LANCZOS)


def bez(p0, p1, p2, n=64):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1.0 - t
        pts.append((u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
                    u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]))
    return pts


def poly(draw, pts, fill):
    draw.polygon([scr(p) for p in pts], fill=fill)


def disc(draw, center, r, fill):
    draw.ellipse([center[0] * S - r * S, center[1] * S - r * S,
                  center[0] * S + r * S, center[1] * S + r * S], fill=fill)


def ellipse(draw, box, fill):
    draw.ellipse([scr((box[0], box[1])), scr((box[2], box[3]))], fill=fill)


def rounded(draw, box, radius, fill):
    draw.rounded_rectangle([box[0] * S, box[1] * S, box[2] * S, box[3] * S],
                           radius=wd(radius), fill=fill)


# ---------------------------------------------------------------- candidates

def cand_lantern():
    img = canvas()
    d = ImageDraw.Draw(img)

    ellipse(d, (196, 362, 560, 828), PUMPKIN)
    ellipse(d, (464, 362, 828, 828), PUMPKIN)
    ellipse(d, (286, 330, 738, 842), PUMPKIN)
    # ribs
    for x in (368, 512, 656):
        d.arc([scr((x - 96, 356)), scr((x + 96, 820))], 250, 290, fill=PUMPKIN_D, width=wd(14))

    # stem
    d.line([scr((500, 348)), scr((486, 250))], fill=SLIME_D, width=wd(34), joint="curve")

    # face
    poly(d, [(392, 520), (472, 520), (432, 596)], INK)
    poly(d, [(552, 520), (632, 520), (592, 596)], INK)
    poly(d, [(356, 646), (420, 690), (484, 646), (548, 690), (612, 646),
             (612, 712), (356, 712)], INK)

    return finish(img)


def cand_ghost():
    img = canvas()
    d = ImageDraw.Draw(img)

    disc(d, (512, 420), 226, GHOST)
    d.rectangle([scr((286, 420)), scr((738, 700))], fill=GHOST)
    for i in range(4):
        cx = 342 + i * 114
        disc(d, (cx, 700), 57, GHOST) if i % 2 == 0 else None
    poly(d, [(286, 700), (738, 700), (738, 760), (286, 760)], GHOST)

    # eyes + mouth
    ellipse(d, (400, 372, 476, 476), INK)
    ellipse(d, (548, 372, 624, 476), INK)
    ellipse(d, (476, 528, 548, 600), INK)

    # little spark
    disc(d, (760, 300), 34, SLIME)

    return finish(img)


def cand_bat():
    img = canvas()
    d = ImageDraw.Draw(img)

    # wings
    left = bez((512, 520), (300, 330), (168, 520)) + \
           bez((168, 520), (240, 520), (300, 640))
    poly(d, left + [(512, 640)], INK)
    right = bez((512, 520), (724, 330), (856, 520)) + \
            bez((856, 520), (784, 520), (724, 640))
    poly(d, right + [(512, 640)], INK)

    # body + ears
    ellipse(d, (444, 420, 580, 700), INK)
    poly(d, [(452, 440), (486, 330), (512, 440)], INK)
    poly(d, [(512, 440), (538, 330), (572, 440)], INK)

    # eyes
    disc(d, (486, 512), 17, PUMPKIN)
    disc(d, (538, 512), 17, PUMPKIN)
    disc(d, (512, 300), 30, SLIME)

    return finish(img)


def cand_cauldron():
    img = canvas()
    d = ImageDraw.Draw(img)

    # pot
    ellipse(d, (300, 330, 724, 470), INK)
    pot = bez((300, 400), (300, 700), (512, 740)) + \
          bez((512, 740), (724, 700), (724, 400))
    poly(d, pot + [(724, 400), (300, 400)], NIGHT)
    ellipse(d, (300, 330, 724, 470), INK)

    d.arc([scr((300, 330)), scr((724, 470))], 180, 360, fill=SLIME_D, width=wd(16))

    # legs
    for x in (370, 512, 654):
        d.line([scr((x, 720)), scr((x - 20, 820))], fill=INK, width=wd(30))

    # slime bubbles
    disc(d, (430, 300), 62, SLIME)
    disc(d, (560, 250), 46, SLIME_D)
    disc(d, (500, 344), 34, SLIME)

    return finish(img)


def cand_tombstone():
    img = canvas()
    d = ImageDraw.Draw(img)

    d.pieslice([scr((272, 244)), scr((752, 724))], 180, 360, fill=INK)
    d.rectangle([scr((272, 484)), scr((752, 760))], fill=INK)

    for y, w in ((470, 120), (546, 120), (622, 78)):
        d.line([scr((512 - w, y)), scr((512 + w, y))], fill=PUMPKIN, width=wd(22))

    # grass
    d.line([scr((196, 792)), scr((828, 792))], fill=SLIME_D, width=wd(26))
    for x in (250, 330, 690, 770):
        d.line([scr((x, 792)), scr((x + 26, 726))], fill=SLIME_D, width=wd(18))

    return finish(img)


def cand_cat():
    img = canvas()
    d = ImageDraw.Draw(img)

    # body
    ellipse(d, (352, 470, 700, 866), INK)
    # head
    disc(d, (512, 430), 194, INK)
    # ears
    poly(d, [(356, 336), (400, 196), (486, 350)], INK)
    poly(d, [(538, 350), (624, 196), (668, 336)], INK)
    # tail
    tail = bez((660, 760), (826, 700), (742, 560))
    d.line([scr(p) for p in tail], fill=INK, width=wd(44), joint="curve")

    # eyes + collar
    ellipse(d, (420, 392, 478, 462), PUMPKIN)
    ellipse(d, (546, 392, 604, 462), PUMPKIN)
    d.line([scr((430, 604)), scr((594, 604))], fill=SLIME, width=wd(22))
    disc(d, (512, 640), 22, CANDLE)

    return finish(img)


CANDIDATES = [
    ("01", "lantern", cand_lantern),
    ("02", "ghost", cand_ghost),
    ("03", "bat", cand_bat),
    ("04", "cauldron", cand_cauldron),
    ("05", "tombstone", cand_tombstone),
    ("06", "cat", cand_cat),
]


# ---------------------------------------------------------------- sheet bits

def centered_text(d, center, text, fnt, fill):
    b = d.textbbox((0, 0), text, font=fnt)
    x = center[0] - (b[2] - b[0]) / 2 - b[0]
    y = center[1] - (b[3] - b[1]) / 2 - b[1]
    d.text((x, y), text, font=fnt, fill=fill)


def contact_sheet(icons, bg, ink, path):
    cell_w, cell_h = 420, 540
    margin, gap = 40, 26
    head = 118
    sheet_w = margin * 2 + cell_w * 3 + gap * 2
    sheet_h = margin + head + cell_h * 2 + gap + margin

    sheet = Image.new("RGBA", (sheet_w, sheet_h), bg)
    d = ImageDraw.Draw(sheet)

    f_title = font("segoeuib.ttf", 40)
    f_num = font("segoeuib.ttf", 30)
    f_name = font("segoeui.ttf", 26)
    f_small = font("segoeui.ttf", 20)

    centered_text(d, (sheet_w / 2, margin + 34), "WITCHING HOUR THEME", f_title, ink)
    centered_text(d, (sheet_w / 2, margin + 82), "icon candidates", f_small, ink)

    for idx, (num, name, icon) in enumerate(icons):
        row, col = divmod(idx, 3)
        gx = margin + col * (cell_w + gap)
        gy = margin + head + row * (cell_h + gap)

        sheet.alpha_composite(icon.resize((260, 260), Image.LANCZOS),
                              (gx + (cell_w - 260) // 2, gy + 30))

        centered_text(d, (gx + cell_w / 2, gy + 330), num, f_num, ink)
        centered_text(d, (gx + cell_w / 2, gy + 372), name, f_name, ink)
        centered_text(d, (gx + cell_w / 2, gy + 404), "1024 x 1024  PNG", f_small, ink)

        thumb = icon.resize((32, 32), Image.LANCZOS)
        tx, ty = gx + cell_w - 32 - 22, gy + cell_h - 32 - 22
        d.rectangle([tx - 10, ty - 10, tx + 42, ty + 42],
                    outline=(ink[0], ink[1], ink[2], 70), width=1)
        sheet.alpha_composite(thumb, (tx, ty))

    save_png(sheet.convert("RGB"), path)


def inline_strip(icons, path):
    size, gap, margin = 150, 18, 30
    strip_w = margin * 2 + size * len(icons) + gap * (len(icons) - 1)
    strip_h = margin * 2 + size + 34
    strip = Image.new("RGBA", (strip_w, strip_h), LIGHT_BG)
    d = ImageDraw.Draw(strip)
    f_num = font("segoeuib.ttf", 20)

    for idx, (num, _name, icon) in enumerate(icons):
        x = margin + idx * (size + gap)
        strip.alpha_composite(icon.resize((size, size), Image.LANCZOS), (x, margin))
        centered_text(d, (x + size / 2, margin + size + 16), num, f_num, LIGHT_INK)

    save_png(strip.convert("RGB"), path)


def save_png(img, path):
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(buf.getvalue())


def main():
    os.makedirs(OUT, exist_ok=True)

    icons = []
    for num, name, fn in CANDIDATES:
        icon = fn()
        box = icon.getbbox()
        if box is None:
            raise AssertionError("%s rendered empty" % name)
        left, top, right, bottom = box
        lo, hi = 70, 954
        if left < lo or top < lo or right > hi or bottom > hi:
            raise AssertionError("%s out of safe area: %s" % (name, box))
        path = os.path.join(OUT, "%s-%s.png" % (num, name))
        save_png(icon, path)
        print("wrote", os.path.relpath(path, ROOT), box)
        icons.append((num, name, icon))

    contact_sheet(icons, LIGHT_BG, LIGHT_INK, os.path.join(OUT, "contact-light.png"))
    contact_sheet(icons, DARK_BG, DARK_INK, os.path.join(OUT, "contact-dark.png"))
    inline_strip(icons, os.path.join(OUT, "inline-strip.png"))
    print("wrote contact-light.png / contact-dark.png / inline-strip.png")


if __name__ == "__main__":
    main()
