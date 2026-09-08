# K PLUS JobShield V6 — Detailed End-to-End Flow

วันที่: 6 กันยายน 2026  
สถานะ: Current approved flow specification; ยังไม่ได้ Apply ไปยัง Figma canvas  
การทดสอบจริง: 0 pilot sessions conducted; 0 participant sessions conducted

## Product Position

JobShield ไม่ใช่บัญชีเงินฝากหรือ Pocket ประเภทใหม่ แต่เป็นชั้นประสบการณ์และความปลอดภัยที่ทำงานร่วมกับ K-ePocket:

เงินสำรองตั้งหลักก้อนเดียว → ออมอัตโนมัติตามแผน → Benefit ตามความต่อเนื่อง → ปกป้องก่อนเงินออก

K-ePocket ทำหน้าที่เก็บและแยกเงิน ส่วน JobShield เพิ่ม:

- ตัวช่วยคำนวณเป้าหมายเงินสำรอง 3–6 เดือน
- แผนออมอัตโนมัติที่ใช้ Schedule Transfer เป็นฐานใน MVP
- Benefit Tier ตามรอบออมที่เข้าเกณฑ์
- Savings Nudge ก่อนนำเงินฉุกเฉินออก
- Multi-signal security policy และ Cooling-off สำหรับธุรกรรมเสี่ยงสูง

## สิ่งที่ใช้ต่อจาก K PLUS และสิ่งที่ JobShield เพิ่ม

| Existing K PLUS capability | ใช้ใน Flow | JobShield เพิ่ม |
|---|---|---|
| K-ePocket และเป้าหมายการออม | เก็บเงินสำรองและแสดงยอด/ประวัติ | Protected Reserve context, goal calculator และ Benefit state |
| Schedule Transfer | ตั้งจำนวนเงินและวันที่ออมรายเดือน | คำแนะนำจากเป้าหมาย, checkpoint, grace และ tier progress |
| Transfer / Scan / Bill payment | รางทำธุรกรรมและข้อมูลแหล่งเงิน/ผู้รับ/ยอด | ตรวจหลายสัญญาณก่อนส่งคำสั่ง |
| Bank-side Fraud Risk | สัญญาณปลายทางที่ Prototype จำลอง | รวมกับ fund source, new payee, repetition และ job-payment context |
| Face verification / notifications | stronger verification และสถานะรายการ | เลือกใช้ตาม risk policy; quiet receipt สำหรับ Auto-Routing |
| Fraud reporting channel | ปลายทางของ Cancel & Report | เตรียม transaction reference และ indicators ที่จำเป็นเมื่อผู้ใช้ยินยอม |
| K Point ecosystem | ตัวอย่าง Benefit ที่เป็นไปได้ | Tier eligibility concept; ต้องผ่าน Business/Product approval |

## Phase 0 — เข้าใช้ JobShield

1. ผู้ใช้เปิด JobShield แบบ opt-in
2. ระบบอธิบายสั้น ๆ ว่า:
   - ช่วยสร้างเงินสำรองตั้งหลัก
   - ออมตามแผนอัตโนมัติได้
   - เตือนก่อนนำเงินฉุกเฉินออก
   - เพิ่มการป้องกันเมื่อพบหลายสัญญาณ Scam/Fraud
3. แสดง Privacy boundary: JobShield ไม่อ่านข้อความ อีเมล หรือ Resume
4. ผู้ใช้กด เริ่มตั้งค่า

## Phase 1 — เลือก K-ePocket และตั้งเป้าหมาย

### 1.1 ตรวจว่ามีบัญชี K-ePocket หรือไม่

- มีบัญชี K-ePocket:
  - เลือก Pocket เดิม หรือ
  - สร้าง Pocket ย่อยใหม่ชื่อ เงินสำรองตั้งหลัก ซึ่งเป็นตัวเลือกแนะนำ
- ยังไม่มีบัญชี K-ePocket:
  - ระบบนำผู้ใช้ไปเปิดบัญชี K-ePocket ตามขั้นตอนทางการของธนาคาร
  - เมื่อเปิดสำเร็จจึงกลับเข้าหน้าตั้งค่า JobShield

การเปิดบัญชี K-ePocket ไม่เรียกว่า One-tap ส่วนการสร้าง Pocket ย่อยภายในบัญชีเดิมอาจทำให้สั้นได้ตาม capability จริง

### 1.2 คำนวณเป้าหมายเงินสำรอง

