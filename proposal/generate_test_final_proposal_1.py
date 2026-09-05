from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "Test_ Final-Proposal-1.pdf"

FONT_REGULAR = Path(r"C:\Windows\Fonts\tahoma.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\tahomabd.ttf")

pdfmetrics.registerFont(TTFont("Tahoma", str(FONT_REGULAR)))
pdfmetrics.registerFont(TTFont("Tahoma-Bold", str(FONT_BOLD)))

W, H = A4


def box(c, x, y, w, h, fill, stroke="#D7E5E2", radius=10, line=0.8):
    c.setFillColor(HexColor(fill))
    c.setStrokeColor(HexColor(stroke))
    c.setLineWidth(line)
    c.roundRect(x, y, w, h, radius, fill=1, stroke=1)


def text(c, value, x, y, size=9, color="#17212B", bold=False):
    c.setFont("Tahoma-Bold" if bold else "Tahoma", size)
    c.setFillColor(HexColor(color))
    c.drawString(x, y, value)


def lines(c, values, x, y, size=8.4, leading=12.2, color="#17212B", bold=False):
    for index, value in enumerate(values):
        text(c, value, x, y - index * leading, size=size, color=color, bold=bold)


def section_title(c, english, thai, x, y):
    text(c, english, x, y, size=10.2, color="#075B50", bold=True)
    if thai:
        offset = pdfmetrics.stringWidth(english, "Tahoma-Bold", 10.2) + 5
        text(c, thai, x + offset, y + 0.3, size=7.5, color="#60706D")


def pill(c, label, x, y, w, fill, color):
    c.setFillColor(HexColor(fill))
    c.setStrokeColor(HexColor(fill))
    c.roundRect(x, y, w, 15, 7, fill=1, stroke=0)
    c.setFont("Tahoma-Bold", 6.2)
    c.setFillColor(HexColor(color))
    tw = pdfmetrics.stringWidth(label, "Tahoma-Bold", 6.2)
    c.drawString(x + (w - tw) / 2, y + 4.4, label)


