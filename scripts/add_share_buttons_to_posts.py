#!/usr/bin/env python3
"""Add share buttons (X/LinkedIn/Facebook) to all existing posts/*.html.

Idempotent: if a file already contains class="share-buttons", it is skipped.
Inserts the block right before the "Updated:" line container.

No third-party dependencies.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "posts"

SHARE_BLOCK = r'''
                    <!-- Share buttons -->
                    <div class="share-buttons mt-4">
                        <p class="text-muted mb-2">Share:</p>
                        <a class="btn btn-slider trans-btn rounded-pill mr-2" id="share-twitter" target="_blank" rel="noopener noreferrer">X (Twitter)</a>
                        <a class="btn btn-slider trans-btn rounded-pill mr-2" id="share-linkedin" target="_blank" rel="noopener noreferrer">LinkedIn</a>
                        <a class="btn btn-slider trans-btn rounded-pill" id="share-facebook" target="_blank" rel="noopener noreferrer">Facebook</a>
                    </div>

                    <!-- Share links (no login; opens native share pages) -->
                    <script>
                        (function () {
                            function setShareLinks() {
                                var url = encodeURIComponent(window.location.href);
                                var title = encodeURIComponent(document.title);
                                var tw = document.getElementById('share-twitter');
                                var li = document.getElementById('share-linkedin');
                                var fb = document.getElementById('share-facebook');
                                if (tw) tw.href = 'https://twitter.com/intent/tweet?url=' + url + '&text=' + title;
                                if (li) li.href = 'https://www.linkedin.com/sharing/share-offsite/?url=' + url;
                                if (fb) fb.href = 'https://www.facebook.com/sharer/sharer.php?u=' + url;
                            }
                            if (document.readyState === 'loading') {
                                document.addEventListener('DOMContentLoaded', setShareLinks);
                            } else {
                                setShareLinks();
                            }
                        })();
                    </script>
'''


def main():
    files = sorted(POSTS_DIR.glob('*.html'))
    changed = 0

    for f in files:
        txt = f.read_text(encoding='utf-8', errors='ignore')
        if 'class="share-buttons' in txt:
            continue

        # Insert before the Updated date container.
        # Match: <div class="container text-right mb-4">\n        <p class="updated">Updated:
        m = re.search(r'\n\s*<div class="container text-right mb-4">\s*\n\s*<p class="updated">Updated:', txt)
        if not m:
            # fallback: just before </div> closing of content column (first occurrence)
            continue

        insert_at = m.start()
        new_txt = txt[:insert_at] + "\n" + SHARE_BLOCK + txt[insert_at:]
        f.write_text(new_txt, encoding='utf-8')
        changed += 1

    print(f"✅ Updated {changed} posts")


if __name__ == '__main__':
    main()
