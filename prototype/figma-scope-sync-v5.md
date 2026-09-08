# K PLUS JobShield — Figma V5 Scope Sync

> Superseded for current build by figma-scope-sync-v6.md. Retained as a V5 snapshot.

วันที่: 6 กันยายน 2026

Target: [K PLUS JobShield — Clickable Prototype](https://www.figma.com/design/5uoF2s6cq2JMGRFfwmdpc2)

สถานะ: **NOT APPLIED TO FIGMA CANVAS**

## Global Replacements

1. ใช้ `เงินสำรองตั้งหลัก` แทน `เงินสำรองก่อนเงินเดือนแรก` และ `เงินสำรองฉุกเฉิน` ใน current presentation paths
2. ลบหน้าจอเลือก career stage และเส้นทางเปลี่ยน Pocket หลังได้รับเงินเดือน
3. ลบ `Job Search Budget` จาก current presentation paths
4. Setup ต้องสร้างหรือเชื่อม K-ePocket เดียว กำหนดค่าใช้จ่ายจำเป็น เป้าหมาย และ starting amount
5. Auto-Routing ต้องเลือก `เปิดตอนนี้` หรือ `ไว้ภายหลัง` ได้ พร้อม edit/pause/off/stop-at-goal
6. Core overview แสดงเพียง 3 integrations
7. Email/Link scanning และ Fraud Specialist ไม่อยู่ใน Core
8. ใช้ deterministic policy + synthetic data และไม่ใช้คำว่า AI/ML model
9. Cooling-off ระบุ `พักคำสั่งไว้ก่อนส่งเข้าสู่ระบบโอน` และ `ยังไม่ส่งเข้าสู่ PromptPay`
10. Savings Nudge ต้องกดข้ามได้และไม่ใช้ข้อความกล่าวหาว่าเป็น Scam

## Current Screen Map

สร้าง Flow ตาม [figma-flow-spec-v5.md](./figma-flow-spec-v5.md):

- S00–S07: Setup, goal, starting amount, Auto-Routing และ Dashboard
- S08–S09B: Withdrawal, normal access และ Savings Nudge
- H01–H12: Fake Recruiter hero scenario และ High-Risk Cooling-off
- T00: neutral test end

## High-Risk Copy

- Source: `เงินสำรองตั้งหลัก`
- Observable reasons: ผู้รับใหม่ / เงินสำรองตั้งหลัก / ค่าใช้จ่ายก่อนเริ่มงาน
- Impact: `หากทำรายการ เงินสำรองตั้งหลักของคุณจะลดลง ฿7,900`
- Action: `Pause & Verify` / `Cancel/Report`
- State: `พักคำสั่งไว้ก่อนส่งเข้าสู่ระบบโอน` และ `ยังไม่ส่งเข้าสู่ PromptPay`

## Verification

- [ ] current Present paths ไม่มี Stage selection
- [ ] current Present paths ไม่มีชื่อเงินสำรอง V4 หรือ Job Search Budget
- [ ] Auto-Routing consent ไม่ถูกเลือกไว้ล่วงหน้าและมี `ไว้ภายหลัง`
- [ ] own account/verified biller fixture ไม่เข้า High เมื่อ destination risk เป็น neutral
- [ ] general-spending fixture เข้า Savings Nudge และกดทำต่อได้ทันที
- [ ] High fixture ต้องใช้หลายสัญญาณและ H06 อยู่ก่อน transfer success
- [ ] repeated taps ไม่สร้าง Pending Instruction ซ้ำ
- [ ] ไม่มี fixed cooling-off duration, model score หรือ fabricated result
- [ ] visual owner ตรวจ contrast, text overflow, text scaling, focus order และ touch target
- [ ] สถานะเป็น `READY FOR PILOT` เฉพาะหลัง human visual-owner sign-off

สถานะการทดสอบยังเป็น `0 pilot sessions conducted` และ `0 participant sessions conducted`.
