#!/usr/bin/env python3
"""Update post.html (All Posts page) from posts/*.html.

This repo uses static HTML posts under ./posts/*.html.
We keep post.html as a static page with a marked block that we overwrite.

Markers in post.html:
  <!-- POSTS_LIST_START -->
  <!-- POSTS_LIST_END -->

No third-party deps.
"""

import glob
import html
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "posts"
POSTS_PAGE = ROOT / "post.html"

START = "<!-- POSTS_LIST_START -->"
END = "<!-- POSTS_LIST_END -->"


def extract_date_from_filename(name: str):
    m = re.search(r"(\d{4}-\d{2}-\d{2})", name)
    return datetime.strptime(m.group(1), "%Y-%m-%d") if m else None


def strip_tags(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s)


def parse_post(html_path: Path):
    date = extract_date_from_filename(html_path.name)
    if not date:
        return None

    txt = html_path.read_text(encoding="utf-8", errors="ignore")

    mtitle = re.search(r"<h1[^>]*>(.*?)</h1>", txt, flags=re.I | re.S)
    title = html.unescape(strip_tags(mtitle.group(1)).strip()) if mtitle else html_path.stem

    mrt = re.search(r"<p[^>]*class=\"reading-time\"[^>]*>.*?</p>", txt, flags=re.I | re.S)
    reading_time = html.unescape(strip_tags(mrt.group(0)).strip()) if mrt else ""

    # First paragraph after reading-time (best-effort)
    paragraphs = re.findall(r"<p[^>]*>(.*?)</p>", txt, flags=re.I | re.S)
    snippet = ""
    for p in paragraphs:
        plain = html.unescape(strip_tags(p)).strip()
        if not plain:
            continue
        if "minute read" in plain.lower():
            continue
        snippet = plain
        break
    # Trim snippet
    words = snippet.split()
    if len(words) > 50:
        snippet = " ".join(words[:50]) + "…"

    # First image inside post: <img src="images/<file>">
    mimg = re.search(r"<img\s+[^>]*src=\"images/([^\"]+)\"", txt, flags=re.I)
    img = mimg.group(1) if mimg else ""

    return {
        "date": date,
        "date_long": date.strftime("%B %d, %Y"),
        "title": title,
        "reading_time": reading_time,
        "snippet": snippet,
        "img": img,
        "url": f"posts/{html_path.name}",
    }


def build_card(p):
    safe_title = html.escape(p["title"])
    safe_snippet = html.escape(p["snippet"])

    img_tag = (
        f"<img src=\"./posts/images/{p['img']}\" class=\"card-img-top\" alt=\"{safe_title}\">"
        if p["img"]
        else f"<img src=\"static/picture/SJSU_logo.png\" class=\"card-img-top\" alt=\"{safe_title}\">"
    )

    rt = f"<p class=\"reading-time small text-muted\">{html.escape(p['reading_time'])}</p>" if p["reading_time"] else ""

    return f"""
            <div class=\"col-lg-8 mb-5\">
                <div class=\"card\">
                
                {img_tag}
                
                <div class=\"card-body\">
                    <h3 class=\"card-title\">
                    <a href=\"{p['url']}\" class=\"text-decoration-none text-dark\">{safe_title}</a>
                    </h3>
                    
                    {rt}
                    
                    <p class=\"card-text\">{safe_snippet}</p>
                    <p class=\"card-subtitle text-muted\">{p['date_long']}</p>
                </div>
                </div>
            </div>
"""


def main():
    posts = []
    for p in glob.glob(str(POSTS_DIR / "*.html")):
        it = parse_post(Path(p))
        if it:
            posts.append(it)

    posts.sort(key=lambda x: x["date"], reverse=True)

    if not POSTS_PAGE.exists():
        raise SystemExit(f"post.html not found at {POSTS_PAGE}")

    page_txt = POSTS_PAGE.read_text(encoding="utf-8", errors="ignore")
    if START not in page_txt or END not in page_txt:
        raise SystemExit(
            "Missing markers in post.html. Add:\n"
            f"  {START}\n  {END}"
        )

    block = "".join(build_card(p) for p in posts)

    new_txt = re.sub(
        re.escape(START) + r"[\s\S]*?" + re.escape(END),
        START + "\n" + block + "            " + END,
        page_txt,
        flags=re.M,
    )

    POSTS_PAGE.write_text(new_txt, encoding="utf-8")
    print(f"✅ Updated {POSTS_PAGE} with {len(posts)} posts")


if __name__ == "__main__":
    main()
