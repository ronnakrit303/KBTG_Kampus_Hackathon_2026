from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "Proposal-v3.pdf"

FONT_REGULAR = Path(r"C:\Windows\Fonts\tahoma.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\tahomabd.ttf")

pdfmetrics.registerFont(TTFont("Tahoma", str(FONT_REGULAR)))
pdfmetrics.registerFont(TTFont("Tahoma-Bold", str(FONT_BOLD)))

W, H = A4
INK = "#17211F"
GREEN = "#075B50"
MUTED = "#5F6A68"
RULE = "#B8C5C2"
LIGHT_RULE = "#D8E0DE"


def txt(c, value, x, y, size=8, color=INK, bold=False):
    c.setFont("Tahoma-Bold" if bold else "Tahoma", size)
    c.setFillColor(HexColor(color))
    c.drawString(x, y, value)


def right_txt(c, value, x, y, size=8, color=INK, bold=False):
    c.setFont("Tahoma-Bold" if bold else "Tahoma", size)
    c.setFillColor(HexColor(color))
    c.drawRightString(x, y, value)


def lines(c, values, x, y, size=7.5, leading=12, color=INK, bold=False):
    for index, value in enumerate(values):
        txt(c, value, x, y - index * leading, size=size, color=color, bold=bold)


def rule(c, x1, y, x2, color=RULE, width=0.7):
    c.setStrokeColor(HexColor(color))
    c.setLineWidth(width)
    c.line(x1, y, x2, y)


def section(c, english, thai, x, y, width):
    txt(c, english, x, y, size=10.5, color=GREEN, bold=True)
    if thai:
        offset = pdfmetrics.stringWidth(english, "Tahoma-Bold", 10.5) + 6
        txt(c, thai, x + offset, y + 0.3, size=7.2, color=MUTED)
    rule(c, x, y - 6, x + width, LIGHT_RULE, 0.6)


def flow_box(c, x, y, w, h, number, title, body):
    c.setStrokeColor(HexColor(GREEN))
    c.setLineWidth(1.0)
    c.rect(x, y, w, h, fill=0, stroke=1)
    txt(c, f"{number}. {title}", x + 10, y + h - 20, size=8.8, color=GREEN, bold=True)
    rule(c, x + 10, y + h - 28, x + w - 10, LIGHT_RULE, 0.5)
    lines(c, body, x + 10, y + h - 44, size=6.65, leading=12.2)


def flow_arrow(c, x1, x2, y):
    c.setStrokeColor(HexColor(GREEN))
    c.setFillColor(HexColor(GREEN))
    c.setLineWidth(1.2)
    c.line(x1, y, x2 - 7, y)
    p = c.beginPath()
    p.moveTo(x2 - 7, y + 4)
    p.lineTo(x2, y)
    p.lineTo(x2 - 7, y - 4)
    p.close()
    c.drawPath(p, fill=1, stroke=0)


