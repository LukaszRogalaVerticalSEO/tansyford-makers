"""T2: buduje stronę testową „Tansyford Makers" - trzy fikcyjne pracownie.

A  Ostrevane Lantern Works  - adres, założyciel, rok TYLKO w JSON-LD, wymyślony słownik
B  Brackenfold Ceramics     - te same typy faktów TYLKO w JSON-LD, poprawne schema.org
C  Tessellane Rope Company  - kontrola: tych faktów nie ma nigdzie

Żaden z testowanych faktów nie może pojawić się w widocznym tekście, tytule, opisie ani alt.
"""
import json, os, sys, html

OUT = sys.argv[1]
BASE = "https://lukaszrogalaverticalseo.github.io/tansyford-makers/"
# Testowane fakty NIE leżą w repozytorium: przychodzą z sekretu T2_FACTS (JSON:
# {"jsonld": {slug: obiekt}, "forbidden": [...]}) i trafiają wyłącznie do opublikowanego JSON-LD.
_FACTS = json.loads(os.environ["T2_FACTS"])
FORBIDDEN = _FACTS["forbidden"]

DISCLOSURE = ("Research test site. Tansyford and the workshops described here are fictional. "
              "The site exists to study how search engines and AI assistants read web pages.")

SHOPS = {
    "ostrevane-lantern-works": {
        "name": "Ostrevane Lantern Works",
        "accent": "#b5652b", "accent_soft": "#f6e7da",
        "tagline": "Hand-raised copper lanterns, made one at a time.",
        "desc": "Ostrevane Lantern Works makes hand-raised copper and brass lanterns for porches, "
                "gardens and boats, finished with a living patina.",
        "intro": [
            "Every Ostrevane lantern starts as a flat sheet of copper. It is annealed, raised over "
            "a stake with a planishing hammer and seamed by hand, so no two lanterns have quite the "
            "same curve.",
            "The workshop began with a single lantern made for a friend's narrowboat. People kept "
            "asking where it came from, and the second lantern followed, then the tenth. Today the "
            "bench turns out a few dozen pieces a season, each stamped with the maker's mark on the "
            "underside of the cap.",
        ],
        "products": [
            ("Harbour Lantern", "A tall hurricane lantern with a hand-blown glass chimney and a "
             "folding bail handle. Rated for outdoor use and salt air.", "£340"),
            ("Porch Sconce", "A wall-mounted lantern with a riveted back plate, wired for a "
             "low-voltage LED filament bulb.", "£260"),
            ("Garden Lantern", "A squat, wide-based lantern for tables and steps, made for candles "
             "up to 7 cm across.", "£180"),
            ("Pierced Tealight Cup", "A small raised cup with a pierced star pattern that throws "
             "light across the table.", "£45"),
        ],
        "process": [
            ("Anneal", "The copper is heated until it glows dull red and quenched, which makes it "
             "soft enough to move under the hammer."),
            ("Raise", "Course by course, the sheet is hammered over a steel stake until the body "
             "of the lantern takes its shape."),
            ("Seam and solder", "Seams are folded and sweated with silver solder, so they stay "
             "watertight for decades."),
            ("Patina", "Each lantern is left to weather or given a verdigris or dark bronze patina "
             "by hand."),
        ],
        "faq": [
            ("Can a lantern stay outside all year?", "Yes. Copper and brass do not rust. The "
             "surface will darken and may turn green over time, which is part of the finish."),
            ("Do you make lanterns to order?", "Commissions are taken twice a year. Sizes, glass "
             "and patina can be adjusted; the raising method stays the same."),
            ("How do I clean one?", "Wipe the glass with a soft cloth. Leave the metal alone unless "
             "you want the bright finish back, in which case a paste of lemon and salt works."),
        ],
        "jsonld": None,  # z sekretu T2_FACTS
    },
    "brackenfold-ceramics": {
        "name": "Brackenfold Ceramics",
        "accent": "#3f6b5c", "accent_soft": "#e2ede8",
        "tagline": "Wood-fired stoneware for everyday tables.",
        "desc": "Brackenfold Ceramics throws wood-fired stoneware mugs, bowls and jugs, glazed with "
                "ash from the kiln's own firings.",
        "intro": [
            "Brackenfold pots are thrown on a kick wheel and fired for three days in a wood-burning "
            "kiln. Ash from the fire settles on the shoulders of each pot and melts into a glaze, "
            "so the kiln decides the final colour as much as the potter does.",
            "The studio makes useful things: mugs that hold a proper cup of tea, bowls that stack, "
            "jugs that pour without dripping. Firings happen four times a year, and each one "
            "produces a few hundred pieces.",
        ],
        "products": [
            ("Tea Mug", "A 350 ml mug with a pulled handle and a flashing of natural ash glaze on "
             "the rim.", "£32"),
            ("Nesting Bowls", "A set of three bowls in graded sizes, glazed inside with a celadon "
             "and left raw outside.", "£95"),
            ("Pouring Jug", "A one-litre jug with a sharp, turned spout that cuts the pour cleanly.",
             "£70"),
            ("Serving Platter", "A wide, low platter pressed from a slab and marked by the flame "
             "path in the kiln.", "£120"),
        ],
        "process": [
            ("Throw", "Clay is wedged and thrown on a kick wheel, then trimmed when leather-hard."),
            ("Bisque", "Pots are fired once at a low temperature so they can be glazed without "
             "falling apart."),
            ("Wood firing", "The kiln is stoked around the clock for three days, reaching over "
             "1,300 degrees."),
            ("Unpack", "After a week of cooling, every pot is checked, sanded on the foot and "
             "photographed."),
        ],
        "faq": [
            ("Are the pots safe for the dishwasher?", "Yes. Stoneware fired this hot is fully "
             "vitrified and handles dishwashers, ovens and microwaves."),
            ("Why do two mugs look different?", "Ash, flame and position in the kiln change every "
             "piece. Colour and texture vary even within one firing."),
            ("Do you sell seconds?", "Pots with small flaws are sold after each firing at a lower "
             "price, marked with a second stamp on the foot."),
        ],
        "jsonld": None,  # z sekretu T2_FACTS
    },
    "tessellane-rope-company": {
        "name": "Tessellane Rope Company",
        "accent": "#2f4f7a", "accent_soft": "#e1e8f2",
        "tagline": "Laid-by-hand rope for boats, gardens and gyms.",
        "desc": "Tessellane Rope Company lays three-strand rope by hand from hemp, manila and "
                "polyester, for boats, gardens, climbing frames and gyms.",
        "intro": [
            "Tessellane rope is laid on a traditional rope walk: yarns are twisted into strands, "
            "and three strands are twisted together against their lay so the rope holds its shape "
            "under load.",
            "Most customers come for mooring lines and bell ropes, then return for garden edging, "
            "stair banisters and gym climbing ropes. Every coil is measured, whipped at both ends "
            "and tagged with its fibre and breaking strain.",
        ],
        "products": [
            ("Mooring Line", "Three-strand polyester with a spliced eye, UV-stable and soft in the "
             "hand.", "£4.80 per metre"),
            ("Hemp Banister Rope", "Natural hemp in 32 mm, for stair and garden rails, with brass "
             "end caps.", "£9.50 per metre"),
            ("Manila Climbing Rope", "A 38 mm gym rope with a whipped tail and a galvanised "
             "hanging thimble.", "£110"),
            ("Bell Rope", "A hemp rope with a woven wool sally in two colours.", "£85"),
        ],
        "process": [
            ("Spin", "Fibres are combed and spun into yarns of an even twist."),
            ("Form", "Yarns are twisted together into three strands."),
            ("Lay", "The strands are laid together on the rope walk, turning against their own "
             "twist."),
            ("Finish", "Each coil is measured, tested, whipped and tagged."),
        ],
        "faq": [
            ("How strong is your mooring line?", "Every size is listed with its minimum breaking "
             "strain, measured on a sample from the same batch."),
            ("Can you splice eyes and loops?", "Yes. Eye splices, back splices and short splices "
             "are made by hand to order."),
            ("Hemp or polyester?", "Hemp looks traditional and grips well but needs to dry out. "
             "Polyester lasts longer in water and sun."),
        ],
        "jsonld": {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": "Tessellane Rope Company",
            "url": BASE + "tessellane-rope-company/",
            "description": "Hand-laid three-strand rope for boats, gardens and gyms.",
        },
    },
}

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700'
         '&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">')

