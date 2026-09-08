# K PLUS Track 3 Concept Decision

Status: V6 integration-and-benefit scope approved on 2026-09-06; repository sync in progress; Test Final Proposal 1 and Diagram v2/v3/v4/v5 retained as prior snapshots; Figma canvas sync, pilot and participant sessions remain pending
Created: 2026-09-03
Approval: `Test_ Final-Proposal-1.pdf` created by explicit user request; final submission wording/design still awaits user review and test evidence

## Summary

แนวคิดปัจจุบันคือ `K PLUS JobShield — ช่วย First Jobbers สร้างเงินสำรองอย่างต่อเนื่อง และเพิ่มการป้องกันตามความเสี่ยงเมื่อเงินสำคัญกำลังถูกโอนไปยังปลายทางภายนอก` ภายใต้ Track 3 — Cyber Security & Digital Trust ผู้ใช้เลือกหรือสร้าง Pocket ย่อยใน K-ePocket สำหรับ `เงินสำรองตั้งหลัก (Protected Reserve)` เพียงก้อนเดียว ตั้งเป้าจากค่าใช้จ่ายจำเป็น 3–6 เดือนหรือกำหนดเอง นำเงินที่มีอยู่มากันเป็นยอดเริ่มต้น และเลือกเปิดแผนออมอัตโนมัติตามจำนวน/วันที่ที่กำหนดได้ รอบที่เข้าเกณฑ์จะเพิ่ม Benefit Tier แบบ Prototype ที่ 1/3/6 เดือน ส่วนทุกการนำเงินออกจะผ่าน Savings Nudge หรือ High-Risk Security Intervention ตาม multi-signal policy Fake Recruiter ยังคงเป็น Hero Threat Scenario และ novelty อยู่ที่ `Protected Reserve + goal-aware saving plan + context-aware pre-transfer protection` ปัจจุบันยังไม่มี usability result: `0 pilot sessions conducted` และ `0 participant sessions conducted`

## Current Scope Lock — K PLUS Integration & Benefit Loop (V6)

- K-ePocket เป็นผลิตภัณฑ์เดิมที่ใช้เป็น money container; JobShield เป็น goal/benefit experience และ security policy layer ไม่ใช่บัญชีเงินฝากหรือ Pocket รูปแบบใหม่
- ถ้ามีบัญชี K-ePocket แล้ว ผู้ใช้เลือก Pocket เดิมหรือสร้าง Pocket ย่อยสำหรับ `เงินสำรองตั้งหลัก`; ถ้ายังไม่มีบัญชี ระบบนำไปเปิด K-ePocket ตามขั้นตอนทางการแล้วกลับเข้า JobShield ห้ามเรียกการเปิดบัญชีว่า One-tap
- เป้าหมายเงินสำรองคำนวณจากค่าใช้จ่ายจำเป็นต่อเดือน × 3/6 เดือนหรือกำหนดเอง และผู้ใช้เริ่มที่ศูนย์หรือเติมยอดเริ่มต้นได้
- MVP ใช้ความสามารถแบบ Schedule Transfer เป็นฐาน: ผู้ใช้เลือกจำนวนเงินคงที่และวันที่ออมรายเดือน หากกรอกเปอร์เซ็นต์ ระบบใช้เพื่อคำนวณเป็นจำนวนคงที่จากรายได้ประมาณการที่ผู้ใช้กรอก
- การตรวจเงินเดือนเข้าแบบ event-triggered, โอนตรงเข้า Pocket ย่อย, หยุดอัตโนมัติเมื่อถึงเพดาน และ API ภายในเป็น production dependencies ที่ยังไม่ยืนยันจากข้อมูลสาธารณะ
- Auto-Routing เป็น opt-in ปรับ พัก หรือปิดได้; รอบที่พัก/เงินไม่พอไม่นับเพิ่ม และใช้ Grace/Pause ได้ 1–2 รอบโดยไม่ลด Tier
- Prototype Benefit Tier ใช้รอบ Auto-Routing ที่เข้าเกณฑ์: 1 เดือน = `เริ่มต้น`, 3 เดือน = `ต่อเนื่อง`, 6 เดือน = `มั่นคง`
- รอบที่เข้าเกณฑ์ต้องโอนสำเร็จและมียอดสุทธิคงอยู่ถึงวันสรุปรอบ การถอนเงินไม่ลด Tier เดิม แต่พักการเลื่อนไประดับถัดไปจนเติมกลับถึง Checkpoint
- K Point/คูปองพาร์ตเนอร์เป็นเพียงตัวอย่าง `สิทธิประโยชน์ภายใต้เงื่อนไขธนาคาร`; ไม่ระบุคะแนน มูลค่า หรือรับรองสิทธิ และไม่ใช้ดอกเบี้ยขั้นบันไดใน MVP
- เงินสำรองไม่ใช่กระเป๋าใช้จ่าย ทุกการนำออกมี 2 user-facing routes: ไม่เข้า High-Risk combination → Mascot Savings Nudge ที่กดข้ามได้; เข้า High-Risk combination → คำเตือนจริงจัง ไม่มี Mascot และเข้าสู่ Cooling-off
- Mascot copy เป็น Draft ที่สื่อความเป็นห่วง พร้อมปุ่ม `ใช้เงินสำรอง` และ `เก็บไว้ก่อน`; เมื่อผู้ใช้ยืนยันใช้ ให้ส่งกำลังใจสั้น ๆ โดยไม่ถามซ้ำ
- High Risk ยังคงต้องมาจากหลายสัญญาณ เช่น protected reserve + ผู้รับบุคคลใหม่ + job-payment/repetition/destination risk และพัก Pending Instruction ก่อนส่งเข้าสู่ระบบโอน/PromptPay
- Core integrations คง 3 ส่วน: K-ePocket, K PLUS Transaction + Bank-side Fraud Risk และ K PLUS Security & Fraud Response
- Business Claim ใช้แบบมีเงื่อนไข: การออมต่อเนื่องอาจช่วยเพิ่มยอดเงินฝากที่มีเสถียรภาพและ Engagement ซึ่งสนับสนุนฐานเงินทุน/โอกาสสร้างคุณค่า; Benefit ยังขึ้นกับต้นทุน ความเสี่ยง กฎเกณฑ์ และ Business Approval
- Email/Link scanning และ Fraud Specialist ไม่ใช่ Core; Prototype ใช้ deterministic policy + synthetic data ไม่มี AI/ML model

## Previous Approved Scope — V5 Snapshot

รายละเอียด V5 ด้านล่างเก็บเป็นประวัติ หากขัดกับ V6 ให้ใช้ `Current Scope Lock — K PLUS Integration & Benefit Loop (V6)`

