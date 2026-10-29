"""Write the site's three pages from one stylesheet.

Usage: python tools/build.py [out-dir]

Every page inlines the same styles, so the first response paints the
page without another request. Edit the copy and styles here, then run it.
"""

import sys

out = sys.argv[1] if len(sys.argv) > 1 else "."
CSS = '''@font-face{font-family:"Source Serif 4";src:url(/fonts/serif.woff2) format("woff2");font-weight:400;font-display:swap}
@font-face{font-family:"Schibsted Grotesk";src:url(/fonts/sans.woff2) format("woff2");font-weight:400 600;font-display:swap}
@font-face{font-family:Fraunces;src:url(/fonts/italic.woff2) format("woff2");font-weight:300 400;font-style:italic;font-display:swap}
:root{--paper:#fff;--ink:#111;--ink-2:#3a3835;--muted:#5e5b57;--faint:#9a968f;--line:#e4e2de;--accent:#a8336d;--accent-hover:#8c2a5b;--accent-tint:#f6e6ee;--ph:#efedea;--sans:"Schibsted Grotesk",system-ui,-apple-system,"Segoe UI",sans-serif;--serif:"Source Serif 4",Georgia,serif;--italic:Fraunces,Georgia,serif}
@media (prefers-color-scheme:dark){:root{--paper:#141312;--ink:#f1eee9;--ink-2:#d8d4cd;--muted:#a7a29a;--faint:#75706a;--line:#2f2c29;--accent:#e183b3;--accent-hover:#eda3c8;--accent-tint:#3a2130;--ph:#211f1d}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font:400 16px/1.5 var(--sans);-webkit-font-smoothing:antialiased}
::selection{background:var(--accent-tint)}
a{color:var(--accent);text-decoration:none;transition:color 140ms cubic-bezier(.25,.8,.25,1)}
a:hover{color:var(--accent-hover)}
a:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:4px}
.col{width:min(560px,100% - 48px);margin-inline:auto;position:relative}
.wide{width:min(1040px,100% - 48px);margin-inline:auto}
.whoah{margin-top:clamp(96px,13vw,176px);margin-bottom:0;text-align:center;font:italic 300 clamp(72px,11vw,160px)/.95 var(--italic);letter-spacing:-.03em;word-spacing:.06em;font-variant-numeric:lining-nums}
.intro{margin-top:clamp(56px,7vw,96px)}
p{margin:0}
.lede{font:400 19px/1.55 var(--serif);text-wrap:pretty}
.lede+.lede{margin-top:16px}
.next{margin-top:24px;font-size:14px;line-height:1.4;font-weight:600}
.dot{margin:0 6px;color:var(--faint)}
.how a{color:var(--ink-2)}
.how a:hover{color:var(--accent)}
.portrait{display:block;width:112px;height:auto;aspect-ratio:4/5;margin:0 0 32px;object-fit:cover;border-radius:2px;background:var(--ph)}
.shot{margin:16px 0 0}
.photo{display:block;width:100%;height:auto;aspect-ratio:3/2;object-fit:cover;border-radius:2px;background:var(--ph)}
.cap{margin-top:10px;font-size:13px;line-height:1.3;color:var(--muted)}
section.sec{margin-top:clamp(56px,7vw,80px);padding-top:20px;border-top:1px solid var(--line)}
.lab{margin:0 0 16px;font-size:12px;line-height:1.4;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.line{display:flex;justify-content:space-between;align-items:baseline;gap:16px;min-height:44px;padding:10px 0;border-bottom:1px solid var(--line)}
.line span{color:var(--muted)}
cite{font:italic 400 1.02em/1 var(--italic)}
ol.tl{list-style:none;margin:0;padding:0}
.tl li{display:grid;grid-template-columns:72px minmax(0,1fr);column-gap:16px;padding:14px 0 16px;border-bottom:1px solid var(--line)}
.tl li:first-child{padding-top:2px}
.yr{color:var(--muted);font-variant-numeric:tabular-nums;padding-top:2px}
.what{font:400 19px/1.4 var(--serif)}
.how{margin-top:2px;font-size:14px;line-height:1.45;color:var(--muted)}
footer{margin-top:clamp(80px,9vw,112px);padding:24px 0 64px;border-top:1px solid var(--line);display:flex;flex-wrap:wrap;justify-content:space-between;gap:8px 24px;font-size:13px;line-height:1.45;color:var(--muted)}
@media (min-width:1200px){
.lab{position:absolute;left:-168px;top:-1px;width:168px;margin:0;padding-top:24px;border-top:1px solid var(--line)}
.portrait{position:absolute;left:-168px;top:6px;width:128px;margin:0}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}'''

