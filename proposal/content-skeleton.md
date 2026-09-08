# K PLUS JobShield — Non-Final One-Page Content Skeleton

สถานะ: Working content architecture; V6 K PLUS integration + Benefit Loop scope synced — 6 กันยายน 2026
คำเตือน: ไฟล์นี้ **ไม่ใช่ final Proposal**, ไม่ใช่ copy ที่อนุมัติ และยังไม่ใช่ PDF  
ภาษา: ภาษาไทยเป็นหลัก โดยคง required section headings และ technical terms ภาษาอังกฤษ

## Current Scope Lock

- ใช้ชื่อเดียวตลอด Flow: `เงินสำรองตั้งหลัก (Protected Reserve)`
- ไม่มี career-stage selection และไม่มีการเปลี่ยนชื่อ ย้าย หรือสร้าง Pocket ใหม่เมื่อสถานะงานเปลี่ยน
- Core มี 3 integrations: K-ePocket, K PLUS Transaction + Bank-side Fraud Risk และ K PLUS Security & Fraud Response
- `Dynamic Time Lock` เป็นส่วนหนึ่งของ risk-based Cooling-off; High-Risk flow พัก Pending Instruction ก่อนส่งเข้าสู่ระบบโอน/PromptPay
- Email/Link scanning และ Fraud Specialist เป็น Optional/Future integration ไม่ใช่ Core
- Prototype ใช้ rules/policy กับ synthetic data และไม่มี ML model; ห้ามนำเสนอว่าเป็นโมเดลตรวจจับที่สร้างเสร็จแล้ว
- วงจรผลิตภัณฑ์คือ `Set up → Auto-save & Benefit → Protect → Continue`; แผนออมอัตโนมัติสนับสนุนโจทย์บริหารเงิน ส่วน pre-transfer policy เป็นแกน Track 3
- JobShield ไม่ถามหรืออนุมานว่าผู้ใช้มีงานหรือได้รับเงินเดือนแล้วหรือยัง
- K Point/คูปองพาร์ตเนอร์แสดงได้เฉพาะตัวอย่าง Benefit ที่ต้องผ่าน Business Approval; ไม่ระบุคะแนน มูลค่า หรือรับรองสิทธิ และไม่มีดอกเบี้ยขั้นบันไดใน MVP
- ใช้ protected reserve ก้อนเดียวต่อเนื่อง; ผู้ใช้เติมเงินเริ่มต้นเองและเปิดแผนออมตามจำนวนคงที่/วันที่กำหนดตอนนี้หรือภายหลังได้
- Schedule Transfer เป็น existing mechanism ที่นำมาใช้เป็นฐานของ MVP; salary-event trigger, direct sub-pocket routing และ stop-at-cap API ยังเป็น internal assumptions
- Benefit Tier เป็น Prototype Rule ตามรอบที่เข้าเกณฑ์: 1 เดือน = เริ่มต้น, 3 เดือน = ต่อเนื่อง, 6 เดือน = มั่นคง พร้อม Grace/Pause 1–2 รอบ
- ทุกการนำเงินออกแบ่งเป็น 2 เส้นทาง: ไม่เข้า High-Risk combination → Mascot Savings Nudge ที่กดข้ามได้; เข้า High-Risk combination → serious warning + Cooling-off โดยไม่มี Mascot

## 1. Page-Level Message

### Working title

`K PLUS JobShield`

### Working descriptor

`ออมอัตโนมัติให้ต่อเนื่อง รับ Benefit ตามระยะทาง และเพิ่มเกราะก่อนเงินออก`

### Working value proposition — not final copy

`K PLUS JobShield ช่วย First Jobbers สร้างเงินสำรองอย่างต่อเนื่องผ่าน K-ePocket พร้อม Benefit Tier จากวินัยการออม และใช้บริบทของเงินร่วมกับสัญญาณธุรกรรมเพื่อป้องกันก่อนโอน`

ข้อควรระวัง: อย่าใช้คำว่า `first`, `unique`, `ป้องกันได้ทั้งหมด` หรือ `KBank ยังไม่มี` ในข้อความ final