e = html.escape


def head(title, desc, url, css_prefix, jsonld=None, accent=None, accent_soft=None):
    ld = ""
    if jsonld is not None:
        ld = ('<script type="application/ld+json">\n'
              + json.dumps(jsonld, ensure_ascii=False, indent=2) + "\n</script>")
    style = ""
    if accent:
        style = f"<style>:root{{--accent:{accent};--accent-soft:{accent_soft}}}</style>"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
{FONTS}
<link rel="stylesheet" href="{css_prefix}assets/site.css">
{style}
{ld}
</head>
"""


def header(prefix):
    return (f'<header class="site-head"><div class="wrap">'
            f'<a class="brand" href="{prefix}">Tansyford Makers</a>'
            f'<nav><a href="{prefix}ostrevane-lantern-works/">Lanterns</a>'
            f'<a href="{prefix}brackenfold-ceramics/">Ceramics</a>'
            f'<a href="{prefix}tessellane-rope-company/">Rope</a></nav></div></header>')


def footer():
    return (f'<footer class="site-foot"><div class="wrap"><p class="brand-foot">Tansyford Makers</p>'
            f'<p class="disclosure">{e(DISCLOSURE)}</p></div></footer>')


def shop_page(slug, s):
    url = BASE + slug + "/"
    title = f"{s['name']} - {s['tagline'].rstrip('.')}"
    prods = "".join(
        f'<article class="card"><h3>{e(n)}</h3><p>{e(d)}</p><p class="price">{e(p)}</p></article>'
        for n, d, p in s["products"])
    steps = "".join(
        f'<li><span class="step-n">{i}</span><div><h3>{e(n)}</h3><p>{e(d)}</p></div></li>'
        for i, (n, d) in enumerate(s["process"], 1))
    faq = "".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in s["faq"])
    intro = "".join(f"<p>{e(p)}</p>" for p in s["intro"])
    return (head(title, s["desc"], url, "../", s["jsonld"], s["accent"], s["accent_soft"])
            + "<body>" + header("../")
            + f'<main><section class="hero"><div class="wrap"><p class="eyebrow">Tansyford Makers</p>'
              f'<h1>{e(s["name"])}</h1><p class="lede">{e(s["tagline"])}</p></div></section>'
              f'<section class="wrap about"><h2>About the workshop</h2>{intro}</section>'
              f'<section class="band"><div class="wrap"><h2>What we make</h2>'
              f'<div class="grid">{prods}</div></div></section>'
              f'<section class="wrap"><h2>How it is made</h2><ol class="steps">{steps}</ol></section>'
              f'<section class="wrap faq"><h2>Questions</h2>{faq}</section></main>'
            + footer() + "</body></html>\n")


def index_page():
    cards = "".join(
        f'<a class="card link-card" href="{slug}/" style="--accent:{s["accent"]}">'
        f'<h3>{e(s["name"])}</h3><p>{e(s["desc"])}</p><span class="more">Visit the workshop</span></a>'
        for slug, s in SHOPS.items())
    desc = "Three small craft workshops: copper lanterns, wood-fired ceramics and hand-laid rope."
    return (head("Tansyford Makers - small craft workshops", desc, BASE, "", None,
                 "#6b4f2a", "#f1ebe1")
            + "<body>" + header("")
            + '<main><section class="hero"><div class="wrap"><p class="eyebrow">Directory</p>'
              '<h1>Tansyford Makers</h1><p class="lede">Three small workshops that still make things '
              'by hand: copper lanterns, wood-fired ceramics and laid rope.</p></div></section>'
              f'<section class="wrap"><div class="grid three">{cards}</div></section></main>'
            + footer() + "</body></html>\n")


CSS = """:root{--ink:#1f1d1a;--muted:#5d5850;--paper:#fbf8f3;--line:#e6e0d6;--accent:#6b4f2a;--accent-soft:#f1ebe1}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font:400 17px/1.65 Inter,system-ui,sans-serif}
.wrap{max-width:1040px;margin:0 auto;padding:0 20px}
a{color:var(--accent)}
.site-head{border-bottom:1px solid var(--line);background:#fff}
.site-head .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:64px;flex-wrap:wrap}
.brand{font:700 20px/1 Fraunces,Georgia,serif;color:var(--ink);text-decoration:none}
nav a{margin-left:20px;color:var(--muted);text-decoration:none;font-weight:500}nav a:hover{color:var(--ink)}
.hero{background:var(--accent-soft);padding:72px 0 64px;border-bottom:1px solid var(--line)}
.eyebrow{text-transform:uppercase;letter-spacing:.12em;font-size:13px;font-weight:600;color:var(--accent);margin:0 0 12px}
h1{font:700 clamp(38px,6vw,64px)/1.05 Fraunces,Georgia,serif;margin:0 0 16px;letter-spacing:-.01em}
.lede{font-size:21px;color:var(--muted);max-width:640px;margin:0}
h2{font:700 30px/1.2 Fraunces,Georgia,serif;margin:0 0 20px}
h3{font:600 19px/1.3 Inter,system-ui,sans-serif;margin:0 0 8px}
section{padding:56px 0}section.wrap{padding-top:56px;padding-bottom:56px}
.about p{max-width:720px}
.band{background:#fff;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px}
.card{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:22px}
.card p{margin:0 0 10px;color:var(--muted);font-size:16px}
.price{font-weight:600;color:var(--accent)!important;margin:0!important}
.link-card{display:block;text-decoration:none;color:inherit;background:#fff;border-top:5px solid var(--accent);transition:transform .15s}
.link-card:hover{transform:translateY(-3px)}.more{font-weight:600;color:var(--accent)}
.steps{list-style:none;padding:0;margin:0;display:grid;gap:18px}
.steps li{display:flex;gap:18px;align-items:flex-start}
.step-n{flex:0 0 40px;height:40px;border-radius:50%;background:var(--accent);color:#fff;display:grid;place-items:center;font-weight:600}
.steps p{margin:0;color:var(--muted)}
details{border-bottom:1px solid var(--line);padding:16px 0}
summary{cursor:pointer;font-weight:600;font-size:18px}details p{color:var(--muted);margin:10px 0 0}
.site-foot{background:#1f1d1a;color:#d9d3c8;padding:40px 0}
.brand-foot{font:700 18px/1 Fraunces,Georgia,serif;margin:0 0 10px;color:#fff}
.disclosure{font-size:14px;max-width:680px;margin:0;color:#b9b2a6}
@media (max-width:600px){nav a{margin-left:0;margin-right:16px}.hero{padding:48px 0 40px}.lede{font-size:18px}}
"""

for _slug, _ld in _FACTS["jsonld"].items():
    SHOPS[_slug]["jsonld"] = _ld
os.makedirs(f"{OUT}/assets", exist_ok=True)
open(f"{OUT}/assets/site.css", "w").write(CSS)
open(f"{OUT}/index.html", "w").write(index_page())
for slug, s in SHOPS.items():
    os.makedirs(f"{OUT}/{slug}", exist_ok=True)
    page = shop_page(slug, s)
    visible = page.split("</head>", 1)[1]
    headpart = page.split('<script type="application/ld+json">')[0]
    for w in FORBIDDEN:
        assert w not in visible and w not in headpart, (slug, w)
    open(f"{OUT}/{slug}/index.html", "w").write(page)
urls = [BASE] + [BASE + s + "/" for s in SHOPS]
sm = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
      + "".join(f"  <url><loc>{u}</loc><lastmod>2026-09-26</lastmod></url>\n" for u in urls) + "</urlset>\n")
open(f"{OUT}/sitemap.xml", "w").write(sm)
open(f"{OUT}/.nojekyll", "w").write("")
print("ok", urls)
