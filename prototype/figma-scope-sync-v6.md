# K PLUS JobShield — Figma V6 Scope Sync

วันที่: 6 กันยายน 2026  
Target: https://www.figma.com/design/5uoF2s6cq2JMGRFfwmdpc2  
สถานะ: NOT APPLIED TO FIGMA CANVAS

## Required V6 Changes

1. เปลี่ยน One-tap K-ePocket account creation เป็น official-account-opening handoff
2. ใช้เงินสำรองตั้งหลัก Pocket เดียว และไม่มี Stage branching
3. MVP Auto-Routing ใช้จำนวนคงที่/วันที่กำหนด; เปอร์เซ็นต์คำนวณเป็นจำนวนคงที่จากรายได้ประมาณการ
4. เพิ่ม Review, consent, active, Quiet Receipt, insufficient-funds และ Grace/Pause states
5. เพิ่ม Benefit Tier สำหรับ qualified rounds 1/3/6 เดือน
6. เพิ่ม Checkpoint และ progress-held state เพื่อป้องกัน Reward Farming โดยไม่ลด Tier ที่ได้รับแล้ว
7. แสดง K Point/คูปองเฉพาะตัวอย่างภายใต้เงื่อนไขธนาคาร ไม่ระบุจำนวน มูลค่า หรือสิทธิ
8. ใช้สองเส้นทางเมื่อนำเงินออก:
   - ไม่เข้า High Risk → Mascot Savings Nudge ที่กดข้ามได้ครั้งเดียว
   - เข้า High-Risk combination → serious warning, no Mascot, Cooling-off
9. คง Pending Instruction ก่อน PromptPay และป้องกัน repeated-tap duplicate
10. คง Core Integration เพียง 3 ส่วน และไม่ใส่ Email/Link scanning หรือ Fraud Specialist ใน Core
11. ไม่ใช้คำว่า AI/ML model
12. คงสถานะ 0 pilot sessions conducted และ 0 participant sessions conducted

## New Screens And States

- S01N — official K-ePocket opening handoff
- A01–A07 — Auto-save setup, execution และ Grace
- B01–B04 — Benefit eligibility, Tier และ Checkpoint hold
- W03 — Mascot Savings Nudge
- W05 — supportive Mascot หลัง legitimate withdrawal สำเร็จ

## Copy Guardrails

- Mascot: เป็นห่วง กระชับ ไม่กล่าวโทษ และไม่ถามซ้ำ
- Serious warning: ตรงไปตรงมา อธิบายเหตุผลที่สังเกตได้ไม่เกิน 2–3 ข้อ
- Quiet Receipt: ไม่มีภาษา Scam
- Benefit: ติดป้าย Prototype Rule และ Business-dependent
- Business: ใช้ may/can support; ไม่รับรองว่ากำไรหรือการปล่อยกู้เพิ่ม

## Verification Checklist

- [ ] ไม่มี Career Stage หรือ Job Search Budget ใน current Present paths
- [ ] ไม่มี One-tap K-ePocket account-opening claim
- [ ] Auto-save ใช้ fixed amount/date ใน MVP
- [ ] Tier 1/3/6 และ Grace 1–2 แสดงว่าเป็น Prototype rules
- [ ] Withdrawal ไม่ลด earned Tier
- [ ] Checkpoint hold ป้องกัน immediate in/out Reward Farming
- [ ] Mascot ไม่ปรากฏใน High-Risk screens
- [ ] Savings Nudge ทำต่อได้ด้วยหนึ่ง action และไม่สร้าง Pending Instruction
- [ ] High path พักคำสั่งก่อน PromptPay
- [ ] ไม่มี guaranteed K Point, coupon, special interest, profit หรือ lending claim
- [ ] Visual owner ตรวจ overflow, contrast, focus และ touch targets
- [ ] READY FOR PILOT เฉพาะหลัง human visual-owner sign-off

Current status: 0 pilot sessions conducted; 0 participant sessions conducted.
