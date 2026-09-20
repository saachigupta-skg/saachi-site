from docx import Document
from docx.shared import Pt, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

doc = Document()

# --- Styles ---
style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(11)

def add_hyperlink(paragraph, text, url):
    """Add a hyperlink to a paragraph."""
    part = paragraph.part
    r_id = part.relate_to(url, 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink', is_external=True)
    hyperlink = OxmlElement('w:hyperlink')
    hyperlink.set(qn('r:id'), r_id)
    new_run = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    rStyle = OxmlElement('w:rStyle')
    rStyle.set(qn('w:val'), 'Hyperlink')
    rPr.append(rStyle)
    new_run.append(rPr)
    t = OxmlElement('w:t')
    t.text = text
    new_run.append(t)
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)
    return hyperlink

def h1(text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(22)
    p.paragraph_format.space_after = Pt(4)
    return p

def h2(text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(16)
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    return p

def h3(text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(13)
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(2)
    return p

def meta(text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(0x88, 0x88, 0x88)
    run.italic = True
    p.paragraph_format.space_after = Pt(4)
    return p

def body(text):
    p = doc.add_paragraph(text)
    p.paragraph_format.space_after = Pt(8)
    return p

def link_line(label, url):
    p = doc.add_paragraph()
    p.add_run(f'{label}: ')
    add_hyperlink(p, url, url)
    p.paragraph_format.space_after = Pt(4)
    return p

def separator():
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '4')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), 'DDDDDD')
    pBdr.append(bottom)
    pPr.append(pBdr)
    return p

# =====================
# TITLE & INTRO
# =====================
h1("SheJumps x Ikon Pass: Back to Skiing!")
meta("April 1, 2026")

p = doc.add_paragraph()
p.add_run("Leapfrogging my pals while skiing a blue run at Mt. Bachelor in Bend is the kind of joy, belonging, and fun I aspired to when applying for this program. I wasn't afraid of falling, or tense with anxiety at the steep and icy parts — just enjoying the gorgeous view and getting to spend time with people.")
p.paragraph_format.space_after = Pt(8)

p = doc.add_paragraph()
p.add_run("SheJumps' scholarship included season rentals (through ")
add_hyperlink(p, "Ski Mart Bellevue", "https://www.christysports.com/store-locations/ski-mart-bellevue.html")
p.add_run("), a half-day lesson (I chose ")
add_hyperlink(p, "Crystal Mountain", "https://www.crystalmountainresort.com/plan-your-trip/ski-and-snowboard-lessons/adult-group-lessons")
p.add_run("), and an Ikon Pass. It also — crucially — gave me a community of women who were getting into snow sports, making me feel included in an activity that I am very much a neophyte at.")
p.paragraph_format.space_after = Pt(8)

link_line("TikTok", "https://www.tiktok.com/@s_k_g_8/video/7623974893184388383")

# =====================
# HOW SKIING GOT AWAY
# =====================
h2("How skiing got away from me")

body("I first learned to ski in 2019, shortly after moving to Denver. I was a beginner, enthusiastic, and consistent for the three months of ski season I was there for. I got better — more confident, more technical — each time. Then life got in the way: I moved to Seattle, then Arizona, then back to Seattle, and we had a global pandemic. I found it hard to justify a pass when I was far from mountains and didn't feel like I was \"good enough\" to justify the investment.")

body("In 2024 I moved back to WA and was excited to finally get into skiing consistently. At the end of the summer, a cycling accident put me out for an entire winter. I spent months in PT, rebuilding strength and relearning how to trust my body. By the time I was physically ready to ski again, the psychological barriers had compounded. I didn't own gear. Lift tickets alone could run $200 a day. And I had no community of people at my level — my friends, who I loved doing other activities with, were much better skiers, and I feared feeling pressured to go on terrain beyond my comfort or slowing them down.")

# =====================
# WHY SHEJUMPS
# =====================
h2("Why SheJumps")

body("Growing up, my immigrant family explored museums, not trails. The outdoors — and especially skiing — felt like a different world. I've spent years actively working against that feeling, earning my way into outdoor spaces one trip at a time.")

body("That started to shift in the summer of 2018, when I moved to Denver for a work rotation. I went camping — with the intention of actually enjoying it — and I did. I got into hiking. Something clicked: outdoor spaces could be mine too, if I kept showing up.")

p = doc.add_paragraph()
p.add_run("SheJumps has been a big part of deepening that relationship. The summer before Baker, I joined 13 other adult women for a week off-grid in the Chugach Mountains of Alaska through a ")
add_hyperlink(p, "NOLS", "https://www.nols.edu/")
p.add_run(" course. Even during the least \"fun\" moments — rain, cold, a scary loose-gravel mountain pass — I felt energized by the support of my peers. I didn't track elevation or mileage; I just got to be present, moving toward each day's destination, singing Taylor Swift while bushwhacking up a mountain. It was a needed reminder that doing hard things can be exhilarating, terrifying, and fun all at once.")
p.paragraph_format.space_after = Pt(8)

p = doc.add_paragraph()
p.add_run("Around that same time, I got ")
add_hyperlink(p, "Wilderness First Aid certified with SheJumps and the Appalachian Mountain Club", "https://www.shejumps.org/wfa")
p.add_run(", alongside other BIPOC women — a beautiful fall weekend in New England learning how to recreate more responsibly. I'm most proud of the times I've led people's first camping, backpacking, hiking, and snowshoe experiences, and WFA gave me more confidence to do that well.")
p.paragraph_format.space_after = Pt(8)

p = doc.add_paragraph()
p.add_run("Then in July 2024, I climbed Mt. Baker (Koma Kulshan) as part of a ")
add_hyperlink(p, "SheJumps fundraising climb", "https://www.shejumps.org/fundraising-climbs")
p.add_run(" — eight women, six months of training, my first ever mountaineering experience, and over $20K raised collectively. I'd never really considered myself \"athletic,\" and declaring a goal like that publicly was uncomfortable. But working toward something hard in the company of other women, with their honesty and encouragement, was transformative. The guides from Alpine Ascents International set us up beautifully. The summit was everything.")
p.paragraph_format.space_after = Pt(8)

body("All of that is the container SheJumps builds. The Ikon Pass scholarship was one more expression of it — a space where I could be a beginner on skis without apology. Access isn't just about cost. It's also about community and representation.")

# =====================
# WHAT THE SEASON GAVE ME
# =====================
h2("What the season gave me")

body("Access to gear and lift tickets meant I could actually get on the mountain — at Snoqualmie and Crystal Mountain here in Washington. Lessons gave me structure. But the biggest thing was permission: to go slowly, to fall, to be exactly where I was in my progression without feeling like I was holding anyone back.")

body("I also got the chance to meet Guy Lawrence, the GM of The Summit at Snoqualmie — a conversation that opened up a whole other lens on the sport, from water rights and snowmaking to the operational complexity of running a seasonal business. It was the outdoors meeting the intellectual curiosity I usually reserve for work, and I loved it.")

# =====================
# THE SKI LOG
# =====================
h2("The Ski Log")
body("Every day on the mountain this season, documented.")

separator()
h3("Session 1 — First ski of 2026: Snoqualmie")
meta("Snoqualmie Pass, WA · with Borde")
body("First turns of the season with my college friend Borde. We lapped a green run, got our legs under us, and I remembered that skiing is actually fun.")
link_line("Strava", "https://www.strava.com/activities/17166278301")
link_line("TikTok", "https://www.tiktok.com/@s_k_g_8/video/7596511980777639199")

separator()
h3("Session 2 — Working on technique: with Owen")
meta("Snoqualmie Pass, WA · with Owen")
body("Parallel turning, leaning forward, hockey stops. Owen is a patient teacher and these are the drills I needed to start skiing with control instead of just survival mode.")
link_line("Strava", "https://www.strava.com/activities/17166278301")

separator()
h3("Session 3 — Valentine's Day: East Coast")
meta("February 14, 2026 · visiting family")
body("Flew east to see family and somehow ended up skiing on Valentine's Day — which turned out to be a perfect way to spend it. Got confident with blue terrain and made some fun videos along the way.")
link_line("Strava", "https://www.strava.com/activities/17399318706")
link_line("TikTok", "https://www.tiktok.com/@s_k_g_8/video/7607111014873566495")

separator()
h3("Session 4 — SheJumps lesson at Crystal Mountain: with Athena")
meta("Crystal Mountain, WA · first time at Crystal")
body("Used my SheJumps lesson credit for a 1:1 with Athena at Crystal. We worked on parallel turns, side slipping, and pushed into some spicier blue terrain. My first time ever at Crystal Mountain — and what a mountain to debut on.")
link_line("Strava", "https://www.strava.com/activities/17511874830")

separator()
h3("Session 5 — Mt. Bachelor with friends")
meta("Mt. Bachelor, OR")
body("Conditions meant we couldn't ski the three days we'd planned, but I kept up with my friends on blues — and that was the whole point. My goal coming into this season was to be able to say yes to trips like this without hesitation, and I did. Great chairlift conversations, beautiful mountain. Knew when I was done for the day and got off the mountain — learning as an adult means knowing your limit.")
link_line("Strava (run 1)", "https://www.strava.com/activities/17737203288")
link_line("Strava (run 2)", "https://www.strava.com/activities/17737186444")
link_line("TikTok (drive to Bend)", "https://www.tiktok.com/@s_k_g_8/video/7618825820856995102")

separator()
h3("Session 6 — Edge Outdoors: skiing with women of color")
meta("Crystal Mountain, WA · with Tori")
body("Joined an Edge Outdoors class designed for women of color — exactly the kind of space I'd been looking for. Tori, a freeride coach at Crystal, led us through parallel turns and navigating slush. So much fun being in a lesson where representation was the starting point, not the exception.")
link_line("Strava", "https://www.strava.com/activities/17796600431")

separator()
h3("Session 7 — Season closer: Whistler")
meta("Whistler, BC · with friends")
body("Bummed I couldn't ski to my full potential, but loved exploring a new mountain with good company. A solid way to close out the season — more about the people than the turns.")
link_line("Strava", "https://www.strava.com/activities/17893697516")

# =====================
# WHAT'S NEXT
# =====================
h2("What's next")

body("This season changed my trajectory. I'm not just trying to ski comfortably with friends anymore — I'm thinking about ski touring. Eventually, I want to descend Mt. Shasta. That goal felt abstract before this winter. Now it feels like a matter of time and reps.")

body("More than the access, SheJumps gave me momentum and belonging — two things that turn a one-season experiment into a lifelong pursuit.")

# =====================
# CTA
# =====================
h2("Support SheJumps")
p = doc.add_paragraph()
p.add_run("SheJumps creates access to the outdoors for women and girls through free and low-cost programming — 200+ events a year, over half of them free or donation-based. If this resonated with you, consider supporting their work: ")
add_hyperlink(p, "shejumps.org", "https://www.shejumps.org/")

# Save
output_path = r"C:\Users\saach\OneDrive\projects\saachi-site\SheJumps-Ikon-Pass.docx"
doc.save(output_path)
print(f"Saved to {output_path}")