def page(title, desc, body):
    meta = f'<meta name="description" content="{desc}">\n' if desc else ''
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
{meta}<meta name="color-scheme" content="light dark">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Ccircle cx='8' cy='8' r='5' fill='%23a8336d'/%3E%3C/svg%3E">
<link rel="preload" href="/fonts/italic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/serif.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/sans.woff2" as="font" type="font/woff2" crossorigin>
<style>
{CSS}
</style>
</head>
<body>
{body}
</body>
</html>
'''

NOW = '''<main>
<h1 class="wide whoah">Lately</h1>

<section class="col intro">
<img class="portrait" src="/images/portrait-256.webp" srcset="/images/portrait-256.webp 2x, /images/portrait-384.webp 3x" width="128" height="160" alt="Portrait of Kolja von der Twer" decoding="async" fetchpriority="high">
<p class="lede">I am Kolja. I build software that many people depend on. Right now that means the thirty thousand students of the University of Bonn, a flashcard service of my own and a master’s in computer science. I live between Cologne and Bonn.</p>
<p class="next"><a href="/so-far.html">How did I get here? →</a></p>
</section>

<section class="col sec">
<h2 class="lab">Leading</h2>
<p class="lede">The student parliament elected me head of IT for the AStA, the student government of the University of Bonn. I lead a team of five, two full-time staff and three students, and turn what people ask for, and what they need but don’t say, into software. Our minutes tool saves about seven hours of work a month. Now we are rebuilding the semester-ticket refund service, which pays six figures back to students every year.</p>
<p class="lede">I also sit on the advisory board of git.nrw, the shared GitLab of the universities in North Rhine-Westphalia, and speak there for about seven hundred thousand students. Lately we have been talking about how AI should come into it.</p>
</section>

<section class="col sec">
<h2 class="lab">Building</h2>
<p class="lede">AiNKI, because I love learning. I used Anki for years until it grew tedious on an iPhone, and I wasn’t going to pay €30 for the app. So I built my own, and while I was at it, I built more: it schedules every card with FSRS and speaks MCP, so an AI agent can write your cards and quiz you on them. It is written in Rust, self-hosted and open source.</p>
<p class="next"><a href="https://ainki.twer.net">Try AiNKI</a> <span class="dot" aria-hidden="true">·</span> <a href="https://github.com/vdTwer/AiNKI">Read the source</a></p>
</section>

<section class="col sec">
<h2 class="lab">Teaching</h2>
<p class="lede">For three years I have taught programming at the Institute of Computer Science: exercise groups, reviews of more than two hundred student projects in C++ and Python, and five revision courses of up to one hundred students that I started on my own. These days I also teach agentic software engineering, the craft of building software with AI agents. In July I co-led a week-long algorithms workshop for gifted high-school students.</p>
</section>

<section class="col sec">
<h2 class="lab">Studying</h2>
<p class="lede">A master’s in computer science at the University of Bonn, focused on AI and security, especially AI as a supply chain. Alongside it, a bachelor’s in English, because I love the language and its literature.</p>
</section>

<section class="col sec">
<h2 class="lab">Looking for</h2>
<p class="lede">A working-student role in large-scale software deployment and architecture, ideally AI-native, from February 2027. <a href="mailto:kolja@twer.net">Write to me</a>.</p>
</section>

<section class="col sec">
<h2 class="lab">Off the clock</h2>
<p class="lede">Chess, judo and ballroom dancing, with the ADTV gold badge. And the Western canon, slowly.</p>
</section>

<section class="col sec" id="elsewhere">
<h2 class="lab">Elsewhere</h2>
<div class="line"><span>Email</span><a href="mailto:kolja@twer.net">kolja@twer.net</a></div>
<div class="line"><span>GitHub</span><a href="https://github.com/vdTwer">vdTwer</a></div>
<div class="line"><span>LinkedIn</span><a href="https://www.linkedin.com/in/kolja-von-der-twer-57a283377/">kolja-von-der-twer</a></div>
</section>
</main>

<footer class="col">
<span>© 2026 Kolja von der Twer · No cookies, no trackers, no scripts.</span>
<span>Updated October 29, 2026</span>
</footer>'''

UNTIL = '''<main>
<h1 class="wide whoah">So far</h1>

