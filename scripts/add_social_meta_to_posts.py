#!/usr/bin/env python3
"""Add Open Graph/Twitter meta tags to posts/*.html.

Goal: when sharing a post on LinkedIn/X/Facebook, the preview auto-pulls:
- title
- description
- first image in the post

LinkedIn does NOT reliably support pre-filling post body text or forcing an
uploaded image via share URL. The best practice is correct og:* meta tags.

This script is idempotent.
No third-party deps.
"""

import glob
import html
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "posts"
SITE_BASE = "https://geofly.io"  # used for absolute og:url and og:image


def strip_tags(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s)


def upsert_meta(head: str, property_name: str, content: str, attr: str = "property") -> str:
    """Insert or replace a meta tag in the <head> block."""
    content = content.replace('"', '&quot;')
    patt = re.compile(rf"<meta\s+{attr}=\"{re.escape(property_name)}\"\s+content=\"[^\"]*\"\s*/?>", re.I)
    tag = f'<meta {attr}="{property_name}" content="{content}">' 
    if patt.search(head):
        return patt.sub(tag, head)

    # Insert before </head>
    return head.replace("</head>", f"    {tag}\n</head>")


def main():
    files = sorted(glob.glob(str(POSTS_DIR / "*.html")))
    changed = 0
    for fp in files:
        p = Path(fp)
        txt = p.read_text(encoding="utf-8", errors="ignore")

        mhead = re.search(r"<head>[\s\S]*?</head>", txt, flags=re.I)
        if not mhead:
            continue

        head_block = mhead.group(0)

        # Title from first <h1>
        mtitle = re.search(r"<h1[^>]*>(.*?)</h1>", txt, flags=re.I | re.S)
        title = html.unescape(strip_tags(mtitle.group(1)).strip()) if mtitle else p.stem

        # Description from existing meta description if present, else first paragraph
        mdesc = re.search(r"<meta\s+name=\"description\"\s+content=\"([^\"]*)\"", head_block, flags=re.I)
        if mdesc:
            desc = mdesc.group(1).strip()
        else:
            paras = re.findall(r"<p[^>]*>(.*?)</p>", txt, flags=re.I | re.S)
            desc = ""
            for para in paras:
                plain = html.unescape(strip_tags(para)).strip()
                if not plain:
                    continue
                if "minute read" in plain.lower():
                    continue
                desc = plain
                break
            desc = desc[:180]

        # First image src="images/<file>"
        mimg = re.search(r"<img\s+[^>]*src=\"images/([^\"]+)\"", txt, flags=re.I)
        og_img = f"{SITE_BASE}/posts/images/{mimg.group(1)}" if mimg else f"{SITE_BASE}/static/picture/SJSU_logo.png"

        # URL
        og_url = f"{SITE_BASE}/posts/{p.name.replace(' ', '%20')}"

        new_head = head_block
        new_head = upsert_meta(new_head, "og:type", "article")
        new_head = upsert_meta(new_head, "og:site_name", "GeoFly Lab")
        new_head = upsert_meta(new_head, "og:title", title)
        new_head = upsert_meta(new_head, "og:description", desc)
        new_head = upsert_meta(new_head, "og:url", og_url)
        new_head = upsert_meta(new_head, "og:image", og_img)

        new_head = upsert_meta(new_head, "twitter:card", "summary_large_image", attr="name")
        new_head = upsert_meta(new_head, "twitter:title", title, attr="name")
        new_head = upsert_meta(new_head, "twitter:description", desc, attr="name")
        new_head = upsert_meta(new_head, "twitter:image", og_img, attr="name")

        if new_head != head_block:
            txt2 = txt.replace(head_block, new_head)
            p.write_text(txt2, encoding="utf-8")
            changed += 1

    print(f"✅ Updated OG/Twitter meta for {changed} posts")


if __name__ == "__main__":
    main()
