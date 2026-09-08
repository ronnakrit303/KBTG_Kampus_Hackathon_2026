# K PLUS JobShield — Visual Owner Review

> Scope note — 6 กันยายน 2026: เอกสารนี้บันทึกการตรวจ canvas รุ่นก่อน V6; current scope อยู่ใน [figma-flow-spec-v6.md](./figma-flow-spec-v6.md) จึงต้อง visual-review ใหม่หลัง Sync V6

วันที่เตรียม: 4 กันยายน 2026; scope checklist updated 5 กันยายน 2026  
สถานะ: Automated pre-check completed for prior canvas; V6 screens/copy and human visual-owner sign-off pending

ผู้รับผิดชอบตามแผน: สมาชิกคนที่สอง — final visual/prototype owner

## Figma Target

- [K PLUS JobShield — Clickable Prototype](https://www.figma.com/design/5uoF2s6cq2JMGRFfwmdpc2)
- Page ที่ต้องตรวจ: `02 Clickable Prototype`
- ขอบเขต: concept prototype ไม่ใช่ official K PLUS UI

## Evidence Checked

- Structural audit: 31 screens
- Reaction audit: 44/44 links resolved, missing destination = 0
- Testing start points: 10
- Visual screenshots inspected: `A04` และ `E02`
- Additional screenshots unavailable because Figma Starter MCP call limit remained active; authenticated browser view was not available in this environment

## Automated Pre-Check Findings

### A04 — Scenario Dashboard

- Thai font rendered correctly and headings/actions were readable
- Four scenario actions were visually distinct and touch targets appeared large enough
- Job Search Budget และเงินสำรองก่อนเงินเดือนแรกถูกแยกด้วย label และ container ชัดเจน
- Prototype disclaimer was present
- Non-blocking observation: the lower part of the screen has substantial empty space; visual owner may retain it for calm hierarchy or rebalance vertical spacing

### E02 — Emergency Review

- เหตุผลเรื่องบัญชีตนเอง ยอดเงินสำรองก่อนเงินเดือนแรกคงเหลือ และ security note ถูกแยกชัดเจน
- Screen used semantic labels in addition to green/amber color
- Primary `ยืนยัน` action was visible at the bottom
- No High-Risk Scam warning appeared in the emergency path
- Non-blocking observation: verify the top header and body remain visible at 100% text size and with Thai text scaling

## Required Human Visual Review Before Pilot

เปิดแต่ละ start point ใน Present mode และทำเครื่องหมายจากสิ่งที่เห็นจริง:

- [ ] `START-SETUP`: A00–A04 ไม่มีข้อความล้น ปุ่มถูกตัด หรือ dead end
- [ ] ทุกหน้าที่กล่าวถึงเงินก้อนนี้ใช้คำว่า `เงินสำรองก่อนเงินเดือนแรก`
- [ ] Core integration overview มีเพียง 3 ส่วน: K-ePocket, K PLUS Transaction + Bank-side Fraud Risk และ K PLUS Security & Fraud Response
- [ ] ไม่มี Email/Link scanning หรือ Fraud Specialist ใน Core flow; ถ้ามีในหน้าสำรองต้องติดป้าย Optional/Future
- [ ] ไม่มีการเรียก Dynamic Time Lock เป็นฟีเจอร์แยก และไม่มีข้อความอ้างโมเดลที่ยังไม่ได้สร้าง
- [ ] `START-HIGH-FULL`: H01–H12 ใช้งานได้ครบทั้ง Pause, Cancel/Report และ deliberate continuation
- [ ] `H05`: เห็นเหตุผล 3 ข้อ, ผลกระทบต่อเงินสำรองก่อนเงินเดือนแรก และข้อความ `รายการยังไม่ถูกส่ง` โดยไม่ต้องเลื่อนหา
- [ ] `H06`: เห็นข้อความ `พักคำสั่งไว้ก่อนส่งเข้าสู่ระบบโอน` และ `ยังไม่ส่งเข้าสู่ PromptPay` เด่นกว่ารายละเอียดรอง และไม่มีข้อความที่สื่อว่าธนาคารรับรอง employer
- [ ] `START-S1-GENERIC` เทียบ `START-S1-CONTEXTUAL`: ความต่างอยู่ที่ warning content/action ไม่ใช่คุณภาพภาพหรือ layout ที่ลำเอียงชัดเจน
- [ ] `START-S2-GENERIC` เทียบ `START-S2-CONTEXTUAL`: scenario data ตรงกันภายในคู่ทดสอบ
- [ ] `START-LEGIT-LOW`: verified payment channel ไม่ถูกเขียนเหมือนรับรอง employer/offer
- [ ] `START-LEGIT-MEDIUM`: Medium warning ไม่ดูรุนแรงเท่า High Risk และยังทำรายการต่อได้
- [ ] `START-EMERGENCY`: โอนไปบัญชีตนเองได้โดยไม่มี fixed delay หรือ High-Risk warning
- [ ] ทุกหน้าจอ: ไม่มี clipping/overflow ที่ขนาดปกติ และลองเพิ่ม text size อย่างน้อยหนึ่งระดับ
- [ ] ทุก action: touch target อย่างน้อยประมาณ 44 px และลำดับปุ่มปลอดภัยชัดเจน
- [ ] Contrast: body/action text อ่านได้ และไม่ได้ใช้สีเป็นสัญญาณเดียว
- [ ] `START-NO-EPOCKET`: ผู้ใช้เข้าใจว่า K-ePocket แยกเงิน ส่วน JobShield ปกป้องก่อนโอน และสามารถสร้างสองกระเป๋าแบบ One-tap ได้
- [ ] `START-RESERVE-SETUP`: ผู้ใช้ตั้ง essential-expense target, Auto-Routing และ stop-at-cap ได้ โดย consent ไม่ถูกเลือกไว้ล่วงหน้า
- [ ] `START-RESERVE-WITHDRAW`: own/verified emergency, general-spending nudge และ High-Risk route ให้ friction ต่างกันตาม specification
- [ ] Friendly character ใช้เฉพาะ nudge/education; High-Risk Scam screen ยังจริงจังและไม่ใช้สีเป็นสัญญาณเดียว
- [ ] K Point/ดอกเบี้ยติดป้ายว่าเป็นแนวคิดที่ยังไม่รับรอง และไม่มีอัตราหรือ reward earn rate สมมติ
- [ ] Prototype-only labels ไม่ปะปนกับข้อความที่จะเสนอเป็น production claim

## Issue Log — Fill From Actual Review

| ID | Screen | Severity | Observed issue | Required change | Status |
|---|---|---|---|---|---|
| — | — | — | ยังไม่มี human visual-owner finding | — | Pending |

Severity: `Critical` = เสี่ยงทำรายการผิด/เข้าใจ transaction state ผิด, `High` = ขวาง task หรือหา safety action ไม่พบ, `Medium` = ต้องอธิบายเพิ่ม, `Low` = cosmetic

## Sign-Off — Human Visual Owner Only

```text
Reviewer:
Review date/time:
Screens/start points reviewed:
Critical findings remaining: 0 / list
High findings remaining: 0 / list
Decision: READY FOR PILOT / REVISE BEFORE PILOT
Notes:
```

ห้ามกรอก `READY FOR PILOT` จาก automated audit หรือการคาดเดา ต้องเป็นผลจากการเปิดและตรวจ prototype จริงโดย visual owner