<section class="col intro">
<p class="lede">Each step so far has been a little wider than the last. At sixteen I helped build a fraud-detection pipeline at Generali. At university I taught one exercise group, then chaired my faculty’s student council, then took on IT for the student government of all thirty thousand students. Now I speak for seven hundred thousand students across the state.</p>
<p class="next"><a href="/">Where am I now? →</a></p>
</section>

<section class="col sec">
<h2 class="lab">Timeline</h2>
<ol class="tl" reversed>
<li><span class="yr">2026</span><div><p class="what">Joined the advisory board of git.nrw</p><p class="how">Speaking for about seven hundred thousand students in the shared GitLab of the universities in North Rhine-Westphalia.</p></div></li>
<li><span class="yr"></span><div><p class="what">Elected head of IT, AStA, University of Bonn</p><p class="how">Leading the IT of the student government for more than thirty thousand students, with a team of five. Since March.</p></div></li>
<li><span class="yr"></span><div><p class="what">Cyber Threat Analyst (intern), Deutsche Telekom Security</p><p class="how">Designed and built Argus, a host intrusion detection system for hardware honeypots across several CPU architectures, in Go, plus central alerting for Splunk and Arkime. February to April.</p></div></li>
<li><span class="yr"></span><div><p class="what">B.Sc. Cyber Security, University of Bonn</p><p class="how">Graded 1.0. My thesis tested whether people report their update behavior truthfully, against what they actually did.</p></div></li>
<li><span class="yr">2025</span><div><p class="what">Chaired the computer science student council</p><p class="how">The voice of the faculty’s students, until early 2026.</p>
<figure class="shot">
<img class="photo" src="/images/chair-560.webp" srcset="/images/chair-560.webp 560w, /images/chair-1120.webp 1120w" sizes="(min-width: 608px) 472px, calc(100vw - 136px)" width="472" height="315" alt="Kolja at the lectern of a seminar room, glancing up from a laptop, seen through an open door" loading="lazy" decoding="async">
<figcaption class="cap">One of my last meetings as chair. Bonn, 2025. Taken by David.</figcaption>
</figure></div></li>
<li><span class="yr"></span><div><p class="what">Elected to the student parliament</p><p class="how">University of Bonn. A seat I still hold.</p></div></li>
<li><span class="yr"></span><div><p class="what">Co-authored a paper at SOUPS</p><p class="how"><a href="https://www.usenix.org/conference/soups2025/presentation/ortloff">“Replication: ‘No one can hack my mind’ 10 years later,”</a> on how experts and non-experts stay secure online.</p></div></li>
<li><span class="yr">2023</span><div><p class="what">Started teaching at the Institute of Computer Science</p><p class="how">One exercise group at first. Three years later: more than two hundred project reviews and five revision courses of my own.</p></div></li>
<li><span class="yr">2021</span><div><p class="what">Software developer (intern), Generali Deutschland</p><p class="how">In tenth grade, at sixteen: helped build an AI-native pipeline that flags fraud in submitted invoices.</p></div></li>
</ol>
</section>

<section class="col sec">
<h2 class="lab">Working with</h2>
<p class="lede">Rust and Go for systems, Python and TypeScript for the rest, C++ when I teach. More and more, orchestrating AI agents.</p>
</section>

<section class="col sec">
<h2 class="lab">More</h2>
<p class="lede">A full CV and references from Telekom Security, the Institute of Computer Science and the AStA are yours on request. <a href="mailto:kolja@twer.net">Write to me</a>.</p>
</section>
</main>

<footer class="col">
<span>© 2026 Kolja von der Twer</span>
<span>Updated October 29, 2026</span>
</footer>'''

MISSING = '''<main>
<h1 class="wide whoah">Not here</h1>
<section class="col intro">
<p class="lede">This page does not exist. Try <a href="/">Lately</a> or <a href="/so-far.html">So far</a>.</p>
</section>
</main>'''

for name, args in {
    'index.html': ('Kolja von der Twer · Lately', 'Kolja von der Twer builds software that many people depend on, from the IT of the student government at the University of Bonn to AiNKI, a flashcard service.', NOW),
    'so-far.html': ('Kolja von der Twer · So far', 'How Kolja von der Twer got here: from a fraud-detection pipeline at sixteen to speaking for seven hundred thousand students across North Rhine-Westphalia.', UNTIL),
    '404.html': ('Kolja von der Twer · Not found', '', MISSING),
}.items():
    open(f'{out}/{name}', 'w').write(page(*args))