## 2. Evidence Labels For Drafting

- **[FACT]:** แหล่งทางการรองรับโดยตรงและบันทึกใน `research/sources.md`
- **[PROPOSED]:** พฤติกรรมหรือ control ที่ JobShield เสนอ
- **[HYPOTHESIS]:** ต้องทดสอบกับผู้ใช้หรือข้อมูลเพิ่ม
- **[ASSUMPTION]:** ต้องพึ่ง capability/authority ที่ยังไม่ยืนยันจาก public sources

Label เหล่านี้ใช้ใน skeleton เท่านั้น และจะไม่ใส่ทั้งหมดลงหน้า final

## 3. Recommended Page Hierarchy

| Page zone | สัดส่วนโดยประมาณ | หน้าที่ |
|---|---:|---|
| Title + one-line value proposition | 12–15% | ทำให้เข้าใจผู้ใช้ ความเสี่ยง และจังหวะ intervention ภายในไม่กี่วินาที |
| Problem Statement + Target Users | 20–25% | ระบุ fake-job payment moment โดยไม่เหมารวม First Jobbers |
| Proposed Solution — three-step flow | 35–40% | แสดง end-to-end flow และ novelty ที่ policy |
| Value Proposition + Track Perspective | 20–25% | แยก user/K PLUS value และอธิบาย defense in depth |
| Evidence/assumption footer | 5–8% | อ้างแหล่งหลักและเปิดเผย prototype assumption แบบสั้น |

หนึ่งหน้าควรมีภาพ flow หลักเพียงหนึ่งชุดและ warning mockup หนึ่งภาพ ไม่ใส่ risk table เต็มลง Proposal

## 4. Required Section Skeleton

### Problem Statement

เป้าหมายข้อความ: 45–60 คำภาษาไทย

- **[FACT]** ผู้รับสมัครงานปลอมอาจแอบอ้างบริษัทและเรียกค่าสมัคร ค่าเริ่มงาน ค่าอุปกรณ์ หรือเงินประกันก่อนเริ่มงาน
- **[FACT]** เมื่อเจ้าของบัญชีเป็นผู้สั่งโอนเอง authentication ยืนยันตัวผู้ทำรายการ แต่ไม่ได้ยืนยันว่า decision ปราศจาก social engineering
- **[HYPOTHESIS]** ช่วงหางาน รอเงินเดือนแรก และเริ่มสร้างเงินสำรองเป็นช่วงที่เงินก้อนจำกัดมีความสำคัญต่อค่าใช้ชีวิต
- จบด้วย design gap: การแบ่ง Pocket หรือคำเตือนทั่วไปเพียงอย่างเดียวไม่ได้เชื่อม `protected fund source + transaction context + destination risk` เพื่อปกป้องเงิน ณ decision point

ห้ามเขียน:

- First Jobbers ถูกหลอกมากกว่ากลุ่มอื่น
- ผู้สมัครงานทุกคนรีบกดลิงก์หรือไม่ระมัดระวัง
- ตัวเลข task-scam ทั้งหมดคือความเสียหายจาก fake recruiter หลังส่ง Resume

### Target Users

เป้าหมายข้อความ: 25–35 คำภาษาไทย

- First Jobbers อายุ 22–30 ที่กำลังสมัครงาน รอเงินเดือนแรก หรือเริ่มมีรายได้และต้องการสร้างเงินสำรอง
- เน้นผู้ใช้ที่เลือกเปิด JobShield เอง โดยระบบไม่ infer สถานะงานจากอายุ อีเมล หรือพฤติกรรม
- ปัญหาเฉพาะคือ transitional job-search context ไม่ใช่การตีตราว่ากลุ่มนี้มีความรู้ต่ำ

### Proposed Solution

เป้าหมาย: three-step flow รวมประมาณ 90–120 คำ

#### Step 1 — Set up: ตั้งเป้าหมายเงินสำรอง