### One Continuous Reserve (V5)

- ใช้ชื่อเดียวตลอด Flow: `เงินสำรองตั้งหลัก (Protected Reserve)`
- ตัด career-stage selection, การแยกก่อน/หลังเงินเดือน และการเปลี่ยนวัตถุประสงค์หรือย้าย Pocket ออก
- ผู้ใช้ไม่ต้องมี K-ePocket มาก่อน; onboarding เสนอสร้างหรือเชื่อม Pocket เดียวแบบ One-tap
- ผู้ใช้กำหนดค่าใช้จ่ายจำเป็นต่อเดือน เป้าหมาย 3/6 เดือนหรือกำหนดเอง และยอดเริ่มต้นจากเงินที่มีอยู่
- Auto-Routing เป็น opt-in: จำนวนคงที่หรือเปอร์เซ็นต์ของเงินเข้า เปิดภายหลังได้ ปรับ พัก ปิด และหยุดเมื่อถึงเป้าหมายได้
- หากยังไม่มีรายได้ ผู้ใช้ยังใช้ JobShield และเงินสำรองตั้งหลักได้ โดย Auto-Routing อยู่สถานะยังไม่เปิดหรือรอแหล่งเงินที่ผู้ใช้กำหนด
- บัญชีตนเอง/verified biller ที่ไม่มี risk conflict ใช้ flow ปกติ; ค่าใช้จ่ายทั่วไปที่ไม่จำเป็นใช้ Savings Nudge ที่กดข้ามได้
- Fraud/Scam Intervention ต้องใช้หลายสัญญาณร่วมกัน เช่น protected reserve + ผู้รับบุคคลใหม่ + job-payment/repetition/destination risk
- Fake Recruiter ยังเป็น Hero Scenario โดยไม่ใช้สถานะงานเป็นสัญญาณ
- Core statement คือ `เงินสำรองตั้งหลักก้อนเดียว → สร้างต่อเนื่องด้วย Auto-Routing → ปกป้องด้วย Risk-based Protection`
- Core integrations ยังมี 3 ส่วนเดิม: K-ePocket, K PLUS Transaction + Bank-side Fraud Risk และ K PLUS Security & Fraud Response
- Email/Link scanning และ Fraud Specialist ไม่ใช่ Core; Prototype ใช้ deterministic rules/policy กับ synthetic data และไม่อ้างว่ามี ML model
- High-Risk Cooling-off พักเฉพาะ Pending Instruction และยอดรายการนั้นก่อนส่งเข้าสู่ระบบโอน/PromptPay

## Previous Approved Scope — V4 Snapshot

เนื้อหา V4 ด้านล่างเก็บไว้เป็น decision history เท่านั้น หากขัดกับ `Current Scope Lock — One Continuous Reserve (V5)` ให้ใช้ V5 เป็นปัจจุบัน

### Approved Scope Alignment — 6 September 2026

- Positioning ใช้วงจร `Set up → Build → Protect → Continue` โดย Auto-Routing เป็น money-management mechanism และ context-aware pre-transfer policy เป็นแกน Track 3
- `Career Mode` เดิมลดบทบาทเหลือ `career stage/context` ที่ผู้ใช้เลือกตอนเปิด JobShield: กำลังหางาน/รอเงินเดือนแรก หรือเริ่มมีรายได้แล้ว
- ช่วงก่อนรับเงินเดือนแรกใช้ protected reserve เพียงก้อนเดียวชื่อ `เงินสำรองก่อนเงินเดือนแรก`; หลังมีรายได้เปลี่ยนวัตถุประสงค์เป็น `เงินสำรองฉุกเฉิน` ที่ตั้งเป้าจากค่าใช้จ่ายจำเป็น 3–6 เดือนหรือกำหนดเอง
- เงินที่เหลือจากช่วงก่อนเงินเดือนแรกย้ายไปเริ่มเป้าหมายเงินสำรองฉุกเฉินได้เฉพาะเมื่อผู้ใช้ยืนยัน ไม่ย้ายอัตโนมัติ
- Auto-Routing เป็น opt-in ปรับ พัก ปิด และหยุดเมื่อถึงเป้าหมายได้; Prototype ใช้ user-configured/synthetic salary event
- แยก `Savings Nudge` ที่กดข้ามได้ออกจาก `Fraud/Scam Intervention` ที่ใช้ friction ตามระดับความเสี่ยง
- Fake recruiter payment เป็น Hero Threat Scenario ไม่ใช่ขอบเขตการใช้งานทั้งหมดของผลิตภัณฑ์
- K Point เป็น Future Concept ที่ต้องผ่าน Business/Product approval; ตัดดอกเบี้ยพิเศษและ claim เรื่องนำเงินลูกค้าไปลงทุนออกจาก Prototype/Proposal
- Email/Link scanning, employer network และ Fraud Specialist ยังคงเป็น Optional/Future และไม่ใช่ Core
- High-Risk Cooling-off พักเฉพาะ Pending Instruction และยอดนั้นก่อนเข้าสู่ PromptPay; ไม่ล็อกทั้งบัญชีหรือทั้ง K-ePocket
- Test Final Proposal 1 และ Diagram v3 เป็น snapshot เดิม ห้ามเขียนทับ; artifact ใหม่ต้องใช้ชื่อเวอร์ชันถัดไป

### Approved Simplification — Single Protected Reserve

- ผู้ใช้อนุมัติให้ตัด `Job Search Budget` ออกจากแนวคิดปัจจุบันเมื่อ 6 กันยายน 2026
- ก่อนรับเงินเดือนแรก ผู้ใช้นำเงินที่มีอยู่มากันไว้ใน `เงินสำรองก่อนเงินเดือนแรก` และทยอยใช้สำหรับค่าใช้ชีวิตที่จำเป็น
- หลังรับเงินเดือน ผู้ใช้ยืนยันการเปลี่ยนวัตถุประสงค์ของเงินก้อนเดิมเป็น `เงินสำรองฉุกเฉิน` หรือเลือกเริ่ม Pocket ใหม่; ระบบไม่ย้ายหรือเปลี่ยนให้เอง
- Auto-Routing เติมเงินใหม่เข้าสู่เงินสำรองฉุกเฉินตามจำนวนหรือเปอร์เซ็นต์ที่ผู้ใช้กำหนด
- Hero Scenario คือ Fake Recruiter พยายามให้ผู้ใช้ดึงเงินสำรองก่อนเงินเดือนแรกไปยังบัญชีบุคคลใหม่
- Core statement ใช้ `Protected Reserve + Auto-Routing + Risk-based Protection`
- การอ้างอิง Job Search Budget ใน Historical Scope Lock, prior PDF, Diagram v2/v3 และ research history เป็น snapshot เดิม ไม่ใช่ current scope

