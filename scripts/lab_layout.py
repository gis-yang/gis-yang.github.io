"""Shared page layout for the GeoFly Lab site (header, footer, <head>).

Used by the page build scripts so every page has the same header and footer.
`prefix` is "" for top-level pages and "../" for pages inside posts/.
"""

import html

NAV = [
    ("index.html", "Home"),
    ("project.html", "Research"),
    ("publication.html", "Publications"),
    ("facility.html", "Facilities"),
    ("post.html", "News"),
    ("contact.html", "Contact"),
]

FONTS = ("https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700"
         "&family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap")


def head(title, description, prefix="", extra=""):
    t = html.escape(title)
    d = html.escape(description, quote=True)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{t}</title>
    <meta name="description" content="{d}">
    <meta name="author" content="GeoFly Lab">
{extra}    <link rel="icon" type="image/png" href="{prefix}static/picture/geoflylab_logo.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="{FONTS}">
    <link rel="stylesheet" href="{prefix}static/css/lab.css">
</head>
<body>
"""


def header(active, prefix=""):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ""
        items.append(f'                <li><a href="{prefix}{href}"{cur}>{label}</a></li>')
    links = "\n".join(items)
    return f"""<header class="site-header">
    <div class="wrap">
        <a class="brand" href="{prefix}index.html">
            <span class="brand-name">GeoFly Lab</span>
            <span class="brand-sub">Environmental Studies &middot; University of California, Santa Cruz</span>
        </a>
        <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
        <nav class="site-nav" id="site-nav" aria-label="Main">
            <ul>
{links}
            </ul>
        </nav>
    </div>
</header>
"""


def footer(prefix=""):
    return f"""<footer class="site-footer">
    <div class="wrap">
        <div>
            <div class="footer-name">GeoFly Lab</div>
            <p>GIS, remote sensing, and UAV-based mapping for environmental research and education.</p>
        </div>
        <div>
            <h2>Visit</h2>
            <p>Department of Environmental Studies<br>University of California, Santa Cruz<br>1156 High Street<br>Santa Cruz, CA 95064</p>
        </div>
        <div>
            <h2>Explore</h2>
            <ul>
                <li><a href="{prefix}project.html">Research</a></li>
                <li><a href="{prefix}publication.html">Publications</a></li>
                <li><a href="{prefix}facility.html">Facilities</a></li>
                <li><a href="{prefix}post.html">News</a></li>
                <li><a href="{prefix}gallery.html">Photo gallery</a></li>
                <li><a href="{prefix}contact.html">Contact</a></li>
            </ul>
        </div>
    </div>
    <div class="copyright">
        <div class="wrap">&copy; 2026 GeoFly Lab, University of California, Santa Cruz</div>
    </div>
</footer>
<script src="{prefix}static/js/lab.js" defer></script>
"""


def page(title, description, active, main_html, prefix="", extra_head="", extra_body=""):
    return (head(title, description, prefix, extra_head)
            + header(active, prefix)
            + "<main>\n" + main_html.rstrip() + "\n</main>\n"
            + footer(prefix)
            + extra_body
            + "</body>\n</html>\n")


def page_head(title, lede="", crumbs=None, prefix=""):
    """Title block at the top of an inner page. crumbs: list of (href, label)."""
    c = ""
    if crumbs:
        parts = [f'<a href="{prefix}{h}">{html.escape(l)}</a>' for h, l in crumbs]
        c = f'        <p class="crumbs">{" / ".join(parts)}</p>\n'
    l = f'        <p class="lede">{lede}</p>\n' if lede else ""
    return f"""    <div class="page-head">
{c}        <h1>{title}</h1>
{l}    </div>
"""
