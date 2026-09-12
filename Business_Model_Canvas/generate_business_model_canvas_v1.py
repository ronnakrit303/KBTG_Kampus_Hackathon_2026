from pathlib import Path

import fitz
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A3, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "Business_Model_Canvas-V1.pdf"
PREVIEW = ROOT / "Business_Model_Canvas-V1-preview.png"
PREVIEW_PAGE2 = ROOT / "Business_Model_Canvas-V1-preview-page2.png"

FONT_REGULAR = Path(r"C:\Windows\Fonts\tahoma.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\tahomabd.ttf")

pdfmetrics.registerFont(TTFont("Tahoma", str(FONT_REGULAR)))
pdfmetrics.registerFont(TTFont("Tahoma-Bold", str(FONT_BOLD)))

W, H = landscape(A3)


def rounded_box(c, x, y, w, h, fill, stroke, radius=10, line_width=0.8):
    c.setFillColor(HexColor(fill))
    c.setStrokeColor(HexColor(stroke))
    c.setLineWidth(line_width)
    c.roundRect(x, y, w, h, radius, fill=1, stroke=1)


def label(c, value, x, y, size, color, bold=False):
    c.setFont("Tahoma-Bold" if bold else "Tahoma", size)
    c.setFillColor(HexColor(color))
    c.drawString(x, y, value)


def section(c, x, y, w, h, number, english, thai, body, fill, stroke, accent):
    rounded_box(c, x, y, w, h, fill, stroke)

    c.setFillColor(HexColor(accent))
    c.roundRect(x, y + h - 42, w, 42, 10, fill=1, stroke=0)
    c.rect(x, y + h - 42, w, 12, fill=1, stroke=0)

    c.setFillColor(HexColor("#FFFFFF"))
    c.circle(x + 18, y + h - 20, 10, fill=1, stroke=0)
    label(c, str(number), x + 15.1, y + h - 23.3, 7.7, accent, True)
    label(c, english, x + 34, y + h - 18, 11.2, "#FFFFFF", True)
    label(c, thai, x + 34, y + h - 32, 7.2, "#EAF7F3")

    style = ParagraphStyle(
        name=f"body-{number}",
        fontName="Tahoma",
        fontSize=8.45,
        leading=12.15,
        textColor=HexColor("#1E2B29"),
        spaceAfter=0,
        wordWrap="CJK",
    )
    paragraph = Paragraph(body, style)
    available_w = w - 22
    available_h = h - 58
    pw, ph = paragraph.wrap(available_w, available_h)
    paragraph.drawOn(c, x + 11, y + h - 52 - ph)


def paragraph(c, body, x, y, w, h, size=8.4, leading=12.0, color="#1E2B29"):
    style = ParagraphStyle(
        name=f"paragraph-{x}-{y}",
        fontName="Tahoma",
        fontSize=size,
        leading=leading,
        textColor=HexColor(color),
        wordWrap="CJK",
    )
    item = Paragraph(body, style)
    pw, ph = item.wrap(w, h)
    item.drawOn(c, x, y + h - ph)
    return ph


def arrow(c, x1, y1, x2, y2, color="#7D918B", width=1.5):
    c.setStrokeColor(HexColor(color))
    c.setFillColor(HexColor(color))
    c.setLineWidth(width)
    c.line(x1, y1, x2 - 7, y2)
    c.line(x2 - 7, y2, x2 - 13, y2 + 4)
    c.line(x2 - 7, y2, x2 - 13, y2 - 4)