- **[REUSE]** ผู้ใช้เลือก Pocket เดิมหรือสร้าง Pocket ย่อยใน K-ePocket สำหรับ `เงินสำรองตั้งหลัก`; หากยังไม่มีบัญชี ให้ผ่านขั้นตอนเปิด K-ePocket ทางการก่อนกลับเข้า JobShield
- **[PROPOSED]** ผู้ใช้กรอกค่าใช้จ่ายจำเป็นต่อเดือน เลือกเป้าหมาย 3/6 เดือนหรือกำหนดเอง และนำเงินที่มีอยู่มากันเป็นยอดเริ่มต้น
- ห้ามกล่าวว่าการเปิดบัญชี K-ePocket เป็น One-tap

#### Step 2 — Auto-save & Benefit: ออมต่อเนื่องโดยไม่ต้องจำทุกเดือน

- **[REUSE]** ใช้กลไก Schedule Transfer เป็นฐาน ให้ผู้ใช้กำหนดจำนวนคงที่และวันที่ออมรายเดือน; หากกรอกเปอร์เซ็นต์ ให้คำนวณเป็นจำนวนคงที่จากรายได้ประมาณการ
- **[PROPOSED]** รอบที่โอนสำเร็จและมียอดสุทธิคงอยู่ถึง Checkpoint จะเพิ่ม Progress ไปยัง Tier เริ่มต้น/ต่อเนื่อง/มั่นคงที่ 1/3/6 เดือน
- Grace/Pause 1–2 รอบไม่ลด Tier และไม่นับ Progress เพิ่ม การถอนเงินไม่ลด Tier เดิมแต่พักการเลื่อนระดับจนเติมกลับถึง Checkpoint
- **[ASSUMPTION]** K Point/คูปองเป็นตัวอย่างสิทธิภายใต้เงื่อนไขธนาคาร ไม่ใช่สิทธิที่รับรองแล้ว

#### Step 3 — Protect & Continue: ปกป้องทุกครั้งก่อนนำเงินสำรองออก

- **[PROPOSED]** policy รวม protected fund source, first-seen payee, repeated/cumulative transfers, job-payment context และ simulated destination risk
- ไม่เข้า High-Risk combination: Mascot เตือนด้วยความเป็นห่วง พร้อม `ใช้เงินสำรอง` / `เก็บไว้ก่อน`; กดใช้ต่อได้ทันที ไม่เรียกว่า Scam และไม่สร้าง Pending Instruction
- เข้า High-Risk combination: contextual warning แบบจริงจัง ไม่มี Mascot แล้วพัก `Pending Instruction` ก่อนส่งเข้าสู่ระบบโอน/PromptPay พร้อม `Pause & Verify` และ `Cancel/Report`
- purpose answer เป็นเพียง signal หนึ่งและไม่มีสิทธิ์ลดระดับที่เกิดจากสัญญาณอื่น

### Value Proposition

เป้าหมายข้อความ: 45–65 คำ แบ่งสองฝั่ง

#### For First Jobbers

- **[PROPOSED VALUE]** ช่วยทั้งสร้างและปกป้องเงินสำรอง ณ decision point ไม่ใช่ให้ความรู้หลังเกิดเหตุ
- ลดภาระการจำออมทุกเดือน และเห็น Progress/Tier จากความต่อเนื่องโดยไม่ให้ผู้มีเงินก้อนใหญ่ได้เปรียบจากยอดดิบ
- เข้าใจเหตุผลที่เตือนจาก observable signals และยังทำธุรกรรมถูกต้อง/ฉุกเฉินได้
- **[HYPOTHESIS]** contextual warning จะเพิ่ม Pause/Cancel โดย friction ยังยอมรับได้—ต้องทดสอบ ไม่เขียนเป็นผลลัพธ์ที่พิสูจน์แล้ว

#### For K PLUS