## Historical Scope Lock — 5 September 2026

ส่วนนี้เก็บไว้เป็น decision history เท่านั้น หากขัดกับ `Current Scope Lock — One Continuous Reserve (V5)` ให้ใช้ V5 และ Draw.io V5 เป็นปัจจุบัน

- คำเรียกมาตรฐานในภาษาไทยคือ `เงินสำรองก่อนเงินเดือนแรก` และใช้คำนี้เหมือนกันทุกเอกสาร/หน้าจอที่ใช้งานต่อจากนี้
- Core มีเพียง 3 integrations: (1) `K-ePocket` สำหรับแยกวัตถุประสงค์ของเงิน (2) `K PLUS Transaction + Bank-side Fraud Risk` สำหรับข้อมูลผู้รับ ยอด รูปแบบธุรกรรม และสัญญาณปลายทาง และ (3) `K PLUS Security & Fraud Response` สำหรับคำเตือน การยืนยันที่เข้มขึ้น Cooling-off และ Cancel/Report
- `Dynamic Time Lock` ไม่ใช่ฟีเจอร์แยก แต่เป็นกลไกภายใน `risk-based Cooling-off`
- เมื่อเป็น High Risk ระบบพักเป็น `Pending Instruction` **ก่อนส่งเข้าสู่ระบบโอน/PromptPay** เงินจึงยังไม่ถูกส่งไปยังผู้รับระหว่าง Cooling-off
- Email/Link scanning และ Fraud Specialist ไม่อยู่ใน Core; หากกล่าวถึง ให้ติดป้าย `Optional/Future integration` ชัดเจนเท่านั้น
- Prototype ปัจจุบันใช้ deterministic multi-signal rules/policy และ synthetic data; ห้ามเรียกว่าโมเดลอัจฉริยะหรืออ้างว่ามี ML model ที่ยังไม่ได้สร้าง
- FigJam อ้างอิงชุดใหม่ที่ [K PLUS JobShield — Detailed System Flow](https://www.figma.com/board/2Zucnsm9P4uPJdZ1BHVRv9); Mermaid source ใน Repository ต้องเป็น canonical source ชุดเดียวกัน
- ผู้ใช้ไม่ต้องมี K-ePocket มาก่อน; Full JobShield onboarding ต้องเสนอสร้าง/เชื่อม `Job Search Budget` และ `เงินสำรองก่อนเงินเดือนแรก` แบบ One-tap ส่วนการข้ามเหลือเพียง baseline protection
- เพิ่ม Protected Savings/Auto-Routing เป็น Supporting Prototype flow หลังได้รับเงินเดือนแรก โดยแยก `เงินสำรองฉุกเฉิน` ออกจาก `เงินสำรองก่อนเงินเดือนแรก`; Core Track 3 ยังเป็น pre-transfer JobShield policy
- Auto-Routing เป็น opt-in ปรับ/พัก/ปิดและหยุดเมื่อถึงเพดานได้; recommendation ใช้ deterministic rule ไม่ใช้คำว่า AI
- K Point และดอกเบี้ยพิเศษเป็น unconfirmed future business concepts เท่านั้น ห้ามแสดงอัตรา สิทธิ หรือผลตอบแทนเสมือนว่าได้รับอนุมัติแล้ว
- Figma canvas ยังมีโครงสร้างเดิม 31 screens; A01K/A01N และ R00–R09B อยู่ใน local Figma-ready specification และยังไม่ได้ apply เพราะ Starter MCP tool-call limit

## Clarifying Questions — Historical Decision Log

รายการด้านล่างเก็บคำตอบระหว่างการพัฒนาแนวคิดไว้เพื่อการตรวจสอบย้อนหลัง หากกล่าวถึง `Job Search Budget`, Career Mode, Stage branching หรือชื่อเงินสำรองเดิม ให้ถือว่าถูกแทนที่ด้วย `Current Scope Lock — One Continuous Reserve (V5)`

- [x] เลือก Direction A เป็นแนวคิดหลัก: JobShield สำหรับ recruitment-payment scam ต่อ First Jobbers
- [x] เลือกความเสียหายหลัก: ถูกหลอกให้โอนเงินเพื่อแลกกับการสมัครหรือเริ่มงาน
- [x] เลือกกลไกหลัก: ผู้ใช้เปิด Career Mode ล่วงหน้า; ระบบตรวจผู้รับใหม่และถามเฉพาะธุรกรรมเสี่ยง
- [x] กำหนดให้การ Share อีเมล/ลิงก์เป็น optional/future integration โดยไม่อ่านข้อความส่วนตัวอัตโนมัติ
- [x] แบ่งเงินเป็น Job Search Budget สำหรับใช้ตามแผน และ `เงินสำรองก่อนเงินเดือนแรก` สำหรับค่าใช้ชีวิตจนได้เงินเดือนแรก
- [x] ใช้ context-aware risk policy ที่รวม fund source, Career Mode และ transaction/recipient risk เพื่อเลือกระดับ intervention
- [x] ใช้ transaction signals เป็น core, destination-risk เป็น bank-side assumption และอีเมล/ลิงก์เป็น optional/future consent-based evidence
- [x] กำหนด Low = normal flow, Medium = contextual warning + deliberate confirmation, High = cooling-off + stronger verification
- [x] ใช้ limited break-glass: own account/verified biller ผ่านได้; new payee ต้อง independent verification หรือรอครบ cooling-off
- [x] กำหนด independent verification ผ่านช่องทางทางการที่ผู้ใช้หาแยกเอง; verified-employer network, automated lookup และ Fraud Specialist เป็น optional/future integrations
- [x] ใช้ multi-signal red-flag combination และตรวจยอด/ความถี่สะสม พร้อม destination-risk
- [x] ให้ self-declared purpose เป็นเพียงหนึ่ง signal และไม่เปิด model weights/thresholds ทั้งหมด
- [x] ใช้ verified payee + planned expense + Job Search Budget เป็น positive signals; trusted payee ต้องผ่านครั้งแรก
- [x] ใช้ risk-proportional cooling-off พร้อม countdown, cancel/report และ limited break-glass; ระยะจริงต้องทดสอบ
- [x] ใช้ opt-in onboarding เมื่อสร้าง Job Search Budget/เงินสำรองก่อนเงินเดือนแรก พร้อม user-defined duration, off และ auto-expiry
- [x] Primary success = contextual warning เพิ่ม comprehension + pause/cancel โดย legitimate flow ยังมี friction ที่ยอมรับได้
- [x] Failure = ไม่ดีกว่า generic warning, ผู้ใช้ไม่เข้าใจ หรือ legitimate friction ทำให้ไม่เปิดใช้
- [x] เปรียบเทียบ 4 directions และยืนยัน JobShield เป็นแนวคิดหลัก
- [x] One-page core = Career Mode + Budget/เงินสำรองก่อนเงินเดือนแรก → multi-signal transfer risk → warning/Cooling-off/Cancel-Report
- [x] ล็อก Core ให้มี 3 integrations: K-ePocket, K PLUS Transaction + Bank-side Fraud Risk และ K PLUS Security & Fraud Response
- [x] กำหนด Dynamic Time Lock เป็นส่วนหนึ่งของ risk-based Cooling-off ไม่ใช่ฟีเจอร์แยก
- [x] กำหนดให้ Cooling-off พัก Pending Instruction ก่อนส่งเข้าสู่ระบบโอน/PromptPay
- [x] Share-email/link, verified-employer network และ Fraud Specialist workflow เป็น optional/future integrations
- [x] ยืนยันทีม 2 คน
- [x] ยืนยันทักษะสมาชิกคนที่สอง: UX/UI, Figma, Research, Writing/Pitch และ Cyber Security
- [x] สมาชิกคนที่สองเป็น owner ของ user-flow prototype + visual design; ผู้สมัครหลักเป็น owner ของ threat model/risk policy
- [x] เลือกภาษาไทยเป็นหลัก โดยคง required headings และ technical terms ภาษาอังกฤษ; provisional pending form check
- [x] ตรวจยืนยัน deadline 21 กันยายน 2026 และทีมไม่เกิน 3 คนจาก KBTG official LinkedIn ณ 4 กันยายน 2026
- [x] ยืนยัน minimum guaranteed capacity รวมทั้งทีม 2 ชั่วโมง 30 นาที/วัน ทำได้ทุกวัน หรือ 17.5 ชั่วโมง/สัปดาห์
- [x] กำหนด content freeze วันที่ 18 กันยายน 2026 เพื่อเหลือ buffer 3 วันก่อน deadline
- [x] ระบุ pain point เป็น transitional job-search risk window และแยกหลักฐานออกจาก hypothesis
- [x] เลือก protected-fund intervention สำหรับ fake-recruiter payment เป็นแกนหลัก
- [x] ระบุ novelty gap เทียบ K PLUS, K-ePocket, MAKE และ anti-fraud controls ปัจจุบัน พร้อมลด claim ที่ซ้ำของเดิม
- [x] ระบุ transaction-level signals เป็น core, destination risk เป็น integration assumption และ email/link เป็น consent-based optional/future input
- [x] กำหนด actions สำหรับ Low/Medium/High พร้อม cooling-off, independent verification และ limited break-glass
- [x] ออกแบบ boundary scenarios สำหรับ false positives, warning fatigue, scammer-guided confirmation และ attacker evasion
- [x] เลือก committed prototype เป็น clickable Figma flow + synthetic risk table/scenarios
- [x] กำหนด mini rule-based coded demo เป็น stretch goalเมื่อชิ้นงานหลักเสร็จก่อน content freeze เท่านั้น; ไม่มี ML model ใน Prototype ปัจจุบัน
- [x] ยืนยันทีม ภาษา เวลาที่มี และ prototype expectation ก่อนล็อก scope
- [x] อธิบาย First Jobber specificity เป็น transitional risk window โดยไม่อ้างอัตรา victimization ที่สูงกว่ากลุ่มอื่นหากไม่มีหลักฐาน
- [x] กำหนด proposed differentiation เป็น context-aware policy ที่เชื่อม protected fund, Career Mode/job-payment context และ recipient/transaction risk ก่อน authorized transfer
- [x] กำหนด K PLUS fit จาก bank-native advantage ที่ pre-transfer authorization point พร้อม intervention และ Cancel/Report ใน flow เดียว
- [x] กำหนด final authority boundary: High Risk ต้องผ่าน cooling-off/independent verification แต่ผู้ใช้ยังทำรายการได้หลังครบเงื่อนไข; ไม่อ้างป้องกันได้ 100%
- [x] กำหนด privacy boundary ของ optional/future shared email/link ด้วย per-item consent, data minimization, declared retention และไม่นำข้อมูลไปฝึกโมเดลอัตโนมัติ
- [x] กำหนด High-Risk warning content, actions และ accessibility requirements สำหรับ Figma prototype
- [x] กำหนด formative usability test 5–8 คน เปรียบเทียบ contextual กับ generic warning ด้วย scam/legitimate tasks
- [x] กำหนด synthetic boundary suite 4 กรณี ครอบคลุม true positive, false positive, emergency path และ coached bypass
- [x] กำหนด final ownership: ผู้สมัครหลักคุม content/technical; สมาชิกคนที่สองคุม visual/prototype; cross-review ก่อน freeze
- [x] ล็อก evidence-first milestone plan รวม 35 ชั่วโมงถึง content freeze วันที่ 18 กันยายน 2026

## File And Code References

- `AGENTS.md` — โจทย์ ข้อกำหนด กระบวนการ และ design principles
- `research/sources.md` — source registry พร้อม access dates, supported claims และข้อจำกัด
- `research/user-problem.md` — หลักฐาน fake-job payment scam และ First Jobber claim boundary
- `research/competitor-gap.md` — public KBank capability matrix และ refined novelty statement
- `research/signal-feasibility.md` — bank-visible/derived signals, assumptions และ prototype boundaries
- `research/threat-model-v5.md` — current actors, assets, trust boundaries, attack paths, controls และ residual risks
- `research/synthetic-risk-table-v5.md` — current deterministic rule precedence, boundary cases และ acceptance criteria
- `proposal/content-skeleton.md` — โครงเนื้อหาห้าส่วนและ three-step visual map; ไม่ใช่ final Proposal
- `proposal/Test_ Final-Proposal-1.pdf` — one-page test Final Proposal; A4, one page, rendered and visually inspected on 5 September 2026
- `proposal/generate_test_final_proposal_1.py` — reproducible source for the test PDF
- `prototype/technical-visual-cross-review.md` — consistency review, issue resolutions และ Figma constraints
- `prototype/figma-flow-spec-v5.md` — current frame inventory, components, interaction map และ clickable build checklist
- `prototype/figma-scope-sync-v5.md` — current screen-copy patch และ verification checklist ที่ยังรอลง Figma canvas
- `research/formative-usability-test-plan.md` — consent, counterbalanced tasks, measures, observation/synthesis templates และ decision rules
- `research/phase-a-research-plan.md` — facts, hypotheses, research workstreams และ milestone status

## Candidate Direction Comparison

| Direction | First Jobber specificity | Money/saving fit | Track 3 fit | Duplication/dependency risk | Demo story |
|---|---|---|---|---|---|
| A. JobShield: recruitment-payment protection + protected reserve | สูง | สูง | สูง | ปานกลาง: ต้องพิสูจน์ JobShield adoption และ verification integration | ชัดและเฉพาะเจาะจง |
| B. SafeStart: protected savings + scam intervention ทั่วไป | ปานกลาง | สูง | สูง | สูง: เสี่ยงซ้ำ pocket และ transaction warning เดิม | กว้างและอธิบายยากกว่า |
| C. MuleGuard: recipient/graph risk ก่อนโอน | ต่ำ–ปานกลาง | ต่ำ | สูง | สูง: KBank ระบุว่ามี suspicious-destination detection และต้องพึ่ง internal graph data | เทคนิคเด่นแต่โจทย์ออมอ่อน |
| D. Recruitment PhishScan: สแกนอีเมล/ลิงก์ปลอม | สูง | ต่ำ | สูง | สูง: generic scanner, cross-app visibility และ privacy | เข้าใจง่ายแต่ K PLUS fit อ่อน |

คำตัดสิน: Direction A เพราะเชื่อม target, money-management และ pre-loss security ได้สมดุลที่สุด โดยใช้ transaction-level core ลดข้อจำกัด cross-app ของ Direction D

## Proposed Differentiation

JobShield ไม่อ้างว่า pocket, Auto-Routing, fraud detection หรือ warning เป็นองค์ประกอบใหม่โดยลำพัง ความแตกต่างที่เสนอคือการเชื่อม `เงินสำรองตั้งหลัก + user-controlled Auto-Routing + job-payment/recipient/transaction risk` เข้าเป็น context-aware security policy ซึ่งปรับ intervention ก่อนผู้ใช้ยืนยัน authorized transfer ภายใต้ social engineering

Claim boundary: ใช้คำว่า proposed differentiation จนกว่าจะตรวจ capability ล่าสุดของ K PLUS, K-ePocket, MAKE by KBank และมาตรการ anti-fraud ทางการครบถ้วน ห้ามใช้คำว่า first, unique หรือ KBank ยังไม่มีโดยไม่มีหลักฐานโดยตรง

## Why K PLUS

K PLUS อยู่ที่จุดก่อนเงินออกและสามารถเชื่อม fund source, payee และ transaction context ที่จำเป็นกับ risk-based intervention รวมถึง Cancel/Report ภายใน transaction flow เดียว นี่คือ bank-native advantage เหนือ standalone email/link checker ซึ่งไม่มีทั้ง transaction visibility และ intervention capability ครบถ้วน ทั้งนี้ prototype จะจำลอง destination/network risk เป็น integration assumption เท่านั้นและไม่อ้างการเข้าถึง KBank internal data

## User Authority And Safety Boundary

- High-Risk transfer ต้องผ่าน risk-based cooling-off และ independent verification ตาม policy ที่กำหนด
- หากไม่มีเหตุระงับตามกฎธนาคารอื่นและผู้ใช้รอครบเวลาพร้อมยืนยันอีกครั้ง ผู้ใช้ยังมีสิทธิดำเนินธุรกรรม
- ระบบมี Cancel/Report และ audit trail เพื่อช่วยการตอบสนองต่อเหตุ แต่ไม่อ้างว่าจะหยุด Scam ได้ทุกกรณี
- ห้ามอ้าง permanent blocking, guaranteed prevention หรือ guaranteed reimbursement

## Privacy Boundary

- การ Share อีเมลหรือลิงก์เป็น optional/future input ไม่ใช่ Core และต้องขอ explicit consent รายครั้ง
- วิเคราะห์เฉพาะรายการที่ผู้ใช้เลือกส่ง พร้อมเปิดเผยประเภทข้อมูลหรือ indicators ที่นำมาใช้
- เก็บเฉพาะ indicators และ audit data ที่จำเป็นตาม retention period ที่แจ้ง; ระยะเวลาจริงเป็น policy/legal design item ที่ห้ามสร้างตัวเลขเอง
- ไม่นำเนื้อหาไปฝึกโมเดลโดยอัตโนมัติ และ transaction-based core ต้องทำงานได้โดยไม่อ่าน inbox

## High-Risk Warning UX

- ใช้ plain Thai ที่สั้น ชัด และไม่ตำหนิผู้ใช้
- แสดง observable reasons 2–3 ข้อและจำนวน `เงินสำรองตั้งหลัก` ที่กำลังเสี่ยง โดยไม่เปิดกฎและ thresholds ทั้งหมด
- Primary actions คือ `Pause & Verify` และ `Cancel/Report`; รายละเอียดเชิงเทคนิคอยู่ใน `Learn more`
- ไม่ใช้ risk score ที่อธิบายไม่ได้และไม่กล่าวยืนยันว่าผู้รับเป็นมิจฉาชีพ
- ใช้สีร่วมกับข้อความ/ไอคอน ไม่พึ่งสีอย่างเดียว และออกแบบรองรับ text scaling กับ screen reader

## Formative Evaluation

- ผู้เข้าร่วมเป้าหมาย 5–8 คนที่เป็น First Jobbers หรือใกล้เคียงกลุ่มเป้าหมาย โดยบันทึกจำนวนและคุณสมบัติจริง
- ใช้ synthetic scam และ legitimate tasks เปรียบเทียบ contextual JobShield warning กับ generic warning
- วัด warning comprehension, การเลือก `Pause/Cancel`, legitimate task completion และ task time
- รายงานผลเป็น exploratory/formative evidence เท่านั้น ไม่อนุมานแทนประชากรและไม่อ้าง real-world loss reduction
- หากรับสมัครได้น้อยกว่า 5 คน ให้รายงานจำนวนจริงและ limitation พร้อมเสริม heuristic review ห้ามแต่ง sample size หรือผลลัพธ์

## Synthetic Boundary Scenarios

1. Fake recruiter ขอให้โอนไป new personal payee โดยดึงเงินจาก `เงินสำรองตั้งหลัก`
2. ค่าใช้ชีวิตที่ถูกต้อง จ่ายจากเงินสำรองตั้งหลักไป verified biller โดยไม่มี High-Risk warning
3. เหตุฉุกเฉินที่ใช้เงินสำรองตั้งหลักไปบัญชีตนเองหรือ verified biller ผ่าน normal/limited break-glass path
4. การใช้เงินสำรองตั้งหลักกับผู้รับเดิมและไม่มี Fraud signal แสดง Savings Nudge ที่กดข้ามได้ ไม่สร้าง Cooling-off
5. Attacker-coached bypass เช่น แบ่งยอดโอนหรือบอกให้ผู้ใช้ตอบ purpose ผิด โดย multi-signal policy ยังประเมินยอดสะสม แหล่งเงิน ผู้รับใหม่ และ destination risk

Risk table ต้องมีครบทั้งห้ากรณี ส่วน Figma usability flow เน้น Hero, legitimate, emergency และ Savings Nudge; กรณี coached bypass เป็น adversarial policy test และไม่ต้องสร้างหน้าจอสำหรับทุก permutation

## Ownership

- ผู้สมัครหลัก: final content editor และ technical owner สำหรับ problem framing, evidence/claim boundaries, threat model และ risk policy
- สมาชิกคนที่สอง: final visual และ prototype owner สำหรับ Figma user flow และ visual consistency
- ทั้งคู่: evidence research, formative testing และ cross-review ก่อน content freeze โดย final decision ต่อ artifact ยังคงอยู่กับ owner ที่ระบุ

## Timeline And Capacity

Committed capacity รวมทีม 35 ชั่วโมงก่อน content freeze:

- 4–7 กันยายน: evidence และ novelty review — 7 ชั่วโมง
- 8–11 กันยายน: threat model, synthetic risk table และ content skeleton — 6 ชั่วโมง
- 10–14 กันยายน: clickable Figma user flow — 8 ชั่วโมง
- 15–16 กันยายน: formative usability testing และ synthesis — 6 ชั่วโมง
- 17–18 กันยายน: one-page integration และ cross-review — 8 ชั่วโมง
- 19–20 กันยายน: render PDF และ visual/content QA buffer; ห้ามเพิ่ม feature ใหม่
- 21 กันยายน: ส่งเฉพาะหลังผู้ใช้ตรวจและอนุมัติ final artifact

Mini rule-based coded demo ไม่อยู่ใน committed 35 ชั่วโมงและเปิดเป็น stretch goal ได้เมื่อ evidence, risk policy, Figma flow, testing และ one-page integration ผ่าน review แล้วเท่านั้น

## Conditional Research Gates

JobShield จะถูกล็อกสำหรับ Proposal เมื่อผ่านสามเงื่อนไขต่อไปนี้:

1. พบ authoritative evidence ว่า fake-job/recruitment scam ที่เรียกเก็บเงินเพื่อสมัครหรือเริ่มงานเป็นภัยจริง
2. ตรวจ public K PLUS, K-ePocket, MAKE by KBank และ KBank anti-fraud capabilities แล้วไม่พบ end-to-end policy ที่ซ้ำกับ core อย่างมีนัยสำคัญ
3. ยืนยันว่า transaction-based core ใช้ bank-visible signals ได้ โดยข้อมูล destination/network risk ที่เข้าถึงไม่ได้สามารถแยกเป็น explicit integration assumption โดยไม่ทำให้ core ล้ม

หากไม่มี comparative evidence ว่า First Jobbers มี victimization rate สูงกว่ากลุ่มอื่น ให้ถอนหรือลด claim ดังกล่าว แต่ยังใช้ transitional-risk rationale ได้ Pivot เมื่อพบ substantial core duplication หรือพบว่า core ต้องพึ่งข้อมูลที่ทีมไม่มีจนไม่สามารถสาธิตอย่างน่าเชื่อถือ

### Gate Results — 4 September 2026

1. **Gate 1 — PASS WITH CLAIM LIMITS:** แหล่งทางการไทยยืนยัน fake-job/recruitment-payment scam แต่ไม่พบ comparative evidence ว่า First Jobbers 22–30 เสี่ยงกว่ากลุ่มอื่น จึงใช้ transitional-risk context เป็น hypothesis และไม่ใช้ prevalence claim
2. **Gate 2 — PASS WITH MATERIAL NARROWING:** ไม่พบ public end-to-end flow ที่รวม protected source-of-funds + user-controlled Auto-Routing + recruitment/transaction context + adaptive pre-transfer action แต่แทบทุก primitive มีอยู่แล้ว Novelty จึงอยู่ที่ orchestration/policy เท่านั้น และต้องเรียกว่า proposed differentiation based on reviewed public sources
3. **Gate 3 — PASS FOR CONCEPT/PROTOTYPE:** core ใช้ app state และ transaction-derived signals ได้โดยไม่อ่านข้อความส่วนตัว; destination-risk ใช้ simulated bank-side flag ส่วน recipient legal type, verified-employer network, registry automation, fraud graph และ cooling-off authority เป็น assumptions/future integrations

หลักฐานและขอบเขตอยู่ที่ `research/user-problem.md`, `research/competitor-gap.md`, `research/signal-feasibility.md` และ `research/sources.md`

## First Jobber Rationale

- Evidence-backed layer ที่พบแล้ว: รูปแบบ fake-job/recruitment scam และการเรียกเก็บเงินเพื่อสมัครหรือเริ่มงาน
- Hypothesis layer ที่ต้องตรวจสอบ: First Jobbers อาจส่งใบสมัครหลายแห่ง คาดหวังการติดต่อจากผู้ส่งที่ไม่รู้จัก ถูกกดดันให้ตอบสนองเร็ว และมีเงินสำรองช่วงเปลี่ยนผ่านจำกัด
- Claim boundary: ห้ามเขียนว่า First Jobbers ถูกหลอกมากกว่ากลุ่มอื่นหรือมีลักษณะดังกล่าวทุกคน หากไม่มี comparative evidence โดยตรง
- Product implication: `เงินสำรองตั้งหลัก` และ Fake Recruiter hero scenario ตอบบริบทของ First Jobbers โดยไม่ต้องถามสถานะงาน และไม่ได้ตั้งอยู่บนสมมติฐานว่าผู้ใช้ขาดความรู้หรือความระมัดระวัง

## Plan Todos

- [x] ใช้ `$grill-me` เลือก user/scam scenario ที่แคบและมีเหตุผล
- [x] วิจัยหลักฐาน First Jobber และ Scam/Fraud ที่สัมพันธ์กับ scenario พร้อมบันทึก claim limits
- [x] ตรวจ capability/novelty gap ของ KBank จากแหล่งทางการล่าสุด
- [x] แยก bank-visible/derived signals ออกจาก simulated และ future integration assumptions
- [x] สร้าง decision matrix เปรียบเทียบอย่างน้อย 3 directions
- [x] เลือก minimum viable security control และระบุ non-goals
- [x] ทำ threat/failure/privacy review ระดับ concept
- [x] สรุปแนวคิดที่เลือก เหตุผล ทางเลือกที่ตัด และเงื่อนไขที่ทำให้ต้องเปลี่ยนแนว
- [x] ผ่าน research gates แบบมี scope refinement; ยังไม่เริ่ม final Proposal ตามคำสั่งผู้ใช้
- [x] สร้าง threat model สำหรับ authorized transfer under fake-recruiter social engineering
- [x] สร้าง deterministic synthetic risk table ครบ true positive, legitimate payment, emergency และ coached bypass
- [x] สร้าง non-final content skeleton ครบห้าหัวข้อบังคับ พร้อม claim/assumption boundaries
- [x] ทำ technical/visual cross-review ระดับ specification และแก้ terminology/control conflicts
- [x] จัดทำ Figma-ready frame/component/interaction specification พร้อม build checklist
- [x] จัดทำ formative usability protocol, facilitator script, observation และ synthesis templates
- [x] แปลง three-step flow + BC1-A/BC2/BC3 และ Generic/Contextual test variants เป็น clickable Figma prototype
- [x] Sync scope และคำเรียกมาตรฐานใน Project plan, research notes, content skeleton, Figma spec และ Mermaid source เข้ากับ FigJam ชุดใหม่
- [x] สร้าง `Test_ Final-Proposal-1.pdf` ตามคำสั่งผู้ใช้และตรวจยืนยันว่าเป็น A4 หนึ่งหน้า ฟอนต์ไทยอ่านได้ และมีหัวข้อบังคับครบห้าส่วน
- [ ] Sync ข้อความชุดเดียวกันลง Figma canvas และตรวจภาพจริง; ยังทำไม่ได้ในรอบนี้เพราะ Figma Starter MCP limit
- [ ] Pilot clickable prototype 1 คน แล้วแก้ critical flow defects
- [ ] รับสมัครและทำ formative usability test กับผู้เข้าร่วมจริง 5–8 คน
- [ ] สรุปผลจริงและตัดสิน continue/revise/pivot ก่อนเริ่ม final Proposal

## Grill-Me Outcome

- Transcript: `tmp/grill-me/session-kbtg-track3-concept-2026-09-03-20260903-224142.md`
- Finalized outcome: `tmp/grill-me/outcome-kbtg-track3-concept-2026-09-03-20260903-224142.md`
- Outcome: Completed — conditional concept lock after 36 questions
- Summary: ยืนยัน JobShield, one-page core, Track 3 mechanism, privacy/autonomy/failure boundaries, team ownership, language, deadline, capacity และ prototype/testing scope แล้ว; research gates ผ่านแบบลด claim และแยก existing capability/proposed layer/future assumptions เรียบร้อย โดย final Proposal ยังไม่เริ่ม

## Build From Plan

- Figma target: [K PLUS JobShield — Clickable Prototype](https://www.figma.com/design/5uoF2s6cq2JMGRFfwmdpc2) ใน Drafts ของ `Re: Verse's team`
- FigJam diagrams: [K PLUS JobShield — Detailed System Flow](https://www.figma.com/board/2Zucnsm9P4uPJdZ1BHVRv9); editable Mermaid source อยู่ที่ `prototype/jobshield-diagrams.md`
- Completed todos: plugin connection, new-file creation, cover/foundations, 31-screen clickable flow, 44/44 reaction audit, 10 testing start points และ formative usability test kit
- Partial QA: prior Figma canvas ผ่านเพียง visual spot-check บางหน้า; V5 ยังต้องลงตาม `prototype/figma-scope-sync-v5.md` และให้ visual owner ตรวจ H05/H06, warning variants, contrast, text scaling และ focus order
- Visual-owner handoff: ใช้ `prototype/visual-owner-review.md`; automated pre-check ไม่ใช่ human sign-off และยังห้ามระบุ `READY FOR PILOT`
- Blocking dependencies: ต้องมี human visual-owner sign-off และ pilot participant จริง 1 คนก่อน sessions จริง 5–8 คน; ขณะนี้ `0 pilot sessions conducted` และ `0 participant sessions conducted`
- Next selected todos: visual-owner QA → pilot 1 คน → แก้ Critical/High defects → sessions 5–8 คน → synthesize actual findings
- Execution notes: ใช้ BC1-A เป็น hero scenario, BC2/BC3 ทดสอบ friction และ BC4 ทดสอบ evasion; ห้ามกำหนด Cooling-off duration, production risk score หรือผลทดสอบขึ้นเอง; High-Risk flow ต้องแสดงว่า Pending Instruction ยังไม่ถูกส่งเข้าสู่ระบบโอน/PromptPay

## Validation

- มีการเปรียบเทียบอย่างน้อย 3 directions ด้วยเกณฑ์เดียวกัน
- แนวคิดที่เลือกเชื่อมทั้งการจัดการเงิน/การออมและ pre-loss Scam/Fraud protection
- อธิบาย Track 3 mechanism, data assumptions, abuse/failure cases และ user autonomy ได้
- novelty claim ย้อนกลับไปยังหลักฐานทางการล่าสุดได้
- prototype และ metrics ไม่พึ่งข้อมูลลูกค้าจริงหรือ KBank internal API ที่ไม่ได้รับ

## Risks

- กลายเป็น budgeting feature ที่มี warning แปะเพิ่ม จน Track 3 ไม่ชัด
- ซ้ำกับ saving pocket, suspicious-account checker หรือมาตรการ KBank เดิม
- หากอธิบาย JobShield เป็นเพียง pocket ใหม่หรือ fraud warning ใหม่ กรรมการสามารถสรุปได้ทันทีว่าเป็นการรวมฟีเจอร์เดิมโดยไม่มี security-policy innovation
- สมมติว่ามีข้อมูลภายใน/สิทธิ์ชะลอธุรกรรมโดยไม่มีหลักฐาน
- หากอธิบายข้อได้เปรียบเพียงว่าเป็นแบรนด์ธนาคารที่น่าเชื่อถือ โดยไม่ชี้ transaction visibility และ control point จะตอบไม่ได้ว่าทำไมต้องสร้างใน K PLUS
- false positives และ friction ทำให้ผู้ใช้ปิดหรือข้ามการป้องกัน
- ไม่มีหลักฐานว่า pain point หรือ scenario เฉพาะกับ First Jobbers
- หากเปลี่ยน transitional-risk hypotheses ให้เป็นข้อเท็จจริงโดยไม่มีหลักฐาน Proposal จะดูตีตรากลุ่มเป้าหมายและถูกกรรมการทักเรื่อง evidence ได้
- จุดเริ่มโจมตีอยู่ในอีเมล/เว็บภายนอก ทำให้ K PLUS มองไม่เห็นเหตุการณ์หากไม่มี explicit share/consent หรือจนกว่าจะเกิดธุรกรรม
- การสแกนอีเมลอัตโนมัติเสี่ยงต่อ privacy, platform permissions และความไว้วางใจ
- หาก optional sharing ไม่มี consent รายครั้งและ retention boundary จะทำให้ฟีเจอร์ป้องกัน Scam กลายเป็นความเสี่ยงด้าน privacy/digital trust เอง
- หาก warning ใช้คะแนนลึกลับ ภาษาตำหนิ หรือข้อความยาว ผู้ใช้อาจไม่เข้าใจหรือกดยืนยันผ่านภายใต้แรงกดดัน และ prototype จะไม่พิสูจน์ explainability
- ผู้ทดสอบ 5–8 คนไม่รองรับ statistical/general population claim และอาจเกิด learning/order effect จึงต้องระบุว่าเป็น formative study และจัดลำดับ scenario อย่างระมัดระวัง
- หาก synthetic scenarios มีเฉพาะ Scam ที่ชัดเจน ผลทดสอบจะไม่เปิดเผย false positives, emergency harm หรือช่องทาง evasion และไม่เพียงพอสำหรับ Track 3 review
- หากเหลือเพียง URL/domain check จะกลายเป็น generic link scanner และเชื่อมกับการจัดการเงิน/เงินออมไม่พอ
- JobShield อาจมี adoption ต่ำเพราะผู้ใช้ที่ไม่คิดว่าตนเสี่ยงอาจไม่เปิดใช้งาน ต้องออกแบบ onboarding/value ให้คุ้มกับ friction
- หากอธิบายเงินสำรองตั้งหลักเป็นเพียง Pocket ออมเงินอีกใบ แนวคิดจะซ้ำกับ K-ePocket/MAKE ได้ง่าย; ความต่างต้องอยู่ที่ Auto-Routing journey และ risk-based pre-transfer policy
- Risk policy จะไม่ credible หากไม่แยกสัญญาณที่ K PLUS เห็นได้โดยตรงออกจากข้อมูล fraud network ภายในที่เป็นเพียง integration assumption
- หาก risk score ทุกระดับลงท้ายด้วย pop-up แบบเดียว ระบบจะไม่ใช่ risk-based control และจะเกิด warning fatigue
- Face scan หรือการกดยืนยันซ้ำเพียงอย่างเดียวพิสูจน์ได้แค่ว่าเจ้าของบัญชีเป็นผู้ทำรายการ ไม่ได้พิสูจน์ว่าเจ้าของบัญชีไม่ได้กำลังถูก social engineering
- หากใช้เบอร์โทร เว็บไซต์ หรือลิงก์จากข้อความต้องสงสัยเป็นช่องทางตรวจสอบ ผู้ใช้จะถูกส่งกลับไปยืนยันกับมิจฉาชีพคนเดิม
- การพึ่งยอดเงินขั้นต่ำเพียงอย่างเดียวเปิดช่องให้มิจฉาชีพแบ่งธุรกรรมเป็นยอดเล็กหลายครั้ง
- หากใช้คำตอบของผู้ใช้ว่า “เกี่ยวกับงานหรือไม่” เป็นสวิตช์ตัดสินหลัก มิจฉาชีพสามารถ coach ให้เลือกคำตอบอื่นและลดความเสี่ยงเทียมได้
- การเตือนค่าสอบ ใบรับรอง หรือบริการสมัครงานที่ถูกต้องทุกครั้งจะทำให้เกิด warning fatigue และลด adoption ของ JobShield
- Cooling-off ที่สั้นหรือง่ายต่อการ bypass จะไม่หยุดผู้ใช้ที่กำลังถูกกดดัน แต่ถ้ายาวแบบตายตัวอาจกระทบค่าใช้จ่ายจำเป็นและโอกาสงานที่ถูกต้อง
- แม้มีหลายขั้น ผู้ใช้ที่ยังเชื่อมิจฉาชีพหลังครบ cooling-off อาจยืนยันต่อได้ จึงต้องวัด risk reduction และ comprehension แทนการอ้าง complete prevention
- หาก JobShield ซ่อนอยู่ใน settings ผู้ใช้เสี่ยงไม่พบ แต่หากเปิดให้อัตโนมัติตามอายุหรือพฤติกรรม ระบบอาจสร้างความรู้สึกถูกเฝ้าดูและผิดพลาดเรื่องสถานะการทำงาน
- Prototype ที่แสดงเพียงหน้าจอและ risk score จะไม่พิสูจน์ว่า contextual intervention ช่วยการตัดสินใจหรือรักษา usability ของธุรกรรมปกติ
- หากไม่กำหนด failure condition ทีมอาจเลือกตีความผลทดสอบทุกแบบว่าแนวคิดสำเร็จและไม่ยอมตัด scope ที่อ่อน
- บทเรียนจาก scope เดิมคือ หากใส่หลายกระเป๋า, Stage branching, link scan, employer network, risk engine และ Fraud Specialist เป็น Core พร้อมกัน Proposal หนึ่งหน้าจะกลายเป็น feature bundle; V5 จึงเหลือเงินสำรองตั้งหลักก้อนเดียวและ 3 integrations
- Scope ที่วางไว้ต้องทำได้แม้ทีมเล็ก; ห้ามแจกบทบาทหรืออ้างความสามารถสมาชิกที่ยังไม่ได้ยืนยัน
- แม้สมาชิกคนที่สองทำได้หลายด้าน แต่ถ้าไม่มี primary owner ต่อ deliverable งานอาจซ้ำกันและไม่มีผู้รับผิดชอบปิดคุณภาพขั้นสุดท้าย
- หาก content owner และ visual owner ไม่ cross-review ก่อน freeze Proposal กับ Figma อาจใช้คำ นิยามระดับความเสี่ยง หรือ user flow ไม่ตรงกัน
- หากทำ coded prototype หรือ ML model เกินจำเป็น อาจเบียดเวลาวิจัย ตรวจ novelty ทดสอบ user flow และขัดเกลา one-page proposal ก่อน content freeze
- หากใช้ QA buffer วันที่ 19–20 กันยายนเพิ่ม scope แทนแก้ overflow, Thai font, citations และความสอดคล้อง จะเสีย buffer ก่อนวันส่ง

## Approval

- Status: V5 continuous-reserve repository scope and Draw.io are synced; existing 31-screen Figma canvas remains a prior snapshot and still needs the V5 patch plus human visual QA; `0 pilot sessions conducted`; `0 participant sessions conducted`; Test Final Proposal 1 remains an earlier snapshot and is not approved for submission
