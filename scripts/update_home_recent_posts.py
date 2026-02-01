#!/usr/bin/env python3
"""Update index.html Recent posts carousel with latest N posts.

This repo uses static HTML posts under ./posts/*.html. We generate the
"Recent posts" section on the homepage by scanning posts, sorting by date
(from filename), and rewriting a marked block in index.html.

Markers in index.html:
  <!-- RECENT_POSTS_START -->
  <!-- RECENT_POSTS_END -->

No third-party deps.
"""

import glob
import html
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
POSTS_DIR = ROOT / "posts"

START = "<!-- RECENT_POSTS_START -->"
END = "<!-- RECENT_POSTS_END -->"


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

    # First image inside the post body: <img src="images/<file>">
    mimg = re.search(r"<img\s+[^>]*src=\"images/([^\"]+)\"", txt, flags=re.I)
    img = mimg.group(1) if mimg else ""

    return {
        "date": date,
        "date_mmddyyyy": date.strftime("%m-%d %Y"),
        "date_long": date.strftime("%B %d, %Y"),
        "title": title,
        "img": img,
        "url": f"posts/{html_path.name}",
    }


def build_item(p):
    # Homepage uses mixed image paths; prefer posts/images for consistency.
    img_tag = (
        f"\n                            <img src=\"posts/images/{p['img']}\" alt=\"blog img\">\n"
        if p["img"]
        else "\n                            <img src=\"static/picture/SJSU_logo.png\" alt=\"blog img\">\n"
    )

    safe_title = html.escape(p["title"])

    return f"""                    <div class=\"item blog-item wow fadeInUp\" data-wow-duration=\".8s\">
                        <div class=\"blog-img\">
                            <a href=\"{p['url']}\">{img_tag}                            </a>
                        </div>

                        <div class=\"blog-text text-center\">
                            <div class=\"date d-flex justify-content-center text-black\">
                                <p class=\"mb-0 text-black sub-heading mr-3\">{p['date_mmddyyyy']}</p>
                                <p class=\"text-black sub-heading\">{safe_title}</p>
                            </div>
                            <div class=\"info-blog mb-3\">
                                <a href=\"{p['url']}\" class=\"text-decoration-none\"><h4 class=\"text-black mb-3 mt-2 blog-heading\">{safe_title}</h4></a>
                            </div>
                            <a href=\"{p['url']}\" class=\"btn btn-slider trans-btn rounded-pill\">Read More</a>
                        </div>
                     </div>
"""


def main(limit=5):
    posts = []
    for p in glob.glob(str(POSTS_DIR / "*.html")):
        it = parse_post(Path(p))
        if it:
            posts.append(it)

    posts.sort(key=lambda x: x["date"], reverse=True)
    posts = posts[:limit]

    if not INDEX.exists():
        raise SystemExit(f"index.html not found at {INDEX}")

    index_txt = INDEX.read_text(encoding="utf-8", errors="ignore")
    if START not in index_txt or END not in index_txt:
        raise SystemExit(
            "Missing markers in index.html. Add:\n"
            f"  {START}\n  {END}"
        )

    block = "".join(build_item(p) for p in posts)

    new_txt = re.sub(
        re.escape(START) + r"[\s\S]*?" + re.escape(END),
        START + "\n" + block + "                    " + END,
        index_txt,
        flags=re.M,
    )

    INDEX.write_text(new_txt, encoding="utf-8")
    print(f"✅ Updated {INDEX} with {len(posts)} recent posts")


if __name__ == "__main__":
    main()