1. ผู้ใช้กรอกค่าใช้จ่ายจำเป็นต่อเดือน เช่น ค่าเช่า ค่าอาหาร ค่าเดินทาง และภาระจำเป็น
2. เลือกให้เงินสำรองครอบคลุม 3 เดือน, 6 เดือน หรือกำหนดเอง
3. ระบบคำนวณ:
   ค่าใช้จ่ายจำเป็นต่อเดือน × จำนวนเดือน = เป้าหมายเงินสำรอง
4. ตัวอย่าง Prototype:
   15,000 บาท × 3 เดือน = เป้าหมาย 45,000 บาท
5. ตัวเลขนี้เป็นข้อมูลช่วยวางแผน ไม่ใช่คำแนะนำการลงทุนหรือข้อบังคับ

### 1.3 กำหนดยอดเริ่มต้น

- ผู้ใช้เลือกกันเงินที่มีอยู่เข้ามาเป็นยอดเริ่มต้น หรือ
- เริ่มที่ 0 บาทได้
- ก่อนยืนยัน ระบบแสดงยอดคงเหลือในบัญชีต้นทางและจำนวนเดือนที่เงินสำรองครอบคลุมโดยประมาณ

## Phase 2 — ตั้งแผนออมอัตโนมัติ

### 2.1 เลือกวิธีตั้งจำนวนเงิน

- จำนวนคงที่ เช่น 2,500 บาทต่อเดือน หรือ
- กรอกเปอร์เซ็นต์จากรายได้ประมาณการ เช่น 10% ของ 25,000 บาท แล้ว JobShield คำนวณออกมาเป็นจำนวนคงที่ 2,500 บาท

MVP ไม่อ้างว่าตรวจพบเงินเดือนจริงหรือหักเปอร์เซ็นต์จากเงินเข้าทุกก้อนโดยอัตโนมัติ

### 2.2 เลือกวันและบัญชีต้นทาง

1. ผู้ใช้เลือกวันที่คาดว่าเงินเดือนหรือรายได้เข้า
2. เลือกบัญชีต้นทาง
3. ปลายทางคือ Pocket เงินสำรองตั้งหลัก
4. ผู้ใช้เลือกเปิดตอนนี้หรือ ไว้ภายหลัง ได้

Schedule Transfer ยืนยันได้จากข้อมูลสาธารณะในระดับบัญชี/จำนวน/วันเวลา แต่ direct sub-pocket routing และ stop-at-cap ต้องยืนยันกับระบบภายในก่อน Production

### 2.3 Review และ Consent

แสดงให้ผู้ใช้ตรวจ:

- บัญชีต้นทาง
- จำนวนเงินคงที่
- วันที่ทำรายการ
- Pocket ปลายทาง
- เป้าหมายสูงสุด
- วิธีปรับ พัก หรือปิดแผน

Consent ต้องไม่ถูกเลือกไว้ล่วงหน้า

### 2.4 เมื่อถึงวันทำรายการ

- เงินเพียงพอและโอนสำเร็จ:
  - เติมเงินเข้า Pocket
  - แสดง Quiet Receipt
  - ไม่แสดงคำเตือน Scam
  - ส่งรอบไปตรวจ Benefit eligibility
- เงินไม่พอหรือผู้ใช้พัก:
  - ไม่ดึงจนบัญชีติดลบ
  - รอบนั้นไม่นับ Progress
  - Tier เดิมยังอยู่
  - ใช้ Grace/Pause ได้ 1–2 รอบ

## Phase 3 — Benefit Tier และ Anti-Reward-Farming

### 3.1 Qualified round

หนึ่งรอบจะเข้าเกณฑ์เมื่อ:

1. Auto-Routing สำเร็จตามแผน
2. เงินถูกเติมเข้าเงินสำรองตั้งหลัก
3. ยอดสุทธิคงอยู่ถึงวันสรุปรอบ

### 3.2 Tier progression สำหรับ Prototype

| Qualified rounds | Tier | สิ่งที่แสดง |
|---:|---|---|
| 1 เดือน | เริ่มต้น | เริ่มสร้างความต่อเนื่องแล้ว |
| 3 เดือน | ต่อเนื่อง | ออมอัตโนมัติสำเร็จต่อเนื่อง 3 รอบ |
| 6 เดือน | มั่นคง | ออมอัตโนมัติสำเร็จต่อเนื่อง 6 รอบ |