- ต่อ K-ePocket, Schedule Transfer, transaction context, security controls และระบบสิทธิประโยชน์เดิมให้เป็น journey เดียว
- ขยับจาก awareness ไปสู่ pre-loss intervention โดยไม่ต้องอ่านข้อความส่วนตัวเป็นค่าเริ่มต้น
- **[HYPOTHESIS]** การออมต่อเนื่องอาจเพิ่มยอดเงินฝากที่มีเสถียรภาพและ Engagement ซึ่งสนับสนุนฐานเงินทุน/โอกาสสร้างคุณค่า; Benefit ขึ้นกับต้นทุน ความเสี่ยง กฎเกณฑ์ และ Business Approval
- ผลลัพธ์ทางธุรกิจ/ความเชื่อมั่นเป็น expected value ไม่ระบุตัวเลขกำไร การปล่อยกู้ reduction หรือ adoption โดยไม่มีข้อมูล

### Track Perspective — Cyber Security & Digital Trust

เป้าหมายข้อความ: 70–90 คำ

- Hero threat: authorized transfer ภายใต้ fake-recruiter social engineering; protection policy ใช้กับ protected reserve ใน lifecycle อื่นได้ด้วย
- Detection: multi-signal policy จาก JobShield state, protected fund source, payee history, cumulative behavior, job-payment context และ simulated destination risk
- Defense in depth: contextual explanation → deliberate confirmation → cooling-off/independent verification → Cancel/Report
- Privacy: transaction core ไม่อ่าน inbox; optional sharing ต้อง consent รายครั้งและ data minimization
- Resilience: แยก Savings Nudge จาก Fraud/Scam warning และทดสอบ false positives, emergency access, warning fatigue และ coached bypass ด้วย synthetic scenarios
- ห้ามทำให้ section นี้อ่านเหมือน Track 2 ML model; policy/control design เป็นพระเอก

Core integration boundary: K-ePocket ให้บริบทแหล่งเงิน, K PLUS Transaction + Bank-side Fraud Risk ให้สัญญาณธุรกรรม/ปลายทาง และ K PLUS Security & Fraud Response ใช้แทรกแซงก่อนเงินออก

## 5. Three-Step Visual Content Map

```text
[1 SET UP]
K-ePocket + เงินสำรองตั้งหลัก
Goal + Starting amount + Schedule-based Auto-Routing
        ↓
[2 AUTO-SAVE & BENEFIT]
Qualified rounds + Checkpoint → Benefit Tier 1/3/6 เดือน
        ↓
[3 PROTECT & CONTINUE]
นำเงินออก → Mascot Savings Nudge หรือ Serious Warning/Cooling-off
```

Caption ที่ต้องสื่อ: `K PLUS เดิมเป็นรางสำหรับเก็บ ออม โอน และยืนยันตัวตน ส่วน JobShield เชื่อมรางเหล่านี้เข้ากับ Benefit Loop และ security policy ที่ใช้บริบทของเงินก่อนโอน`

## 6. One Warning Mockup Content Slot

ใช้ BC1-A จาก `research/synthetic-risk-table-v5.md` เป็น hero scenario:

- User context: เปิด JobShield และกำลังดึง ฿7,900 จาก `เงินสำรองตั้งหลัก`
- Destination: ผู้รับใหม่ที่ยังไม่ verified
- Reasons ที่แสดง: ผู้รับใหม่ / แตะเงินสำรองตั้งหลัก / จ่ายเพื่อเริ่มงาน
- Primary actions: `Pause & Verify`, `Cancel/Report`
- Secondary continuation: แสดงตาม cooling-off/verification condition ไม่วางเด่นเท่าปุ่มหยุด

จำนวนเงินและรายละเอียดเป็น synthetic fixture เท่านั้น ไม่ใช่ evidence/statistic

## 7. Evidence Footer Candidates

เลือกเพียง 2–4 แหล่งในหน้า final ตามพื้นที่:

1. KBank — หลอกรับสมัครงานออนไลน์
2. K PLUS product page / K-ePocket
3. KBank 1Q25 MD&A — Lock Account เพื่อยืนยันว่าเราไม่ได้อ้าง money lock เป็นของใหม่
4. KBank anti-fraud controls หรือ ธปท. enhanced measures