def page_two(c):
    c.setFillColor(HexColor("#F4FAF8"))
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Executive header
    rounded_box(c, 24, 744, W - 48, 72, "#073B3A", "#073B3A", radius=14, line_width=0)
    label(c, "ที่มาของแนวคิด เหตุผลทางธุรกิจ และ Operating Model", 46, 783, 19, "#FFFFFF", True)
    label(c, "EXECUTIVE RATIONALE · จากปัญหาจริง → กลไกที่เลือก → คุณค่าที่คาดหวัง → สิ่งที่ต้องพิสูจน์", 47, 760, 8.5, "#8AF0D1", True)
    rounded_box(c, W - 225, 759, 150, 27, "#124F48", "#6EAA9E", radius=8, line_width=0.6)
    label(c, "JOBSHIELD · MOBILE-FIRST", W - 210, 768, 7.2, "#FFFFFF", True)

    # Origin and rationale row
    top_y, top_h, gap = 548, 181, 8
    box_w = (W - 48 - gap * 3) / 4
    top_x = [24 + i * (box_w + gap) for i in range(4)]

    origin = (
        "<b>ข้อเท็จจริงที่เป็นจุดเริ่มต้น [S1]</b><br/>"
        "KBank อธิบายรูปแบบประกาศงานปลอมที่แอบอ้างองค์กร และเรียกให้โอนเงินประกันก่อนเริ่มงาน ค่าสมัคร หรือค่าดำเนินการ รวมถึงการหลอกให้โอนซ้ำ<br/><br/>"
        "<b>เหตุผลที่เลือกปัญหานี้</b><br/>"
        "ความเสียหายเกิดในจังหวะก่อนเงินออก ซึ่ง K PLUS มีโอกาสช่วยให้ผู้ใช้หยุด ตรวจสอบ และยกเลิกได้ก่อนการชำระเสร็จสมบูรณ์"
    )
    section(c, top_x[0], top_y, box_w, top_h, 1, "Problem Origin", "ปัญหาเริ่มจากอะไร", origin,
            "#FFF4F2", "#E7BBB4", "#B55547")

    user_moment = (
        "<b>บริบทของ First Jobbers</b><br/>"
        "ระหว่างหางาน ผู้ใช้ต้องรับการติดต่อจากผู้ส่งที่ยังไม่คุ้นเคย และอาจถูกเร่งให้จ่ายเงินเพื่อแลกกับโอกาสงาน ขณะที่เงินสำรองมีความสำคัญต่อการตั้งหลัก<br/><br/>"
        "<b>Claim Boundary</b><br/>"
        "ยังไม่มีหลักฐานว่ากลุ่มอายุ 22–30 ถูกหลอกมากกว่าทุกกลุ่ม จึงใช้คำว่า “ช่วงเปลี่ยนผ่านมีบริบทเสี่ยงเฉพาะ” ไม่กล่าวว่าผู้ใช้ประมาทหรือหลงเชื่อง่าย"
    )
    section(c, top_x[1], top_y, box_w, top_h, 2, "User Moment", "เหตุใดจึงเป็น First Jobbers", user_moment,
            "#FFF9ED", "#E7D3A6", "#A9741F")

    strategic_gap = (
        "<b>สิ่งที่มีอยู่แล้ว [S2]</b><br/>"
        "K-ePocket ช่วยแบ่งเงิน ตั้งเป้าหมาย และทำธุรกรรมจาก Pocket ได้ ขณะที่ K PLUS มีการยืนยันตัวตนและ Fraud Controls เป็นพื้นฐาน<br/><br/>"
        "<b>ช่องว่างที่ JobShield เสนอ</b><br/>"
        "ไม่สร้าง Pocket หรือ Warning ใหม่เพียงอย่างเดียว แต่เชื่อมแหล่งเงินที่ถูกปกป้อง + ผู้รับ + บริบทธุรกรรม + Destination Risk เพื่อเลือก Intervention ก่อนเงินออก"
    )
    section(c, top_x[2], top_y, box_w, top_h, 3, "Strategic Gap", "ต่างจากระบบเดิมอย่างไร", strategic_gap,
            "#F4F8FD", "#BDD0E5", "#3E74A8")

    business_rationale = (
        "<b>ตรรกะการสร้างคุณค่า</b><br/>"
        "Auto-Allocation ลดภาระการจำออม [S4] → ผู้ใช้อาจสร้างเงินสำรองต่อเนื่องขึ้น → Context-aware Protection ช่วยลดโอกาสเสียเงินก้อนสำคัญ → Trust และ Engagement อาจเพิ่มขึ้น<br/><br/>"
        "<b>คุณค่าต่อธนาคารแบบมีเงื่อนไข</b><br/>"
        "ยอดคงเหลืออาจเสถียรขึ้น และเคส Scam ที่ต้องจัดการอาจลดลง แต่ต้องพิสูจน์ Cost of Funds, Benefit Cost, False Positive และ Unit Economics ก่อน"
    )
    section(c, top_x[3], top_y, box_w, top_h, 4, "Business Rationale", "เหตุใดธนาคารควรพิจารณา", business_rationale,
            "#F3FAF7", "#B8DCCF", "#247E69")

    # Operating model
    rounded_box(c, 24, 371, W - 48, 160, "#FFFFFF", "#B7C9C2", radius=10, line_width=0.8)
    label(c, "OPERATING MODEL — ผู้ใช้ได้รับคุณค่าอย่างไรตั้งแต่เริ่มออมจนถึงก่อนเงินออก", 40, 510, 10.8, "#174C3C", True)
    flow_x0, flow_y, flow_w, flow_h, flow_gap = 42, 397, 174, 91, 20
    flow_items = [
        ("1 · OPT-IN", "เปิด JobShield<br/>รับทราบข้อมูลที่ใช้<br/>เลือก/สร้าง K-ePocket", "#E9F7EF", "#49A987"),
        ("2 · SET GOAL", "ระบุค่าใช้จ่ายจำเป็น<br/>ตั้งเป้า 3/6 เดือน<br/>กำหนดยอดเริ่มต้น", "#E9F7EF", "#49A987"),
        ("3 · BUILD", "ตั้ง Scheduled<br/>Auto-Allocation<br/>ปรับ/พัก/ปิดได้", "#EAF3FF", "#5B93D3"),
        ("4 · MOTIVATE", "ติดตาม Save Point<br/>Benefit Progress<br/>มี Grace/Pause Rule", "#FFF8E6", "#D6A033"),
        ("5 · ASSESS", "ส่ง Transfer Intent<br/>Server เชื่อมหลายสัญญาณ<br/>ยังไม่ส่ง Payment Hub", "#F4EEFF", "#8A63C7"),
        ("6 · PROTECT", "Low: ปกติ/Nudge<br/>Medium: Explain<br/>High: Cooling-off<br/>Verify/Cancel/Report", "#FFEDE8", "#E66C57"),
    ]
    for index, (title, body, fill, stroke) in enumerate(flow_items):
        x = flow_x0 + index * (flow_w + flow_gap)
        rounded_box(c, x, flow_y, flow_w, flow_h, fill, stroke, radius=8, line_width=1.1)
        label(c, title, x + 10, flow_y + flow_h - 20, 8.3, stroke, True)
        paragraph(c, body, x + 10, flow_y + 9, flow_w - 20, flow_h - 35, size=7.65, leading=10.6)
        if index < len(flow_items) - 1:
            arrow(c, x + flow_w + 3, flow_y + flow_h / 2, x + flow_w + flow_gap - 3, flow_y + flow_h / 2)

    # Technical architecture
    rounded_box(c, 24, 211, W - 48, 145, "#F8FAFA", "#B7C9C2", radius=10, line_width=0.8)
    label(c, "TECHNICAL OPERATING MODEL — Mobile แสดงผล; Server ประเมิน ควบคุมเวลา และปล่อยรายการ", 40, 335, 10.8, "#174C3C", True)
    tech_x0, tech_y, tech_w, tech_h, tech_gap = 42, 237, 202, 72, 31
    tech_items = [
        ("K PLUS MOBILE", "UI, Consent, Warning,<br/>Countdown, User Decision<br/><b>ไม่เก็บ Risk Formula</b>", "#E9F7EF", "#49A987"),
        ("MOBILE BFF / API*", "HTTPS · REST/JSON · OpenAPI<br/>Session Validation<br/>transactionId + Idempotency", "#EAF3FF", "#5B93D3"),
        ("BANK-SIDE SIGNALS*", "K-ePocket Context<br/>Payee/Velocity/Device<br/>Destination/Graph Risk Flag", "#F4EEFF", "#8A63C7"),
        ("POLICY & STATE*", "Rule-based Correlation<br/>Low/Medium/High<br/>PENDING_COOLING_OFF", "#FFF8E6", "#D6A033"),
        ("PAYMENT HUB / CORE", "รับคำสั่งเมื่อ Policy อนุญาต<br/>Server time เป็นแหล่งจริง<br/>มี Audit/Observability", "#FFEDE8", "#E66C57"),
    ]
    for index, (title, body, fill, stroke) in enumerate(tech_items):
        x = tech_x0 + index * (tech_w + tech_gap)
        rounded_box(c, x, tech_y, tech_w, tech_h, fill, stroke, radius=8, line_width=1.1)
        label(c, title, x + 10, tech_y + tech_h - 18, 8, stroke, True)
        paragraph(c, body, x + 10, tech_y + 7, tech_w - 20, tech_h - 29, size=7.25, leading=9.5)
        if index < len(tech_items) - 1:
            arrow(c, x + tech_w + 3, tech_y + tech_h / 2, x + tech_w + tech_gap - 4, tech_y + tech_h / 2, color="#647973")
    label(c, "* Proposed Internal Integration — MVP ใช้ Synthetic API/Data; ไม่เข้าถึง Production K PLUS หรือข้อมูลลูกค้าจริง", 43, 218, 7.2, "#8A3022", True)

    # Safeguards and decision gates
    bottom_y, bottom_h, bottom_gap = 78, 118, 8
    bottom_w = (W - 48 - bottom_gap) / 2
    rounded_box(c, 24, bottom_y, bottom_w, bottom_h, "#FFF7F5", "#E2B4AC", radius=9, line_width=0.8)
    label(c, "SECURITY, PRIVACY & OPERATIONAL SAFEGUARDS", 39, 174, 9.4, "#8A3022", True)
    safeguards = (
        "• <b>Defense in Depth:</b> Protected source + payee/context + bank risk flag; ไม่ตัดสินจากสัญญาณเดียว<br/>"
        "• <b>Server Authority:</b> Risk Level, Countdown และ Release อยู่ฝั่ง Server; Mobile ปลอมเวลาเพื่อข้ามไม่ได้<br/>"
        "• <b>Anti-evasion:</b> รวมยอดโอนซ้ำ/แบ่งยอด, Purpose ลด Risk ไม่ได้ และใช้ Idempotency ป้องกันกดซ้ำ<br/>"
        "• <b>False Positive:</b> บัญชีตนเอง/Verified Biller เสี่ยงต่ำยังใช้ได้; Medium ไม่ Cooling-off อัตโนมัติ<br/>"
        "• <b>Privacy by Design:</b> ไม่อ่านข้อความ/อีเมล/Resume; เก็บเฉพาะ Indicators/Audit ที่จำเป็นและกำหนด Retention"
    )
    paragraph(c, safeguards, 39, 88, bottom_w - 30, 73, size=7.55, leading=10.4)

    rounded_box(c, 24 + bottom_w + bottom_gap, bottom_y, bottom_w, bottom_h, "#F3FAF7", "#B8DCCF", radius=9, line_width=0.8)
    right_x = 24 + bottom_w + bottom_gap
    label(c, "SUCCESS METRICS & DECISION GATES", right_x + 15, 174, 9.4, "#174C3C", True)
    metrics = (
        "<b>Security:</b> Pause/Cancel ใน Scam scenarios, False-positive rate, bypass detection และเวลาถึง Report<br/>"
        "<b>UX:</b> เข้าใจเหตุผลเตือน, งานปกติสำเร็จ, เวลาเพิ่ม, warning-dismissal/alert fatigue และ perceived trust<br/>"
        "<b>Savings:</b> Auto-Allocation success, retained balance, progress recovery หลังถอน และ Benefit abuse<br/>"
        "<b>Business:</b> Opt-in/active use, retention/engagement, stable-balance hypothesis และ cost avoidance เทียบต้นทุนรวม<br/>"
        "<b>Gate:</b> Pilot จริง 1 คน → ผู้เข้าร่วม 5–8 คน → Internal API/Risk/Legal/Business validation; <font color='#9A352B'><b>ปัจจุบัน 0 sessions conducted</b></font>"
    )
    paragraph(c, metrics, right_x + 15, 88, bottom_w - 30, 73, size=7.55, leading=10.4)

    # Clickable source strip
    rounded_box(c, 24, 20, W - 48, 44, "#EEF2F1", "#CAD5D2", radius=7, line_width=0.7)
    label(c, "ที่มาและหลักฐาน (เข้าถึง 10 ก.ย. 2569):", 38, 47, 7.2, "#174C3C", True)
    sources = [
        ("[S1] KBank: หลอกรับสมัครงานออนไลน์", "https://www.kasikornbank.com/th/personal/digital-banking/kbankcyberrisk/pages/jobscam.aspx"),
        ("[S2] K-ePocket", "https://www.kasikornbank.com/th/personal/Digital-banking/Pages/k-epocket.aspx"),
        ("[S3] ธปท.: รับมือภัยการเงินดิจิทัล", "https://www.bot.or.th/th/research-and-publications/articles-and-publications/bot-magazine-issues/phrasiam-69-1/synergy-against-fraud.html"),
        ("[S4] AEA: Saving by Default", "https://www.aeaweb.org/articles?id=10.1257/app.20160547"),
        ("[S5] KBTG: Backend &amp; Integration", "https://medium.com/kbtg-life/kbtg-%E0%B9%83%E0%B8%8A%E0%B9%89-golang-%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%AD%E0%B8%B0%E0%B9%84%E0%B8%A3-%E0%B8%A1%E0%B8%B5%E0%B8%AD%E0%B8%B0%E0%B9%84%E0%B8%A3%E0%B8%84%E0%B8%A7%E0%B8%A3%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B8%9A%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%83%E0%B8%8A%E0%B9%89-go-%E0%B9%83%E0%B8%99-kbtg-dca091939147"),
    ]
    sx = 38
    for source_label, source_url in sources:
        display_label = source_label.replace("&amp;", "&")
        text_width = pdfmetrics.stringWidth(display_label, "Tahoma", 6.6)
        label(c, display_label, sx, 30, 6.6, "#176C61")
        c.linkURL(source_url, (sx, 27, sx + text_width, 41), relative=0, thickness=0)
        sx += text_width + 20



