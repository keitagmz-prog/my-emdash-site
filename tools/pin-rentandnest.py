import sys,html
from playwright.sync_api import sync_playwright
o,ey,ti,su=sys.argv[1:5];E=html.escape;A="#c8794a"
h=f"""<body style="margin:0;width:1000px;height:1500px;background:#f4efe7;font-family:Inter;box-sizing:border-box;padding:110px 80px;color:#1f1d1a;display:flex;flex-direction:column">
<div style="font-family:'DejaVu Sans Mono';letter-spacing:6px;font-size:30px;color:{A};text-transform:uppercase">{E(ey)}</div>
<div style="font-size:124px;font-weight:800;line-height:1.02;letter-spacing:-3px;margin-top:48px">{E(ti)}</div>
<div style="width:140px;height:10px;background:{A};margin:64px 0 56px;border-radius:5px"></div>
<div style="font-size:54px;line-height:1.3;color:#4a4540;font-weight:500">{E(su)}</div>
<div style="flex:1"></div>
<div style="background:#1f1d1a;color:#f4efe7;border-radius:999px;padding:30px 48px;font-size:38px;font-weight:700;align-self:flex-start">Read the guide &rarr;</div>
<div style="display:flex;justify-content:space-between;margin-top:80px;font-size:32px;font-weight:700"><span>Rent &amp; Nest</span><span style="font-weight:500;color:#6b645c;font-size:28px">No drilling. No lost deposit.</span></div></body>"""
with sync_playwright() as p:
 b=p.chromium.launch();g=b.new_page(viewport={"width":1000,"height":1500});g.set_content(h);g.wait_for_timeout(300);g.screenshot(path=o,type="jpeg",quality=90);b.close()
