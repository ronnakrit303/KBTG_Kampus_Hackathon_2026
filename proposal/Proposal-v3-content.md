# K PLUS JobShield — Proposal V3 Content

**สถานะ:** Candidate one-page pitch; ต้องให้ผู้ใช้ตรวจและอนุมัติก่อนส่ง  
**ภาษา:** ไทยเป็นหลัก พร้อม required English headings และ technical terms

## Value proposition

> ชั้นความปลอดภัยบน K-ePocket ที่ช่วย First Jobbers สร้าง “เงินสำรองตั้งหลัก” อย่างต่อเนื่อง และเพิ่มช่วงหยุดคิดเมื่อหลายสัญญาณบ่งชี้ว่ากำลังถูกหลอกให้จ่ายเงินเพื่อแลกกับงาน

## Problem Statement

First Jobbers อายุ 22–30 อยู่ในช่วงเปลี่ยนผ่านที่ต้องจัดการค่าใช้จ่าย เริ่มสร้างเงินสำรอง และอาจกำลังรอการติดต่อจากผู้ว่าจ้างหลายแห่ง ขณะเดียวกัน Fake Recruiter สามารถปลอมเป็นบริษัทแล้วเรียกค่าสมัคร ค่าอบรม ค่าอุปกรณ์ หรือเงินมัดจำก่อนเริ่มงานได้

ธุรกรรมประเภทนี้อันตรายเพราะผู้ใช้เป็นผู้ยืนยันการโอนเองภายใต้ Social Engineering: ระบบ Authentication อาจยืนยัน “ผู้ใช้ตัวจริง” ได้ แต่ยังไม่รู้ว่า “เจตนากำลังถูกหลอก” ขณะที่ 77.3% ของคนไทยมีเงินออมฉุกเฉินไม่ถึง 6 เดือน จึงควรปกป้องเงินสำรองก่อนออกจากบัญชี โดยไม่กล่าวว่าสถิตินี้เป็นของ First Jobbers โดยเฉพาะ

## Target Users

First Jobbers อายุ 22–30 ที่กำลังหางาน เริ่มงาน หรือสร้างฐานะช่วงแรก และเลือกเปิด JobShield ด้วยตนเอง จุดเสี่ยงมาจากบริบทช่วงเปลี่ยนผ่านและแรงกดดัน ไม่ใช่การเหมารวมว่ากลุ่มนี้ประมาทกว่าผู้อื่น

## Proposed Solution

### 1. Build — สร้างเงินสำรองตั้งหลัก

เลือกหรือสร้าง K-ePocket กำหนดเป้าหมายจากค่าใช้จ่ายจำเป็น 3–6 เดือน แล้วตั้ง Scheduled Auto-Allocation ตามจำนวนและวันที่ที่เลือก ผู้ใช้ปรับ พัก หรือปิดได้ ส่วน Save Point/Benefit Tier เป็น Product Hypothesis ที่ต้องทดสอบและขออนุมัติ

### 2. Detect — เชื่อมหลายสัญญาณก่อนเงินออก

เมื่อโอนจาก Protected Reserve ระบบฝั่ง Server เชื่อมแหล่งเงิน ผู้รับใหม่/บัญชีบุคคล วัตถุประสงค์จ่ายเพื่อสมัครหรือเริ่มงาน การโอนซ้ำ/แบ่งยอด Destination Risk จากระบบธนาคาร และ Device/Session signal ที่มี โดยไม่อ่านข้อความหรืออีเมลอัตโนมัติ

### 3. Intervene — เพิ่ม Friction ตามความเสี่ยง

- Low: ดำเนินรายการปกติ
- Medium: Contextual warning พร้อมเหตุผล 2–3 ข้อ และให้ยืนยันอย่างตั้งใจ
- High: พักเฉพาะคำสั่งโอนเป็น Server-side Cooling-off ก่อนเข้า Payment Hub พร้อม `Pause & Verify` ผ่านช่องทางบริษัททางการ หรือ `Cancel & Report`

## Novelty

K-ePocket ช่วยแยกและตั้งเป้าหมายเงิน; JobShield เพิ่ม Context-aware Security Policy ที่เข้าใจว่าเงินก้อนนี้คือ Protected Reserve และปรับการป้องกันตามผู้รับ บริบทธุรกรรม และความเสี่ยงปลายทาง ณ จังหวะก่อนเงินออก

## Value Proposition

### สำหรับ First Jobbers

- ลดภาระการจำออมทุกเดือนและเห็นความคืบหน้าของเงินสำรอง
- ได้คำเตือนที่อธิบายเหตุผล ไม่กล่าวโทษ และยังเข้าถึงเงินฉุกเฉินที่ถูกต้องได้
- เพิ่มเวลาตรวจสอบก่อนสูญเสียเงินให้ Fake Recruiter

### สำหรับ K PLUS

- ต่อยอด K-ePocket และ Fraud controls ที่มีอยู่เป็น Journey เดียว
- มีโอกาสเพิ่ม Engagement และความต่อเนื่องของเงินฝาก โดยต้องพิสูจน์ Product economics
- ขยับจาก Awareness/แก้เหตุหลังโอน สู่ Pre-loss intervention พร้อม Audit/Report path

## Track Perspective — Cyber Security & Digital Trust

JobShield ใช้ Defense in Depth: Mobile request integrity → Multi-signal risk correlation → Versioned policy → Server-side enforcement → Incident telemetry ระบบแยก Technical rejection ออกจาก Scam-risk intervention และออกแบบตาม Privacy by Design, Data minimization, Explainability และ User autonomy

MVP ใช้ Deterministic rules, Synthetic transactions และ Destination-risk flag จำลอง ไม่อ้างว่าเป็น AI/ML หรือเชื่อม Production จริง วัด Rule/test coverage, warning comprehension, Pause/Cancel, False positive, legitimate completion และ latency; Precision/Recall ต้องรอข้อมูลจริงที่มี Ground truth

