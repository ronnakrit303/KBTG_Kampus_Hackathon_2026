# JobShield — One Continuous Protected Reserve (Figma-ready)

> Superseded for current build by jobshield-flow-v6.md and figma-flow-spec-v6.md. Retained as a V5 snapshot.

วันที่: 6 กันยายน 2026

สถานะ: **V5 SPEC READY — NOT APPLIED TO FIGMA CANVAS**

Target: [K PLUS JobShield — Clickable Prototype](https://www.figma.com/design/5uoF2s6cq2JMGRFfwmdpc2)

## Product Position

JobShield ใช้ K-ePocket ชื่อ `เงินสำรองตั้งหลัก (Protected Reserve)` เพียงก้อนเดียวตลอดการใช้งาน ผู้ใช้ไม่ต้องเลือกว่ากำลังหางาน รอเงินเดือน หรือได้รับเงินเดือนแล้ว และระบบไม่เปลี่ยนชื่อหรือย้าย Pocket เมื่อสถานะงานเปลี่ยน

วงจรหลักคือ:

1. **Set up** — สร้างหรือเชื่อมเงินสำรองตั้งหลัก กำหนดค่าใช้จ่ายจำเป็น เป้าหมาย และยอดเริ่มต้น
2. **Build** — เปิด Auto-Routing ตอนนี้หรือภายหลัง ติดตามยอดและจำนวนเดือนที่ครอบคลุม
3. **Protect** — เมื่อเงินกำลังออก ระบบแยก Savings Nudge ออกจาก Fraud/Scam Intervention และใช้ friction ตามระดับความเสี่ยง

K-ePocket เป็น money container ส่วน JobShield เป็น goal/automation experience และ security policy layer ก่อนโอน ไม่ใช่ Escrow หรือบัญชีเงินฝากชนิดใหม่

## End-to-End Flow

```text
S00 เปิด JobShield
        ↓
S01 ตรวจว่ามี K-ePocket ที่จะใช้เป็นเงินสำรองตั้งหลักหรือไม่
        ├─ มี → เชื่อม Pocket เดิม
        └─ ไม่มี → สร้าง Pocket เดียวแบบ One-tap
        ↓
S02 กรอกค่าใช้จ่ายจำเป็นต่อเดือน
        ↓
S03 เลือกเป้าหมาย 3 / 6 เดือน / กำหนดเอง
        ↓
S04 กำหนดยอดเริ่มต้นจากเงินที่มีอยู่
        ↓
S05 ตั้ง Auto-Routing ตอนนี้หรือเลือก “ไว้ภายหลัง”
        ↓
S06 ตรวจสอบและให้ความยินยอม
        ↓
S07 Reserve Dashboard
        ↓
S08 ต้องการนำเงินออก
        ├─ บัญชีตนเอง/verified biller → S09A Normal access
        ├─ ค่าใช้จ่ายทั่วไปที่ไม่จำเป็น → S09B Savings Nudge
        └─ หลาย Fraud/Scam signals → H05 → H06
```

## Screen Specification

### S00 — JobShield Introduction

- Heading: `สร้างเงินสำรอง และเพิ่มเกราะก่อนโอน`
- Copy: `JobShield ช่วยตั้งเป้าหมาย เติมเงินอย่างต่อเนื่อง และตรวจหลายสัญญาณเมื่อเงินสำรองกำลังถูกโอนไปยังปลายทางเสี่ยง`
- Privacy: `ไม่อ่านข้อความ อีเมล หรือ Resume`
- Primary: `เริ่มตั้งค่า`

### S01 — K-ePocket Check

- อธิบายว่า K-ePocket ใช้แยกเงิน ส่วน JobShield เพิ่มเป้าหมาย Auto-Routing และการป้องกันก่อนโอน
- Existing: `เลือก Pocket เดิม`
- Missing: `สร้างเงินสำรองตั้งหลัก`
- Skip: `ไว้ภายหลัง` พร้อมบอกว่าฟังก์ชันที่อาศัย protected fund source จะยังทำงานไม่ครบ

### S02 — Essential Monthly Expense

- Heading: `ในหนึ่งเดือน คุณต้องใช้เงินจำเป็นประมาณเท่าไร`
- Helper: `เช่น ค่าเช่า ค่าอาหาร ค่าเดินทาง และภาระจำเป็น`
- Privacy: ใช้เฉพาะตัวเลขที่กรอกเพื่อคำนวณเป้าหมาย

### S03 — Reserve Target

- Options: `3 เดือน`, `6 เดือน`, `กำหนดเอง`
- Formula: `ค่าใช้จ่ายจำเป็นต่อเดือน × จำนวนเดือน`
- Example fixture: `฿15,000 × 3 เดือน = เป้าหมาย ฿45,000`
- เป็นข้อมูลช่วยตัดสินใจ ไม่ใช่คำแนะนำการลงทุนหรือข้อบังคับ

### S04 — Starting Amount

- ผู้ใช้นำเงินที่มีอยู่มากันเป็นยอดเริ่มต้นได้
- แสดงยอดคงเหลือในบัญชีต้นทางและจำนวนเดือนที่เงินสำรองครอบคลุมโดยประมาณ
- ไม่มีขั้นต่ำสมมติและไม่บังคับให้เติมถึงเป้าหมายทันที

### S05 — Auto-Routing

- เลือกจำนวนคงที่หรือเปอร์เซ็นต์ของเงินเข้า เช่น 5%, 10%, 15% หรือกำหนดเอง
- เลือกบัญชีต้นทางและกำหนดเวลา/เหตุการณ์เงินเข้าที่ผู้ใช้ตั้งเอง
- Toggle: `หยุดอัตโนมัติเมื่อถึงเป้าหมาย`
- Secondary: `ไว้ภายหลัง` สำหรับผู้ที่ยังไม่มีรายได้สม่ำเสมอ
- MVP ใช้ schedule หรือ synthetic incoming-fund event; ไม่อ้างว่า K PLUS ตรวจเงินเดือนได้แล้ว

### S06 — Review And Consent

- แสดง source, amount/percentage, destination Pocket, cap และ next route
- Consent: `ยืนยันให้แบ่งเงินตามกฎนี้จนถึงเป้าหมาย หรือจนกว่าฉันจะปิด`
- Consent ไม่ถูกเลือกไว้ล่วงหน้า
- มี edit, pause และ off

### S07 — Reserve Dashboard

- แสดง current balance, target และ estimated months covered
- ตัวอย่าง: `฿24,000 จากเป้าหมาย ฿45,000 — ครอบคลุมประมาณ 1.6 เดือน`
- Auto-Routing state: off / active / paused / goal reached
- K Point แสดงได้เฉพาะ `แนวคิดในอนาคต—ต้องผ่าน Business/Product approval`

### S08 — Withdrawal Context

- ผู้ใช้ระบุยอด ปลายทาง และวัตถุประสงค์กว้าง ๆ
- แสดงยอดคงเหลือและจำนวนเดือนที่คาดว่าจะครอบคลุมหลังทำรายการ
- purpose answer เป็น signal หนึ่ง ไม่ใช่ bypass switch

### S09A — Normal/Essential Access

- ใช้กับบัญชีตนเองหรือ verified biller เมื่อไม่มี risk conflict
- แสดงผลกระทบต่อเงินสำรองอย่างเป็นกลาง
- ไม่มี fixed delay และไม่มี High-Risk Scam warning

### S09B — General-Spending Savings Nudge

- ใช้กับค่าใช้จ่ายทั่วไปที่ไม่จำเป็นและไม่มี Fraud signal
- Heading: `ขอชวนคิดอีกครั้งก่อนใช้เงินก้อนนี้`
- Primary: `เก็บเงินไว้ก่อน`
- Secondary: `ยังต้องการใช้เงิน`
- กดข้ามได้ทันที ไม่สร้าง Pending Instruction และไม่กล่าวหาว่าเป็น Scam

### High-Risk Route

- Trigger เฉพาะเมื่อมีหลายสัญญาณ เช่น ผู้รับบุคคลใหม่ + protected reserve + job-payment/repetition/destination risk
- Route ไป `H05 Contextual Warning → H06 Pending Instruction`
- พักเฉพาะคำสั่งและยอดรายการนั้นก่อนเข้าสู่ PromptPay ไม่ล็อก Pocket หรือบัญชีทั้งหมด
- repeated taps ต้องไม่สร้างคำสั่งซ้ำหรือข้าม Cooling-off

## Alert-Fatigue And False-Positive Guardrails

- Auto-Routing สำเร็จ: quiet receipt ไม่แสดง Scam warning
- บัญชีตนเอง/verified biller: normal flow เมื่อไม่มี risk conflict
- ค่าใช้จ่ายทั่วไป: dismissible Savings Nudge
- High-Risk: ต้องมีหลายสัญญาณและแสดงเหตุผลที่สังเกตได้ไม่เกิน 2–3 ข้อ
- การนำเงินออกจาก Reserve เพียงอย่างเดียวไม่ใช่หลักฐาน Scam
- ตัวละครเป็นมิตรใช้กับ Savings Nudge ได้ แต่ High-Risk warning ต้องจริงจังและไม่ใช้สีเป็นสัญญาณเดียว

## Feasibility Boundary

| Item | Prototype | Production boundary |
|---|---|---|
| Goal calculator | deterministic synthetic data | plausible |
| Starting amount | simulated transfer | requires K-ePocket integration |
| Auto-Routing | schedule/synthetic incoming event | internal APIs and payment rules unconfirmed |
| Risk-based protection | deterministic policy + synthetic scenarios | requires fraud-policy and operations validation |
| K Point | future concept card only | requires Business/Product approval |

Prototype ใช้ข้อมูลสมมติทั้งหมด ไม่อ่านอีเมล/ข้อความ ไม่มี ML model และไม่พิสูจน์ production feasibility หรือ user demand จนกว่าจะทดสอบกับผู้ใช้จริง
