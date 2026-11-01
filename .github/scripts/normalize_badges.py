"""Rewrite the Credly badge section of README.md as fixed-width HTML images.

pemtajo/badge-readme writes markdown images whose only size control is the
Credly URL path (size/NNxNN). Credly ignores that path for images stored
without a file extension (the ones ending in /blob), so those badges render at
native size and the grid looks uneven. Markdown images cannot carry a width;
HTML <img> tags can, and GitHub honours them.
"""

import re
import sys
from pathlib import Path

WIDTH = int(sys.argv[1]) if len(sys.argv) > 1 else 110
README = Path("README.md")
START, END = "<!--START_SECTION:badges-->", "<!--END_SECTION:badges-->"
MD_IMAGE_LINK = re.compile(r"\[!\[([^\]]*)\]\(([^)]+)\)\]\(([^)]+)\)")

text = README.read_text(encoding="utf-8")
head, _, rest = text.partition(START)
body, _, tail = rest.partition(END)

# ask Credly for its standard 340px rendition so the fixed-width image is crisp
SIZE_PATH = re.compile(r"/size/\d+x\d+/")
tags = [
    f'<a href="{href}"><img src="{SIZE_PATH.sub("/size/340x340/", src)}" alt="{alt}" '
    f'title="{alt}" width="{WIDTH}" height="{WIDTH}"></a>'
    for alt, src, href in MD_IMAGE_LINK.findall(body)
]
if not tags:  # already converted, or nothing to do
    sys.exit(0)

section = "\n<p>\n" + "\n".join(tags) + "\n</p>\n"
README.write_text(head + START + section + END + tail, encoding="utf-8")
print(f"normalized {len(tags)} badges to {WIDTH}px")
