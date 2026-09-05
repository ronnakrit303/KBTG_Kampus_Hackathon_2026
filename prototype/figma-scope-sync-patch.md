# K PLUS JobShield — Figma Scope Sync Patch

วันที่: 5 กันยายน 2026  
Target: [K PLUS JobShield — Clickable Prototype](https://www.figma.com/design/5uoF2s6cq2JMGRFfwmdpc2)  
Page: `02 Clickable Prototype`  
สถานะ: **NOT APPLIED TO FIGMA CANVAS** — Figma Starter MCP tool-call limit ยัง active ในวันที่ 5 กันยายน 2026

ไฟล์นี้เป็น text/QA handoff สำหรับแก้ canvas ทันทีที่ MCP quota พร้อมหรือ visual owner เปิดไฟล์เอง ไม่ใช่หลักฐานว่าแก้ Figma สำเร็จแล้ว

## Global Copy Rules

1. เปลี่ยนคำที่ผู้ใช้มองเห็นเกี่ยวกับเงินก้อนนี้เป็น `เงินสำรองก่อนเงินเดือนแรก`
2. ใช้ `Cooling-off` เป็นชื่อ control หลัก; ถ้าต้องอธิบาย Dynamic Time Lock ให้เขียนว่าเป็นกลไกปรับการพักตามความเสี่ยงภายใน Cooling-off ไม่ใช่ฟีเจอร์อีกตัว
3. ใช้ข้อความสถานะ `พักคำสั่งไว้ก่อนส่งเข้าสู่ระบบโอน` และ `ยังไม่ส่งเข้าสู่ PromptPay`
4. ห้ามใช้ข้อความที่สื่อว่ามี ML model หรือคะแนนจากโมเดลจริง; Prototype นี้ใช้ multi-signal rules/policy และ synthetic data
5. Email/Link scanning และ Fraud Specialist ต้องไม่อยู่ใน Core flow; ถ้าคงไว้ใน reference frame ให้ติดป้าย `Optional/Future` ชัดเจน

## Screen Patch List

| Screen/area | Required copy or check |
|---|---|
| `00 Cover & Instructions` | ตรวจคำอธิบายให้กล่าวถึง Core 3 integrations เท่านั้น และไม่ใช้คำอ้างโมเดลที่ยังไม่ได้สร้าง |
| `01 Foundations` | Fund source label ใช้ `เงินสำรองก่อนเงินเดือนแรก`; optional items แยกจาก Core |
| `A01–A04` | Onboarding/dashboard ใช้ `Job Search Budget` และ `เงินสำรองก่อนเงินเดือนแรก`; อธิบายว่าเป็นวัตถุประสงค์บน K-ePocket |
| `H02` | ตัวเลือกแหล่งเงินใช้ `เงินสำรองก่อนเงินเดือนแรก` |
| `H05` | เหตุผลใช้ `รายการนี้ใช้เงินสำรองก่อนเงินเดือนแรก`; impact line ใช้ `หากทำรายการ เงินสำรองก่อนเงินเดือนแรกของคุณจะลดลง ฿7,900` |
| `H06` | Heading/state ใช้ `พักคำสั่งไว้ก่อนส่งเข้าสู่ระบบโอน`; supporting line ใช้ `ยังไม่ส่งเข้าสู่ PromptPay`; ไม่มี fixed duration |
| `H07–H10` | ใช้ independent verification ผ่านช่องทางทางการที่ผู้ใช้หาเอง; ไม่อ้างว่าต้องผ่าน Fraud Specialist ใน Core |
| `H11` | ยืนยันว่า Pending Instruction ถูกยกเลิกและเงินยังไม่ถูกส่ง |
| `E01–E03` | ใช้คำว่า `เงินสำรองก่อนเงินเดือนแรก` และคง limited break-glass สำหรับบัญชีตนเอง/verified biller |
| Generic/Contextual matched variants | ใช้ scenario data เดียวกัน และ contextual variant ต้องไม่เพิ่ม Email/Link scanning เป็น input |

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
- [ ] บันทึก node IDs ที่แก้และ screenshot ของ H05/H06 ใน build report
- [ ] Human visual owner ลงชื่อก่อนเปลี่ยนสถานะเป็น `READY FOR PILOT`