def build():
    c = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1)
    c.setTitle("K PLUS JobShield — One-page Pitch Proposal")
    c.setAuthor("KBTG Kampus Hackathon 2026 Applicant Team")
    c.setSubject("Track 3 — Cyber Security & Digital Trust")

    # Page background and subtle top-right decoration.
    c.setFillColor(HexColor("#F5FBF9"))
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(HexColor("#DDF3EC"))
    c.circle(W - 20, H - 20, 80, fill=1, stroke=0)

    # Header.
    x0, content_w = 28, W - 56
    box(c, x0, 686, content_w, 128, "#073B3A", stroke="#073B3A", radius=16, line=0)
    c.setFillColor(HexColor("#145E53"))
    c.circle(W - 36, 791, 64, fill=1, stroke=0)
    c.setFillColor(HexColor("#1C7868"))
    c.circle(W - 24, 808, 39, fill=1, stroke=0)
    text(c, "KBTG KAMPUS HACKATHON 2026 · ONE-PAGE PITCH", 50, 792, 7.5, "#8AF0D1", True)
    text(c, "K PLUS JobShield", 50, 756, 26, "#FFFFFF", True)
    text(c, "ปกป้อง “เงินสำรองก่อนเงินเดือนแรก” ก่อนถูกบริษัทปลอม", 50, 727, 12.2, "#FFFFFF", True)
    text(c, "ขอให้จ่ายเงินเพื่อแลกกับงาน", 50, 708, 12.2, "#FFFFFF", True)
    text(c, "Career Mode ที่เชื่อมบริบทการหางาน แหล่งเงิน และความเสี่ยงธุรกรรม เพื่อแทรกแซงก่อนเงินออก", 50, 691.5, 7.3, "#CDEBE5")
    box(c, 444, 787, 112, 20, "#124F48", stroke="#77BDB0", radius=9, line=0.6)
    text(c, "TRACK 3 · CYBER SECURITY", 454, 793, 6.4, "#E8FFF8", True)

    # Problem and target row.
    problem_x, problem_y, problem_w, top_h = x0, 566, 350, 108
    target_x, target_w = problem_x + problem_w + 10, content_w - problem_w - 10
    box(c, problem_x, problem_y, problem_w, top_h, "#FFFFFF")
    section_title(c, "Problem Statement", "— ปัญหาที่ต้องแก้", problem_x + 14, 654)
    lines(c, [
        "มิจฉาชีพอาจปลอมเป็นบริษัทหรือ recruiter แล้วเรียกค่าสมัคร ค่าอบรม",
        "ค่าอุปกรณ์ หรือเงินมัดจำก่อนเริ่มงาน ผู้สมัครเป็นผู้ยืนยันการโอนเอง",
        "จึงผ่าน authentication ได้แม้กำลังถูก social engineering ขณะที่คำเตือน",
        "ทั่วไปไม่รู้ว่าเงินก้อนนี้จำเป็นต่อการใช้ชีวิตก่อนเงินเดือนแรก",
    ], problem_x + 14, 635, size=8.25, leading=14)

    box(c, target_x, problem_y, target_w, top_h, "#EAF8F4", stroke="#B9E6D8")
    section_title(c, "Target Users", "", target_x + 13, 654)
    box(c, target_x + 13, 618, 138, 23, "#C9F3E5", stroke="#C9F3E5", radius=7, line=0)
    text(c, "First Jobbers 22–30", target_x + 22, 625, 10, "#075B50", True)
    lines(c, [
        "ผู้ที่กำลังสมัครงาน รอเริ่มงาน หรือรอเงินเดือนแรก",
        "และเลือกเปิด Career Mode ด้วยตนเอง โดยไม่เหมารวม",
        "ว่ากลุ่มนี้ประมาทหรือถูกหลอกมากกว่าคนอื่น",
    ], target_x + 13, 604, size=7.35, leading=13)

    # Proposed solution.
    sol_y, sol_h = 315, 239
    box(c, x0, sol_y, content_w, sol_h, "#FFFFFF", stroke="#B9DEDA", radius=12, line=0.9)
    section_title(c, "Proposed Solution", "— 3 ขั้นตอนก่อนเงินออก", x0 + 14, 534)

    flow_y, flow_h, gap = 421, 94, 9
    step_w = (content_w - 28 - gap * 2) / 3
    step_xs = [x0 + 14, x0 + 14 + step_w + gap, x0 + 14 + (step_w + gap) * 2]
    fills = ["#F0F8F5", "#F5F1FB", "#FFF5E9"]
    strokes = ["#CDE5DD", "#DED2F1", "#F0D4AE"]
    badge = ["#0B6D5D", "#7252A3", "#C66A21"]
    titles = ["Prepare", "Detect", "Intervene"]
    for i, sx in enumerate(step_xs):
        box(c, sx, flow_y, step_w, flow_h, fills[i], stroke=strokes[i], radius=9, line=0.7)
        c.setFillColor(HexColor(badge[i]))
        c.circle(sx + 14, flow_y + flow_h - 16, 9, fill=1, stroke=0)
        text(c, str(i + 1), sx + 11.2, flow_y + flow_h - 19.2, 7.2, "#FFFFFF", True)
        text(c, titles[i], sx + 28, flow_y + flow_h - 20, 9.4, "#17212B", True)

    lines(c, [
        "เปิด Career Mode แบบ opt-in",
        "กำหนดช่วงเวลา แล้วแบ่ง K-ePocket เป็น",
        "Job Search Budget สำหรับค่าใช้จ่ายหางาน",
        "และ เงินสำรองก่อนเงินเดือนแรก สำหรับ",
        "ค่าเช่า อาหาร เดินทาง และเหตุจำเป็น",
    ], step_xs[0] + 10, 480, size=6.85, leading=11.4)

    lines(c, [
        "ก่อนโอน รวมแหล่งเงิน ผู้รับใหม่ ยอดและ",
        "การโอนสะสม บริบทการจ่ายเพื่อเริ่มงาน",
        "และ destination risk จากระบบธนาคาร",
        "คำตอบของผู้ใช้เป็นเพียงหนึ่งสัญญาณ",
        "ไม่อ่านข้อความหรืออีเมลอัตโนมัติ",
    ], step_xs[1] + 10, 480, size=6.85, leading=11.4)

    lines(c, [
        "ปรับ friction ตามความเสี่ยงพร้อมเหตุผล",
        "ที่สังเกตได้ หาก High Risk จะพักเป็น",
        "Pending Instruction ใน Cooling-off",
        "ก่อนส่งเข้าสู่ PromptPay แล้วให้ผู้ใช้",
        "ตรวจสอบ ยกเลิก หรือรายงาน",
    ], step_xs[2] + 10, 480, size=6.85, leading=11.4)
    pill(c, "LOW · NORMAL", step_xs[2] + 9, 428, 49, "#DFF5E4", "#176734")
    pill(c, "MED · EXPLAIN", step_xs[2] + 61, 428, 53, "#FFE8BD", "#8A5110")
    pill(c, "HIGH · PAUSE", step_xs[2] + 117, 428, 50, "#FFD7D2", "#9B3027")

    # Warning example.
    box(c, x0 + 14, 358, 324, 52, "#FFF3F0", stroke="#E6A298", radius=8, line=0.6)
    c.setFillColor(HexColor("#DF5A48"))
    c.roundRect(x0 + 14, 358, 5, 52, 2.5, fill=1, stroke=0)
    text(c, "ตัวอย่างคำเตือน: พักรายการนี้และตรวจสอบก่อน", x0 + 28, 393, 7.8, "#992F25", True)
    lines(c, [
        "ผู้รับใหม่ · ใช้เงินสำรองก่อนเงินเดือนแรก · จ่ายเพื่อเริ่มงาน",
        "คำสั่งยังไม่ถูกส่งเข้าสู่ระบบโอน และผู้ใช้ยังยกเลิกได้",
    ], x0 + 28, 378, size=6.65, leading=11.2, color="#6A3B35")
    box(c, x0 + 349, 382, 92, 23, "#0B6D5D", stroke="#0B6D5D", radius=6, line=0)
    text(c, "Pause & Verify", x0 + 365, 389.5, 7.1, "#FFFFFF", True)
    box(c, x0 + 349, 357, 92, 20, "#FFFFFF", stroke="#DC7A6E", radius=6, line=0.6)
    text(c, "Cancel / Report", x0 + 365, 363.5, 6.8, "#9B3027", True)

    # Three integration strip.
    int_y, int_h = 324, 25
    int_w = (content_w - 28 - 12) / 3
    int_xs = [x0 + 14, x0 + 14 + int_w + 6, x0 + 14 + (int_w + 6) * 2]
    int_titles = ["1 · K-ePocket", "2 · Transaction + Fraud Risk", "3 · Security & Fraud Response"]
    int_subs = ["บริบทและวัตถุประสงค์ของเงิน", "ผู้รับ · ยอด · รูปแบบ · destination risk", "Warning · Verification · Cooling-off · Report"]
    for ix, title_value, sub_value in zip(int_xs, int_titles, int_subs):
        box(c, ix, int_y, int_w, int_h, "#EEF5F4", stroke="#D5E2E0", radius=6, line=0.45)
        text(c, title_value, ix + 7, int_y + 14, 6.3, "#075B50", True)
        text(c, sub_value, ix + 7, int_y + 5.2, 5.7, "#4D5D5A")

    # Bottom row: value and track perspective.
    bottom_y, bottom_h, bottom_gap = 95, 208, 10
    value_w = 252
    track_x = x0 + value_w + bottom_gap
    track_w = content_w - value_w - bottom_gap
    box(c, x0, bottom_y, value_w, bottom_h, "#FFFFFF")
    section_title(c, "Value Proposition", "", x0 + 14, 283)
    box(c, x0 + 14, 196, value_w - 28, 70, "#EEF8F5", stroke="#D5E7E1", radius=8, line=0.5)
    text(c, "FOR FIRST JOBBERS", x0 + 25, 250, 6.8, "#075B50", True)
    lines(c, [
        "ปกป้องเงินสำคัญ ณ จุดตัดสินใจก่อนโอน",
        "อธิบายว่าเตือนเพราะอะไร และยังมีทางผ่าน",
        "สำหรับธุรกรรมถูกต้องหรือเหตุฉุกเฉิน เช่น",
        "บัญชีตนเองหรือ verified biller",
    ], x0 + 25, 234, size=7.2, leading=12)
    box(c, x0 + 14, 112, value_w - 28, 72, "#EEF3FA", stroke="#D4DEEB", radius=8, line=0.5)
    text(c, "FOR K PLUS", x0 + 25, 168, 6.8, "#315B83", True)
    lines(c, [
        "ต่อยอด K-ePocket และ fraud controls ที่มีอยู่",
        "เป็น security journey เฉพาะช่วงหางาน",
        "ขยับจาก awareness สู่ pre-loss intervention",
        "และเสริม Digital Trust โดยไม่อ่านข้อความส่วนตัว",
    ], x0 + 25, 152, size=7.2, leading=12)

    box(c, track_x, bottom_y, track_w, bottom_h, "#FFFFFF")
    section_title(c, "Track Perspective", "— Cyber Security & Digital Trust", track_x + 14, 283)
    lines(c, [
        "รับมือ authorized push payment ที่ผู้ใช้ถูก fake recruiter ชักจูงให้โอนเอง",
        "ด้วย defense in depth ก่อนเงินออก:",
    ], track_x + 14, 265, size=7.2, leading=11.5)

    principle_y = [225, 184]
    principle_x = [track_x + 14, track_x + 139]
    principles = [
        ("EXPLAINABLE POLICY", ["Multi-signal rules และเหตุผล", "ที่ผู้ใช้เข้าใจได้"]),
        ("RISK-BASED CONTROL", ["Low ปกติ · Medium ยืนยัน", "High ใช้ Cooling-off"]),
        ("EVASION-AWARE", ["ตรวจยอดสะสมและประเมินซ้ำ", "รับมือแบ่งยอด/ตอบ purpose ผิด"]),
        ("PRIVACY & AUTONOMY", ["เก็บ audit data เท่าที่จำเป็น", "และไม่ล็อกเงินถาวร"]),
    ]
    for index, (title_value, body_values) in enumerate(principles):
        px = principle_x[index % 2]
        py = principle_y[index // 2]
        text(c, title_value, px, py + 17, 6.2, "#075B50", True)
        lines(c, body_values, px, py + 5, size=6.4, leading=10.3)

    box(c, track_x + 14, 105, track_w - 28, 53, "#FFF5DA", stroke="#E7D49E", radius=7, line=0.5)
    text(c, "PROTOTYPE BOUNDARY", track_x + 24, 143, 6.3, "#6D5420", True)
    lines(c, [
        "ใช้ synthetic data และ deterministic rules; destination risk เป็น simulated",
        "bank-side signal ระยะ Cooling-off จริงต้องผ่าน policy, legal และ usability",
        "validation ระบบช่วยลดความเสี่ยง แต่ไม่รับประกันว่าจะหยุด Scam ได้ทุกกรณี",
    ], track_x + 24, 129, size=5.65, leading=8.7, color="#5B4A25")

    # Evidence footer.
    c.setStrokeColor(HexColor("#C9D8D5"))
    c.setLineWidth(0.65)
    c.line(x0, 82, W - 28, 82)
    text(c, "OFFICIAL REFERENCES · ACCESSED 4 SEP 2026", x0, 69, 5.6, "#394B48", True)
    text(c, "[1] KBank Job Scam   [2] K PLUS   [3] K-ePocket   [4] KBank Anti-fraud Controls", x0, 57, 5.8, "#176C61")
    text(c, "Concept based on reviewed public information; ไม่อ้าง KBank internal access และ Email/Link scanning หรือ Fraud Specialist ไม่อยู่ใน Core", x0, 45, 5.25, "#687572")
    c.linkURL("https://www.kasikornbank.com/th/personal/digital-banking/kbankcyberrisk/pages/jobscam.aspx", (28, 52, 128, 65), relative=0)
    c.linkURL("https://www.kasikornbank.com/th/kplus/", (131, 52, 188, 65), relative=0)
    c.linkURL("https://www.kasikornbank.com/th/personal/Digital-banking/Pages/k-epocket.aspx", (190, 52, 255, 65), relative=0)
    c.linkURL("https://www.kasikornbank.com/th/news/pages/sati_fighter.aspx", (257, 52, 390, 65), relative=0)

    c.showPage()
    c.save()


if __name__ == "__main__":
    build()
    print(OUTPUT)