def build():
    c = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1)
    c.setTitle("K PLUS JobShield — Formal One-page Pitch Proposal V3")
    c.setAuthor("KBTG Kampus Hackathon 2026 Applicant Team")
    c.setSubject("Track 3 — Cyber Security & Digital Trust")

    # Plain white document; the only visual element is the three-step flow.
    c.setFillColor(HexColor("#FFFFFF"))
    c.rect(0, 0, W, H, fill=1, stroke=0)

    margin = 42
    right = W - margin
    content_w = right - margin

    # Formal heading
    c.setFillColor(HexColor(GREEN))
    c.rect(margin, 816, content_w, 4, fill=1, stroke=0)
    txt(c, "K PLUS JobShield", margin, 779, size=24, color="#123B35", bold=True)
    right_txt(c, "TRACK 3 · CYBER SECURITY & DIGITAL TRUST", right, 789, size=7.1, color=GREEN, bold=True)
    txt(c, "สร้างเงินสำรองให้ต่อเนื่อง และเพิ่มช่วงหยุดคิดก่อนจ่ายเงินเพื่อแลกกับงาน", margin, 752, size=11, color=INK, bold=True)
    txt(c, "ชั้นความปลอดภัยบน K-ePocket ที่เชื่อม Protected Reserve กับความเสี่ยงของผู้รับและธุรกรรมก่อนเงินออก", margin, 730, size=7.8, color=MUTED)
    rule(c, margin, 712, right, GREEN, 1.0)

    # Problem Statement and Target Users
    problem_w = 342
    target_x = margin + problem_w + 22
    target_w = right - target_x
    section(c, "Problem Statement", "— ปัญหาที่ต้องแก้", margin, 692, problem_w)
    lines(c, [
        "Fake Recruiter สามารถปลอมเป็นบริษัท แล้วเรียกค่าสมัคร ค่าอบรม ค่าอุปกรณ์",
        "หรือเงินมัดจำก่อนเริ่มงาน ผู้ใช้เป็นผู้ยืนยันการโอนเองภายใต้ Social Engineering",
        "จึงผ่าน Authentication ได้แม้เจตนากำลังถูกชักจูง ขณะที่ 77.3% ของคนไทย",
        "มีเงินออมฉุกเฉินไม่ถึง 6 เดือน [1] เงินก้อนที่สูญเสียจึงอาจกระทบความมั่นคง",
        "ในช่วงเริ่มต้นชีวิตการทำงาน ทั้งนี้ สถิติดังกล่าวเป็นของคนไทยโดยรวม",
        "มิใช่หลักฐานว่า First Jobbers ถูกหลอกมากกว่ากลุ่มอื่น",
    ], margin, 670, size=7.25, leading=13.5)

    section(c, "Target Users", "", target_x, 692, target_w)
    txt(c, "First Jobbers อายุ 22–30 ปี", target_x, 669, size=8.6, color=INK, bold=True)
    lines(c, [
        "ผู้ที่กำลังหางาน เริ่มงาน หรือสร้างฐานะช่วงแรก",
        "และเลือกเปิด JobShield ด้วยตนเอง (Opt-in)",
        "โดยมุ่งปกป้องความเสี่ยงในบริบทช่วงเปลี่ยนผ่าน",
        "ไม่เหมารวมว่าผู้ใช้ขาดความรู้หรือความระมัดระวัง",
    ], target_x, 651, size=7.1, leading=13.2)
    rule(c, margin, 596, right, RULE, 0.8)

    # Proposed Solution — the only diagram on the page
    section(c, "Proposed Solution", "— แนวทางที่เสนอ", margin, 578, content_w)
    txt(c, "K-ePocket ช่วยแยกเงินและตั้งเป้าหมาย [3] ส่วน JobShield เพิ่ม Context-aware Security Policy ณ จังหวะก่อนเงินออก", margin, 557, size=7.35, color=MUTED)

    flow_y, flow_h = 419, 119
    gap = 25
    flow_w = (content_w - gap * 2) / 3
    x1 = margin
    x2 = x1 + flow_w + gap
    x3 = x2 + flow_w + gap

    flow_box(c, x1, flow_y, flow_w, flow_h, "1", "BUILD — สร้างเงินสำรอง", [
        "เลือกหรือสร้าง K-ePocket ‘เงินสำรองตั้งหลัก’",
        "กำหนดเป้าหมายค่าใช้จ่ายจำเป็น 3–6 เดือน",
        "ตั้ง Auto-Allocation ตามจำนวนและวันที่เลือก",
        "โดยผู้ใช้ปรับ พัก หรือยกเลิกได้",
        "Save Point/Benefit เป็น Product Hypothesis",
    ])
    flow_box(c, x2, flow_y, flow_w, flow_h, "2", "DETECT — เชื่อมหลายสัญญาณ", [
        "Protected source + ผู้รับใหม่/บัญชีบุคคล",
        "บริบทจ่ายเพื่อสมัคร/เริ่มงาน + โอนซ้ำ/แบ่งยอด",
        "Destination/Graph Risk + Device/Session signal",
        "Server ประเมินร่วมกัน ไม่ตัดสินจากสัญญาณเดียว",
        "และไม่อ่านข้อความหรืออีเมลอัตโนมัติ",
    ])
    flow_box(c, x3, flow_y, flow_w, flow_h, "3", "INTERVENE — ป้องกันตาม Risk", [
        "Low: ดำเนินรายการตามปกติ",
        "Medium: อธิบายเหตุผลและให้ยืนยันอย่างตั้งใจ",
        "High: พักคำสั่งที่ Server ก่อน Payment Hub",
        "จากนั้น Pause & Verify ผ่านช่องทางบริษัททางการ*",
        "หรือ Cancel & Report ก่อนเงินถูกส่ง",
    ])
    flow_arrow(c, x1 + flow_w, x2, flow_y + flow_h / 2)
    flow_arrow(c, x2 + flow_w, x3, flow_y + flow_h / 2)

    txt(c, "Hero scenario:", margin, 400, size=6.8, color=GREEN, bold=True)
    txt(c, "เงินจาก Protected Reserve + ผู้รับใหม่ + จ่ายเพื่อสมัคร/เริ่มงาน + Destination Risk → High-risk review ก่อนเงินออก", margin + 68, 400, size=6.6, color=INK)
    rule(c, margin, 386, right, RULE, 0.8)

    # Bottom columns
    left_w = 244
    divider_x = margin + left_w + 13
    track_x = divider_x + 18
    track_w = right - track_x

    section(c, "Value Proposition", "— คุณค่าที่ส่งมอบ", margin, 367, left_w)
    txt(c, "สำหรับ First Jobbers", margin, 342, size=8, color=INK, bold=True)
    lines(c, [
        "• ลดภาระการจำออมทุกเดือนและเห็นความคืบหน้า",
        "• ปกป้องเงินที่มีความหมาย ณ จุดตัดสินใจก่อนโอน",
        "• ได้เหตุผลเตือนที่ชัด และยังเข้าถึงเงินฉุกเฉิน",
        "  ที่ถูกต้องได้ตาม Policy",
    ], margin, 325, size=7, leading=12.8)

    txt(c, "สำหรับ K PLUS", margin, 265, size=8, color=INK, bold=True)
    lines(c, [
        "• ต่อยอด K-ePocket และ Fraud controls ที่มีอยู่",
        "• มีโอกาสเพิ่ม Engagement และความต่อเนื่องของ",
        "  เงินฝาก โดยต้องพิสูจน์ Product economics",
        "• ขยับจาก Awareness สู่ Pre-loss intervention",
        "  พร้อม Audit และ Report path ที่ตรวจสอบได้",
    ], margin, 248, size=7, leading=12.8)

    c.setStrokeColor(HexColor(LIGHT_RULE))
    c.setLineWidth(0.7)
    c.line(divider_x, 128, divider_x, 373)

    section(c, "Track Perspective", "— Cyber Security & Digital Trust", track_x, 367, track_w)
    lines(c, [
        "JobShield ใช้ Defense in Depth เพื่อแยก ‘ผู้ใช้ตัวจริง’ ออกจาก",
        "‘เจตนาที่ถูกหลอก’: Mobile request integrity → Multi-signal risk",
        "correlation → Versioned policy → Server-side payment gate →",
        "Incident telemetry ระบบใช้ Risk-based control, Explainability,",
        "Data minimization และ User autonomy โดย Cooling-off พักเฉพาะ",
        "คำสั่งเสี่ยง มิได้ล็อก Pocket หรือเงินทั้งหมดของผู้ใช้",
    ], track_x, 342, size=7.05, leading=13.2)

    txt(c, "MVP and Validation Boundary", track_x, 248, size=8, color=INK, bold=True)
    lines(c, [
        "Prototype ใช้ Deterministic rules, Synthetic transactions และ",
        "Destination-risk flag จำลอง ไม่อ้าง AI/ML หรือ Production integration",
        "ผลที่วัดได้คือ Rule/Test coverage, Warning comprehension,",
        "Pause/Cancel, False positive, Legitimate completion และ Latency",
        "ส่วน Precision/Recall ต้องรอข้อมูลจริงที่มี Ground truth",
    ], track_x, 231, size=6.9, leading=12.8)

    txt(c, "ข้อจำกัด", track_x, 158, size=7.5, color=INK, bold=True)
    lines(c, [
        "ระบบช่วยลดความเสี่ยงแต่ไม่รับประกันว่าจะหยุด Scam ทุกกรณี",
        "Independent Employer Verification, Benefit และระยะ Cooling-off",
        "ต้องผ่าน Product, Risk, Legal, Operations และ Business Approval",
    ], track_x, 142, size=6.7, leading=12)

    # References
    rule(c, margin, 106, right, GREEN, 0.9)
    txt(c, "References", margin, 91, size=7.2, color=GREEN, bold=True)
    txt(c, "[1] ธปท. ผลสำรวจทักษะทางการเงิน ปี 2567   [2] KBank: หลอกรับสมัครงานออนไลน์   [3] K-ePocket", margin, 77, size=5.9, color=INK)
    txt(c, "[4] BIS/BCBS: Digital fraud and banking   [5] ธปท. มาตรการป้องกันภัยการเงิน   ·   Accessed 19 Sep 2026", margin, 64, size=5.9, color=INK)
    txt(c, "หมายเหตุ: ข้อเสนออ้างอิงข้อมูลสาธารณะ ไม่อ้างสิทธิ์เข้าถึงระบบภายใน ข้อมูลลูกค้าจริง หรือโมเดลตรวจจับของ KBank", margin, 46, size=5.7, color=MUTED)

    links = [
        ("https://www.bot.or.th/th/research-and-publications/fl-survey-report.html", (42, 72, 176, 90)),
        ("https://www.kasikornbank.com/th/personal/digital-banking/kbankcyberrisk/pages/jobscam.aspx", (178, 72, 371, 90)),
        ("https://www.kasikornbank.com/th/personal/Digital-banking/Pages/k-epocket.aspx", (373, 72, 470, 90)),
        ("https://www.bis.org/bcbs/publ/d558.pdf", (42, 58, 245, 72)),
        ("https://www.bot.or.th/en/fraud/fraud-measure-development.html", (247, 58, 430, 72)),
    ]
    for url, rect in links:
        c.linkURL(url, rect, relative=0)

    c.showPage()
    c.save()


if __name__ == "__main__":
    build()
    print(OUTPUT)