Tier 1/3/6 เดือนเป็น Prototype Rule ต้องผ่าน usability test, campaign economics และ Business Approval

### 3.3 Benefit ที่แสดงใน Prototype

- แสดง Tier, Progress และ milestone
- แสดง K Point หรือคูปองพาร์ตเนอร์ได้เฉพาะข้อความ:
  ตัวอย่างสิทธิประโยชน์ภายใต้เงื่อนไขธนาคาร
- ไม่ระบุจำนวนคะแนน มูลค่า earn rate หรือรับรองว่าจะได้รับ
- ไม่ใช้ดอกเบี้ยขั้นบันไดใน MVP

### 3.4 Grace, withdrawal และการป้องกัน Reward Farming

- พักหรือเงินไม่พอ 1–2 รอบ: รักษา Tier เดิม แต่ไม่เพิ่ม Progress
- ถอนเงินเพราะจำเป็น: ไม่ลด Tier ที่ได้รับแล้ว
- ถ้ายอดลดต่ำกว่า Checkpoint: พักความคืบหน้าไป Tier ถัดไป
- เมื่อเติมกลับถึง Checkpoint: เริ่มนับ Progress ต่อ
- การโอนเข้าแล้วถอนออกก่อนวันสรุปรอบ: รอบนั้นไม่เข้าเกณฑ์

## Phase 4 — เมื่อต้องการนำเงินสำรองออก

### 4.1 เก็บข้อมูลที่จำเป็นต่อรายการ

ระบบใช้เฉพาะข้อมูลใน Flow ธุรกรรม:

- แหล่งเงินคือ เงินสำรองตั้งหลัก
- จำนวนเงิน
- ผู้รับและสถานะ first-seen/new payee
- รูปแบบโอนซ้ำหรือยอดสะสม
- วัตถุประสงค์กว้าง ๆ ที่ผู้ใช้เลือก
- simulated destination-risk flag ใน Prototype

คำตอบเรื่องวัตถุประสงค์เป็นเพียงหนึ่ง signal และไม่สามารถล้างความเสี่ยงจากสัญญาณอื่น

### 4.2 Multi-signal policy

ตัวอย่าง High-Risk combination:

Protected Reserve + ผู้รับบุคคลใหม่ + จ่ายเพื่อสมัคร/เริ่มงาน + repetition หรือ destination risk

การนำเงินออกจาก Reserve เพียงอย่างเดียวไม่ใช่หลักฐานว่าเป็น Scam

### 4.3 Route A — ไม่เข้า High-Risk combination

1. แสดง Mascot Savings Nudge ด้วยน้ำเสียงเป็นห่วง
2. Draft copy:
   ขอชวนคิดอีกครั้งนะ เงินก้อนนี้คือเงินสำรองสำหรับเหตุฉุกเฉิน คุณยังต้องการใช้เงินก้อนนี้ใช่ไหม?
3. แสดงผลกระทบ:
   - จำนวนเงินที่จะใช้
   - ยอดคงเหลือหลังรายการ
   - จำนวนเดือนที่ยังครอบคลุมโดยประมาณ
4. ปุ่ม:
   - ใช้เงินสำรอง
   - เก็บไว้ก่อน
5. ถ้าเลือก เก็บไว้ก่อน → กลับ Reserve Dashboard
6. ถ้าเลือก ใช้เงินสำรอง → ส่งคำสั่งเข้าสู่ระบบโอนตามปกติ
7. เมื่อสำเร็จ มาสคอตส่งกำลังใจสั้น ๆ เช่น:
   รับทราบ ขอให้ทุกอย่างผ่านไปได้ด้วยดีนะ

Savings Nudge กดข้ามได้ในครั้งเดียว ไม่ถามซ้ำ ไม่สร้าง Pending Instruction และไม่เรียกรายการว่า Scam

### 4.4 Route B — เข้า High-Risk combination

1. แสดง Contextual Warning แบบจริงจังโดยไม่มี Mascot
2. แสดงเหตุผลที่สังเกตได้ไม่เกิน 2–3 ข้อ เช่น:
   - คุณยังไม่เคยโอนให้ผู้รับนี้
   - รายการนี้ใช้เงินสำรองตั้งหลัก
   - รายการนี้เกี่ยวข้องกับค่าใช้จ่ายก่อนเริ่มงาน
3. แสดงจำนวนเงินสำรองที่กำลังเสี่ยง
4. ให้เลือก:
   - Pause & Verify
   - Cancel & Report