FTC/FCA/PSR เหมาะกับ research appendix หรือคำตอบกรรมการมากกว่าหน้าเดียว เว้นแต่ต้องรองรับ intervention rationale โดยตรง

## 8. Assumptions To Keep Out Of The Core Claim

- `KBank-verified employer/payment network` — future integration
- recipient legal type ที่เชื่อถือได้ข้ามธนาคาร — unconfirmed
- automated registry/company-contact lookup — future integration
- fraud graph/CFR/internal API — simulated destination-risk flag เท่านั้น
- exact cooling-off duration และ fraud-specialist SLA — policy/operational unknown
- Email/Link scanning — Optional/Future consent-based extension ไม่ใช่ transaction core
- production ML accuracy หรือ real-world loss reduction — ไม่มีหลักฐานสำหรับ claim
- K Point/คูปองพาร์ตเนอร์ — ตัวอย่าง Benefit ที่ต้องผ่าน Business/Product approval
- เงินฝากเพิ่มทำให้ปล่อยกู้หรือกำไรเพิ่มโดยตรง — ใช้ได้เพียง expected business-value hypothesis แบบมีเงื่อนไข
- event-triggered salary percentage, direct sub-pocket scheduled transfer และ stop-at-cap API — ยังไม่ยืนยันจาก public sources
- special/tiered interest และการนำเงินผู้ใช้ไปลงทุนต่อโดยตรง — ตัดออกจากแนวคิดปัจจุบัน

## 9. Content Cuts If The Page Is Crowded

ตัดตามลำดับนี้:

1. K Point Future Concept และ gamification detail
2. Optional/Future Email/Link sharing
3. verified-employer network และ Fraud Specialist future flow
4. technical signal detail ที่เกินสี่สัญญาณ
5. coded demo/ML/graph discussion
6. สถิติที่ต้องใช้ footnote ยาว

ห้ามตัด:

- First Jobbers อายุ 22–30
- เงินสำรองตั้งหลัก เป้าหมาย 3–6 เดือน และ Auto-Routing ที่ผู้ใช้ควบคุมได้
- fake-recruiter payment moment
- three-step Set up & Build → Detect → Protect & Continue flow
- Track 3 control mechanism
- privacy, false-positive/emergency boundary อย่างน้อยหนึ่งบรรทัด
- value ต่อทั้งผู้ใช้และ K PLUS

## 10. Pre-Draft Questions For Later User Approval

คำถามเหล่านี้ไม่ block skeleton แต่ต้องตอบก่อน final wording/layout:

1. Test Final Proposal 1 ใช้ชื่อ `K PLUS JobShield`; final submission ยังรอ user approval
2. Test Final Proposal 1 ไม่ใช้ตัวเลข 17% / มากกว่า 920 ล้านบาท เพื่อหลีกเลี่ยงการทำให้หมวด task scam ที่กว้างกว่าดูเหมือนเป็นสถิติของ fake recruiter/First Jobbers โดยตรง
3. **Resolved:** ใช้คำว่า `เงินสำรองตั้งหลัก (Protected Reserve)` เป็นชื่อเดียวตลอด Flow และอธิบายว่าเป็น K-ePocket ที่กำหนดวัตถุประสงค์ ไม่ใช่ผลิตภัณฑ์เงินฝากใหม่
4. Test Final Proposal 1 ใช้ High warning จาก BC1-A เป็น hero mockup
5. หลัง formative test ต้องปรับ copy/control ใดก่อนเริ่ม final Proposal

## 11. Exit Criteria Before Final Proposal

- threat model และ synthetic policy ผ่าน cross-review ของ technical owner
- visual owner แปลง three-step flow และ warning fixtureเป็น clickable Figma ได้โดยไม่เพิ่ม feature
- formative test เปรียบเทียบ contextual กับ generic warning และรายงานจำนวน/ผลจริง
- claim ทุกข้อ trace กลับไปที่ source, proposed behavior, hypothesis หรือ assumption ได้
- ผู้ใช้อนุมัติ final name, evidence choice และ wording direction ก่อนเริ่ม final Proposal