def build_pdf():
    c = canvas.Canvas(str(OUTPUT), pagesize=(W, H), pageCompression=1)
    c.setTitle("K PLUS JobShield — Business Model Canvas V1")
    c.setAuthor("KBTG Kampus Hackathon 2026 Applicant Team")
    c.setSubject("Track 3 — Cyber Security & Digital Trust")

    c.setFillColor(HexColor("#F4FAF8"))
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Header
    rounded_box(c, 24, 744, W - 48, 72, "#073B3A", "#073B3A", radius=14, line_width=0)
    c.setFillColor(HexColor("#12594F"))
    c.circle(W - 58, 798, 45, fill=1, stroke=0)
    c.setFillColor(HexColor("#1A7565"))
    c.circle(W - 32, 818, 28, fill=1, stroke=0)
    label(c, "K PLUS JobShield", 46, 783, 23, "#FFFFFF", True)
    label(c, "BUSINESS MODEL CANVAS · V1", 47, 762, 8.5, "#8AF0D1", True)
    label(c, "Protected Reserve + Auto-Allocation + Risk-based Protection", 306, 782, 11, "#DDF7EF", True)
    label(c, "Mobile Security Module ภายใน K PLUS · Target: First Jobbers อายุ 22–30", 306, 762, 8.4, "#B9DCD4")
    rounded_box(c, W - 221, 759, 145, 27, "#124F48", "#6EAA9E", radius=8, line_width=0.6)
    label(c, "TRACK 3 · CYBER SECURITY", W - 207, 768, 7.2, "#FFFFFF", True)

    gap = 8
    main_y, main_h = 278, 452
    x0 = 24
    widths = [190, 210, 300, 210, 200]
    xs = [x0]
    for width in widths[:-1]:
        xs.append(xs[-1] + width + gap)

    key_partners = (
        "<b>พันธมิตรภายในธนาคาร</b><br/>"
        "• KBank Product/Business Owner และทีม K PLUS<br/>"
        "• ทีม K-ePocket และระบบบัญชีเงินฝาก<br/>"
        "• KBTG Mobile, Backend, Architecture และ Platform<br/>"
        "• KBTGSec, Fraud Analytics, Fraud Operations และ Incident Response<br/>"
        "• Risk, Legal, Compliance, PDPA และ Internal Audit<br/>"
        "• ทีม K Point/CRM และ Finance สำหรับประเมินต้นทุน Benefit<br/><br/>"
        "<b>พันธมิตรภายนอกที่อาจต้องใช้</b><br/>"
        "• หน่วยงาน/แหล่งข้อมูลบริษัททางการ สำหรับ Independent Verification ในอนาคต<br/>"
        "• Partner merchants สำหรับคูปองหรือสิทธิประโยชน์ ภายใต้ Business Approval<br/>"
        "• ผู้เชี่ยวชาญหรือผู้รับจ้างด้าน Usability, Accessibility และ Security Testing ภายใต้การกำกับของธนาคาร<br/><br/>"
        "<font color='#7A4A20'><b>ขอบเขต:</b> ไม่ถือว่าพันธมิตรเหล่านี้ตกลงเข้าร่วมแล้ว</font>"
    )
    section(c, xs[0], main_y, widths[0], main_h, 1, "Key Partners", "พันธมิตรหลัก", key_partners,
            "#F3FAF7", "#B8DCCF", "#247E69")

    activities_h = 222
    key_activities = (
        "• ออกแบบ JobShield เป็น Mobile Module ภายใน K PLUS<br/>"
        "• เชื่อมการตั้งเงินสำรองและ Scheduled Auto-Allocation กับ K-ePocket<br/>"
        "• บริหาร Save Point, Benefit Tier และ Grace/Pause Rule<br/>"
        "• ทำ Transaction Risk Correlation จากหลายสัญญาณ<br/>"
        "• Orchestrate Warning, Cooling-off, Verify และ Cancel/Report ก่อนส่งเงิน<br/>"
        "• ทดสอบ Threat Model, False Positive, Alert Fatigue, Evasion และ Emergency Use<br/>"
        "• ติดตามประสิทธิภาพ Policy และปรับกติกาอย่างมี Audit Trail"
    )
    section(c, xs[1], main_y + activities_h + gap, widths[1], activities_h, 2, "Key Activities",
            "กิจกรรมหลัก", key_activities, "#F4F8FD", "#BDD0E5", "#3E74A8")

    key_resources = (
        "<b>Technology</b><br/>"
        "• K PLUS Mobile, Mobile BFF และ K-ePocket<br/>"
        "• Transaction Context, Bank-side Risk Flag และ Device/Session Signal<br/>"
        "• Policy Engine, Pending Instruction State, Notification และ Audit Log<br/><br/>"
        "<b>People &amp; Governance</b><br/>"
        "• Mobile/Backend Engineer, Cyber Security, Fraud, UX Research, Data, Risk และ Legal<br/><br/>"
        "<b>MVP Resources</b><br/>"
        "• Figma, Flutter, FastAPI, OpenAPI, NetworkX และ Synthetic Data"
    )
    section(c, xs[1], main_y, widths[1], activities_h, 3, "Key Resources", "ทรัพยากรหลัก",
            key_resources, "#F4F8FD", "#BDD0E5", "#3E74A8")

    value_proposition = (
        "<b><font color='#174C3C'>สำหรับ First Jobbers</font></b><br/>"
        "• เริ่มสร้างเงินสำรองได้ง่าย และลดโอกาสลืมออมด้วย Auto-Allocation ที่ผู้ใช้กำหนดเอง<br/>"
        "• เห็นเป้าหมาย จำนวนเดือนที่เงินสำรองครอบคลุม Save Point และความคืบหน้าของ Benefit<br/>"
        "• ปกป้องเงินสำรอง ณ จังหวะที่กำลังถูก Social Engineering ให้โอนไปยังปลายทางเสี่ยง<br/>"
        "• ได้คำเตือนที่บอกเหตุผล ไม่ใช่ข้อความทั่วไป และมี Cooling-off สำหรับรายการ High Risk<br/>"
        "• ยังควบคุมเงินของตนเองได้ ระบบไม่ล็อกทั้งบัญชีหรือทั้ง Pocket<br/>"
        "• ไม่อ่านข้อความ อีเมล Resume หรือเสียงสนทนาโดยอัตโนมัติ<br/><br/>"
        "<b><font color='#174C3C'>สำหรับ K PLUS/KBank</font></b><br/>"
        "• เพิ่มความแตกต่างจาก Pocket หรือ Fraud Warning ทั่วไป ด้วย Context-aware Security Policy<br/>"
        "• สนับสนุน Trust, Engagement และ Retention ภายใน K PLUS<br/>"
        "• การออมต่อเนื่องอาจช่วยให้ยอดเงินฝากคงเหลือมีเสถียรภาพขึ้น<br/>"
        "• การแทรกแซงก่อนเงินออกอาจลดภาระ Fraud Report, Support และ Dispute Operations<br/><br/>"
        "<font color='#7A4A20'><b>Core Differentiation:</b> ระบบรู้ว่าเงินก้อนใดกำลังเสี่ยง เชื่อมบริบทผู้รับและธุรกรรม แล้วเพิ่มการป้องกันให้เหมาะกับระดับความเสี่ยง</font>"
    )
    section(c, xs[2], main_y, widths[2], main_h, 4, "Value Proposition", "คุณค่าที่ส่งมอบ",
            value_proposition, "#EEF9F5", "#9FD3C2", "#126D59")

    customer_relationships = (
        "• Opt-in onboarding พร้อมอธิบายข้อมูลที่ใช้และขอ Consent อย่างชัดเจน<br/>"
        "• Self-service: ตั้งค่า ปรับ พัก หรือปิด Auto-Allocation ได้<br/>"
        "• Dashboard แสดงเป้าหมาย Save Point และ Benefit Progress<br/>"
        "• มาสคอตใช้เฉพาะ Savings Nudge ที่กดข้ามได้<br/>"
        "• Scam Warning ใช้ภาษาจริงจัง ไม่ตำหนิ และแสดงเหตุผล 2–3 ข้อ<br/>"
        "• มี Cancel/Report, สถานะรายการ Pending และช่องทางช่วยเหลือ<br/>"
        "• รับ Feedback/Complaint เพื่อลด False Positive และเพิ่ม Accessibility"
    )
    section(c, xs[3], main_y + activities_h + gap, widths[3], activities_h, 5,
            "Customer Relationships", "ความสัมพันธ์กับลูกค้า", customer_relationships,
            "#FFF9ED", "#E7D3A6", "#A9741F")

    channels = (
        "<b>Awareness</b> — Banner/Recommendation ใน K PLUS และบริบท K-ePocket<br/>"
        "<b>Evaluation</b> — หน้าอธิบาย ตัวอย่างความเสี่ยง และเครื่องคำนวณเป้าหมายเงินสำรอง<br/>"
        "<b>Activation</b> — เปิด JobShield และเลือก/สร้าง K-ePocket ใน Mobile Flow<br/>"
        "<b>Delivery</b> — Dashboard, Transfer Flow, Contextual Warning และ Push/In-app Notification<br/>"
        "<b>After-use</b> — Cooling-off Status, Cancel/Report Status, FAQ และช่องทางช่วยเหลือ<br/><br/>"
        "<font color='#7A4A20'><b>หลักการ:</b> ส่งมอบผ่าน K PLUS เดิม ไม่สร้างแอปใหม่</font>"
    )
    section(c, xs[3], main_y, widths[3], activities_h, 6, "Channels", "ช่องทางส่งมอบ",
            channels, "#FFF9ED", "#E7D3A6", "#A9741F")

    customer_segments = (
        "<b>Primary Users</b><br/>"
        "• First Jobbers อายุ 22–30 ที่ใช้ K PLUS<br/>"
        "• ผู้ที่เพิ่งเริ่มสร้างเงินสำรอง มีรายได้จำกัด/ไม่สม่ำเสมอ หรือยังไม่มีวินัยออมต่อเนื่อง<br/>"
        "• ผู้ที่กำลังสมัครงาน รอเริ่มงาน หรือเริ่มมีรายได้แล้ว โดยไม่ต้องแบ่ง Stage<br/><br/>"
        "<b>Hero Security Scenario</b><br/>"
        "• ผู้ใช้ถูก Fake Recruiter ขอค่าสมัคร ค่าอบรม ค่าอุปกรณ์ หรือเงินมัดจำ<br/>"
        "• พยายามนำ Protected Reserve ไปโอนให้บัญชีบุคคลใหม่<br/><br/>"
        "<b>Needs &amp; Expectations</b><br/>"
        "• ออมง่าย ใช้ไม่กี่ขั้นตอน และหยุด/ปรับได้<br/>"
        "• เงินฉุกเฉินเข้าถึงได้เมื่อจำเป็นจริง<br/>"
        "• คำเตือนเข้าใจง่าย ไม่เตือนพร่ำเพรื่อ และไม่ละเมิดความเป็นส่วนตัว<br/><br/>"
        "<b>Internal Decision Makers</b><br/>"
        "• KBank Product, Risk, Security, Legal, Compliance และ Operations เป็นผู้อนุมัติ ไม่ใช่ผู้ใช้ปลายทาง"
    )
    section(c, xs[4], main_y, widths[4], main_h, 7, "Customer Segments", "กลุ่มลูกค้า",
            customer_segments, "#FFF4F2", "#E7BBB4", "#B55547")

    bottom_y, bottom_h = 94, 172
    bottom_w = (W - 48 - gap) / 2
    cost_structure = (
        "<b>Fixed/Initial Costs:</b> Product &amp; UX Research • Mobile/BFF/Backend Integration • Security Architecture • Policy Engine • K-ePocket/Fraud System Adapter • Legal/PDPA/Compliance • Penetration, Performance, UAT และ Accessibility Testing<br/><br/>"
        "<b>Variable/Ongoing Costs:</b> Compute/API/Notification • Monitoring และ Rule Tuning • Fraud/Customer Support • K Point/Partner Benefit • External Verification Data • Incident Response และ Audit<br/><br/>"
        "<b>Cost Risks:</b> False Positive เพิ่มภาระ Support • Benefit ถูกใช้งานผิดวัตถุประสงค์ • Integration กับ Legacy/Payment Flow ซับซ้อน • ต้นทุน Incentive สูงกว่าคุณค่าที่เกิดขึ้น"
    )
    section(c, 24, bottom_y, bottom_w, bottom_h, 8, "Cost Structure", "โครงสร้างต้นทุน",
            cost_structure, "#FFF4F2", "#E7BBB4", "#B55547")

    revenue_streams = (
        "<b>Direct Revenue:</b> MVP ไม่คิดค่าบริการผู้ใช้ และไม่ขายข้อมูลส่วนบุคคล<br/><br/>"
        "<b>Potential Business Value:</b> Engagement/Retention ใน K PLUS • ยอดเงินฝากคงเหลือที่อาจมีเสถียรภาพขึ้น • โอกาสใช้ผลิตภัณฑ์การเงินที่เหมาะสมในอนาคตโดยมี Consent • Cost Avoidance จาก Scam Support, Investigation และ Dispute ที่อาจลดลง • Partner-funded Benefits ภายใต้ข้อตกลงและ Business Approval<br/><br/>"
        "<font color='#7A4A20'><b>Claim Boundary:</b> เงินฝากเพิ่มไม่ได้แปลว่าเงินทุกบาทถูกปล่อยกู้หรือกลายเป็นกำไรโดยตรง ต้องพิสูจน์ Unit Economics ต้นทุน Benefit ความเสี่ยง และผลกระทบด้านกฎเกณฑ์ก่อน</font>"
    )
    section(c, 24 + bottom_w + gap, bottom_y, bottom_w, bottom_h, 9,
            "Revenue Streams / Business Value", "รายได้และคุณค่าทางธุรกิจ", revenue_streams,
            "#F3FAF7", "#B8DCCF", "#247E69")

    # Validation footer
    rounded_box(c, 24, 24, W - 48, 56, "#EEF2F1", "#CAD5D2", radius=8, line_width=0.7)
    label(c, "ASSUMPTIONS TO VALIDATE", 38, 59, 7.2, "#174C3C", True)
    footer_style = ParagraphStyle(
        name="footer",
        fontName="Tahoma",
        fontSize=7.35,
        leading=10.6,
        textColor=HexColor("#394744"),
        wordWrap="CJK",
    )
    footer = Paragraph(
        "H1 Auto-Allocation เพิ่มการออมสำเร็จต่อเนื่อง • H2 Contextual Warning เพิ่ม Pause/Cancel ใน Scam โดยไม่ขวางรายการปกติมากเกินไป • "
        "H3 Save Point/Benefit สร้างแรงจูงใจโดยไม่บังคับให้ฝืนออม • H4 คุณค่าจาก Trust, Engagement, Stable Balance และ Cost Avoidance คุ้มกว่าต้นทุนรวม "
        "<font color='#9A352B'><b>สถานะหลักฐานผู้ใช้: 0 sessions conducted — ห้ามถือผลลัพธ์ใน Canvas นี้เป็นผลทดสอบจริง</b></font>",
        footer_style,
    )
    fw, fh = footer.wrap(W - 300, 34)
    footer.drawOn(c, 38, 31)
    rounded_box(c, W - 250, 38, 205, 27, "#FFFFFF", "#9FB5AF", radius=7, line_width=0.6)
    label(c, "CURRENT STATUS · BUSINESS HYPOTHESES", W - 236, 47, 6.9, "#49645C", True)

    c.showPage()
    page_two(c)
    c.showPage()
    c.save()


def render_preview():
    document = fitz.open(OUTPUT)
    if document.page_count != 2:
        raise RuntimeError(f"Expected 2 pages, got {document.page_count}")
    preview_targets = (PREVIEW, PREVIEW_PAGE2)
    for page_index, preview_target in enumerate(preview_targets):
        page = document[page_index]
        pixmap = page.get_pixmap(matrix=fitz.Matrix(1.6, 1.6), alpha=False)
        pixmap.save(preview_target)
    document.close()


if __name__ == "__main__":
    build_pdf()
    render_preview()
    print(OUTPUT)
    print(PREVIEW)
    print(PREVIEW_PAGE2)