5. Pause & Verify:
   - สร้าง Pending Instruction เพียงหนึ่งรายการ
   - ยังไม่ส่งคำสั่งเข้าสู่ PromptPay
   - เริ่ม risk-based Cooling-off
   - แนะนำตรวจผ่านช่องทางบริษัทที่ผู้ใช้ค้นหาแยกเอง
   - ทำ stronger verification และประเมินซ้ำตาม policy
6. Cancel & Report:
   - ยกเลิก Pending Instruction
   - ยืนยันว่าเงินยังไม่ถูกส่ง
   - ขอ consent ก่อนส่ง transaction reference/indicators ที่จำเป็นไปช่องทางรายงานของธนาคาร
7. เมื่อครบเงื่อนไขและผู้ใช้ยังยืนยัน:
   - ส่งคำสั่งเข้าสู่ระบบโอน
   - ยอมรับว่าระบบไม่สามารถรับประกันว่าจะหยุด Scam ได้ทุกกรณี

Repeated taps ต้องไม่สร้างคำสั่งซ้ำหรือใช้ข้าม Cooling-off

## Hero Scenario — Fake Recruiter

Synthetic fixture:

- ผู้ใช้โอน 7,900 บาทจาก เงินสำรองตั้งหลัก
- ผู้รับเป็นบัญชีบุคคลใหม่
- วัตถุประสงค์คือค่าอุปกรณ์ก่อนเริ่มงาน
- มีการโอนซ้ำหรือ simulated destination risk

Expected result:

Contextual Warning → Pending Instruction ก่อน PromptPay → Cooling-off → Pause & Verify หรือ Cancel & Report

JobShield ไม่อ่านข้อความ อีเมล หรือลิงก์ของนายจ้างเป็นค่าเริ่มต้น

## Core Integration Boundary

1. K-ePocket
   - money container, goal, balance และ source-of-funds context
2. K PLUS Transaction + Bank-side Fraud Risk
   - recipient, amount, pattern และ destination-risk signal
3. K PLUS Security & Fraud Response
   - serious warning, stronger verification, Cooling-off, notification และ Cancel & Report

Schedule Transfer และ K Point เป็นความสามารถย่อยที่ถูกใช้ภายใน journey นี้ ไม่เพิ่มจำนวน Core Integration

## Business Value Loop — Hypothesis

ออมอัตโนมัติต่อเนื่อง → เงินสำรองและ Engagement อาจเพิ่มขึ้น → ยอดเงินฝากที่มีเสถียรภาพอาจดีขึ้น → สนับสนุนฐานเงินทุนและโอกาสสร้างคุณค่าให้ธนาคาร → ธนาคารอาจพิจารณาออกแบบ Benefit คืนแก่ผู้ใช้ → เสริมแรงให้ออมต่อ

วงจรนี้เป็นสมมติฐาน ไม่ใช่คำรับรองว่าเงินฝากทุกบาทเปลี่ยนเป็นสินเชื่อหรือกำไรโดยตรง ผลจริงขึ้นกับต้นทุนเงินฝาก สภาพคล่อง เงินกองทุน ความต้องการสินเชื่อ ความเสี่ยงเครดิต กฎเกณฑ์ และ Business Approval

## Prototype And Claim Boundaries

- ใช้ deterministic rules และ synthetic data ไม่มี AI/ML model
- ไม่อ่านข้อความ อีเมล Resume หรือแชต
- ไม่กำหนด Cooling-off duration หรือ production risk score ขึ้นเอง
- ไม่รับรอง K Point, คูปอง ดอกเบี้ย หรือผลตอบแทน
- ไม่อ้างว่าเปิดบัญชี K-ePocket ได้ One-tap
- ไม่อ้าง direct sub-pocket Schedule Transfer, salary-event trigger หรือ stop-at-cap ว่ามี API พร้อมใช้
- ไม่อ้างว่ากำไรหรือการปล่อยกู้จะเพิ่มขึ้นแน่นอน
- ไม่สร้างผล usability test สมมติ

## Validation Still Required

1. Visual owner ตรวจ Figma V6 หลัง Apply จริง
2. Pilot จริง 1 คน
3. แก้ Critical/Major issues
4. Formative usability test กับผู้เข้าร่วมจริง 5–8 คน
5. ปัจจุบันยังคงเป็น 0 pilot sessions conducted และ 0 participant sessions conducted
