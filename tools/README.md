# Image tools (used by the scheduled article tasks)

Run with python3 (Playwright + Chromium). All output 1200x675 JPEG featured images unless noted.

- `eyecatch-rentandnest.py OUT CATEGORY_SLUG "EYEBROW" "TITLE" "SUBTITLE" LAYOUT [NUMBER]`
  Category sets color + icon (lighting, walls, small-space-storage, room-ideas). LAYOUT a = text left + icon tile, b = full-color centered, c = color block left (shows NUMBER if given, else the icon).
- `eyecatch-yochibon.py OUT CATEGORY_SLUG "EYEBROW" "TITLE(| = line break)" "SUBTITLE" ICON LAYOUT [BIG]`
  For よちぼん市場. Category colors: rakuten-affiliate (red), us-affiliate (teal), development (navy), anything else orange. ICON: kitchen, storage, ai, bag, chart, code. BIG e.g. "6選" for layout c.
- `pin-rentandnest.py OUT "EYEBROW" "TITLE" "SUBTITLE"` — 1000x1500 Pinterest pin.

Rotate layouts a → b → c by published-post count so neighbouring cards look different.
