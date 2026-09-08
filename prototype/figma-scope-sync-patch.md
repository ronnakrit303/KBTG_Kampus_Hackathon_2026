# K PLUS JobShield — Figma Scope Sync Patch

> Superseded on 6 September 2026 by [figma-scope-sync-v6.md](./figma-scope-sync-v6.md). ไฟล์นี้เก็บ V4 patch ไว้เป็น prior handoff เท่านั้น ห้ามใช้เป็น current scope

วันที่: 6 กันยายน 2026

Target: [K PLUS JobShield — Clickable Prototype](https://www.figma.com/design/5uoF2s6cq2JMGRFfwmdpc2)

Page: `02 Clickable Prototype`

สถานะ: **V4 SINGLE-RESERVE PATCH — NOT APPLIED TO FIGMA CANVAS**

ไฟล์นี้เป็น text/QA handoff สำหรับแก้ canvas ทันทีที่ MCP quota พร้อมหรือ visual owner เปิดไฟล์เอง ไม่ใช่หลักฐานว่าแก้ Figma สำเร็จแล้ว

## Global Copy Rules

1. เปลี่ยนคำที่ผู้ใช้มองเห็นเกี่ยวกับเงินก้อนนี้เป็น `เงินสำรองก่อนเงินเดือนแรก`
2. ใช้ `Cooling-off` เป็นชื่อ control หลัก; ถ้าต้องอธิบาย Dynamic Time Lock ให้เขียนว่าเป็นกลไกปรับการพักตามความเสี่ยงภายใน Cooling-off ไม่ใช่ฟีเจอร์อีกตัว
3. ใช้ข้อความสถานะ `พักคำสั่งไว้ก่อนส่งเข้าสู่ระบบโอน` และ `ยังไม่ส่งเข้าสู่ PromptPay`
4. ห้ามใช้ข้อความที่สื่อว่ามี ML model หรือคะแนนจากโมเดลจริง; Prototype นี้ใช้ multi-signal rules/policy และ synthetic data
5. Email/Link scanning และ Fraud Specialist ต้องไม่อยู่ใน Core flow; ถ้าคงไว้ใน reference frame ให้ติดป้าย `Optional/Future` ชัดเจน
6. JobShield เป็น `ชั้นความปลอดภัยก่อนโอนที่ต่อยอด K-ePocket` ไม่ใช้คำที่ทำให้เข้าใจว่าเป็น Escrow หรือบัญชีเงินฝากชนิดใหม่
7. High-Risk state พักเฉพาะคำสั่งและยอดรายการนั้น ไม่ล็อกทั้ง pocket/account; repeated taps ต้องไม่สร้างคำสั่งซ้ำ
8. ใช้ protected reserve ก้อนเดียว: `เงินสำรองก่อนเงินเดือนแรก` เปลี่ยนวัตถุประสงค์เป็น `เงินสำรองฉุกเฉิน` หลังผู้ใช้ได้รับเงินเดือนและยืนยัน; ไม่มี Job Search Budget
9. Auto-Routing เป็น opt-in, ปรับ/พัก/ปิดได้ และหยุดเมื่อถึงเพดานที่ผู้ใช้ตั้ง
10. K Point ติดป้าย `แนวคิดในอนาคต—ต้องผ่าน Business/Product approval`; ไม่แสดงดอกเบี้ยพิเศษ

## Screen Patch List

| Screen/area | Required copy or check |
|---|---|
| `00 Cover & Instructions` | ตรวจคำอธิบายให้กล่าวถึง Core 3 integrations เท่านั้น และไม่ใช้คำอ้างโมเดลที่ยังไม่ได้สร้าง |
| `01 Foundations` | Fund source label ใช้ `เงินสำรองก่อนเงินเดือนแรก`; optional items แยกจาก Core |
| `A01–A04` | Onboarding/dashboard ให้เลือก career stage และตั้งยอด `เงินสำรองก่อนเงินเดือนแรก` ก้อนเดียว |
| `A01K–A01N` (new) | ตรวจว่ามี K-ePocket หรือไม่; หากไม่มีให้สร้างเงินสำรองหนึ่ง Pocket แบบ One-tap และบอกผลของการข้ามอย่างตรงไปตรงมา |
| `H02` | ตัวเลือกแหล่งเงินใช้ `เงินสำรองก่อนเงินเดือนแรก` |
| `H05` | เหตุผลใช้ `รายการนี้ใช้เงินสำรองก่อนเงินเดือนแรก`; impact line ใช้ `หากทำรายการ เงินสำรองก่อนเงินเดือนแรกของคุณจะลดลง ฿7,900` |
| `H06` | Heading/state ใช้ `พักคำสั่งไว้ก่อนส่งเข้าสู่ระบบโอน`; supporting line ใช้ `ยังไม่ส่งเข้าสู่ PromptPay`; ไม่มี fixed duration |
| `H07–H10` | ใช้ independent verification ผ่านช่องทางทางการที่ผู้ใช้หาเอง; ไม่อ้างว่าต้องผ่าน Fraud Specialist ใน Core |
| `H11` | ยืนยันว่า Pending Instruction ถูกยกเลิกและเงินยังไม่ถูกส่ง |
| `E01–E03` | ใช้คำว่า `เงินสำรองก่อนเงินเดือนแรก` และคง limited break-glass สำหรับบัญชีตนเอง/verified biller |
| Generic/Contextual matched variants | ใช้ scenario data เดียวกัน และ contextual variant ต้องไม่เพิ่ม Email/Link scanning เป็น input |
| `R00–R07B` (new) | เพิ่ม Protected Reserve/Auto-Routing flow ตาม `prototype/protected-savings-extension-spec.md`; high-risk withdrawal route กลับ H05/H06 |

## Core Integration Copy

หากมี overview/architecture frame ให้แสดงเพียง:

1. `K-ePocket` — แยกเงินตามวัตถุประสงค์
2. `K PLUS Transaction + Bank-side Fraud Risk` — ผู้รับ ยอด รูปแบบธุรกรรม และสัญญาณความเสี่ยงปลายทาง
3. `K PLUS Security & Fraud Response` — contextual warning, stronger verification, Cooling-off และ Cancel/Report

## Verification After Applying

- [ ] ค้นทั้งไฟล์แล้วไม่พบคำเรียกเงินก้อนเดิมในหน้าจอที่ใช้งาน
- [ ] ค้นทั้งไฟล์แล้วไม่พบคำอ้าง ML/model ที่ไม่ได้สร้าง
- [ ] H06 อยู่ก่อนทุกเส้นทาง transfer success
- [ ] H06 ระบุชัดว่า Pending Instruction ยังไม่เข้าสู่ PromptPay
- [ ] Email/Link scanning และ Fraud Specialist ไม่ปรากฏใน Core flow
- [ ] Core overview มี 3 integrations เท่านั้น
- [ ] เปิด Present mode จากทั้ง 10 start points แล้วไม่มี dead end หรือข้อความล้นหลังเปลี่ยน copy
- [ ] เพิ่มและทดสอบ `START-NO-EPOCKET`, `START-RESERVE-SETUP` และ `START-RESERVE-WITHDRAW`
- [ ] R07A ใช้เงินฉุกเฉินจริงได้โดยไม่มี fixed delay; R07B เป็น dismissible self-control nudge; High-Risk route เท่านั้นที่เข้า H05/H06
- [ ] Auto-Routing consent ไม่ถูก preselect และมี edit/pause/stop-at-cap ที่หาเจอได้
- [ ] K Point/ดอกเบี้ยไม่มีตัวเลขหรือข้อความรับรองสิทธิ
- [ ] บันทึก node IDs ที่แก้และ screenshot ของ H05/H06 ใน build report
- [ ] Human visual owner ลงชื่อก่อนเปลี่ยนสถานะเป็น `READY FOR PILOT`
