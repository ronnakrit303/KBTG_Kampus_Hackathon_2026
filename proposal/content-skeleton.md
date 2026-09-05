# K PLUS JobShield — Non-Final One-Page Content Skeleton

สถานะ: Working content architecture; scope synced — 5 กันยายน 2026  
คำเตือน: ไฟล์นี้ **ไม่ใช่ final Proposal**, ไม่ใช่ copy ที่อนุมัติ และยังไม่ใช่ PDF  
ภาษา: ภาษาไทยเป็นหลัก โดยคง required section headings และ technical terms ภาษาอังกฤษ

## Current Scope Lock

- ใช้คำว่า `เงินสำรองก่อนเงินเดือนแรก`
- Core มี 3 integrations: K-ePocket, K PLUS Transaction + Bank-side Fraud Risk และ K PLUS Security & Fraud Response
- `Dynamic Time Lock` เป็นส่วนหนึ่งของ risk-based Cooling-off; High-Risk flow พัก Pending Instruction ก่อนส่งเข้าสู่ระบบโอน/PromptPay
- Email/Link scanning และ Fraud Specialist เป็น Optional/Future integration ไม่ใช่ Core
- Prototype ใช้ rules/policy กับ synthetic data และไม่มี ML model; ห้ามนำเสนอว่าเป็นโมเดลตรวจจับที่สร้างเสร็จแล้ว

## 1. Page-Level Message

### Working title

`K PLUS JobShield`

### Working descriptor

`ปกป้องเงินก้อนเริ่มต้น เมื่อถูกผู้รับสมัครงานปลอมขอให้จ่ายเงินเพื่อแลกกับงาน`

### Working value proposition — not final copy

`Career Mode ของ K PLUS ใช้บริบทการหางาน แหล่งเงิน และสัญญาณธุรกรรม เพื่อเลือกการแทรกแซงก่อนเงินออก โดยยังคงทางผ่านสำหรับค่าใช้จ่ายที่ถูกต้องและเหตุฉุกเฉิน`

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
- **[HYPOTHESIS]** ช่วงหางานทำให้ผู้ใช้ต้องรับการติดต่อจากผู้ส่งที่ไม่คุ้นเคยและเงินก้อนเริ่มต้นมีความสำคัญต่อค่าใช้ชีวิต
- จบด้วย design gap: คำเตือนทั่วไปไม่ได้เชื่อม `job-search context + fund source + transaction risk`

ห้ามเขียน:

- First Jobbers ถูกหลอกมากกว่ากลุ่มอื่น
- ผู้สมัครงานทุกคนรีบกดลิงก์หรือไม่ระมัดระวัง
- ตัวเลข task-scam ทั้งหมดคือความเสียหายจาก fake recruiter หลังส่ง Resume

### Target Users

เป้าหมายข้อความ: 25–35 คำภาษาไทย

- First Jobbers อายุ 22–30 ที่กำลังสมัครงาน รอเริ่มงาน หรือรอเงินเดือนแรก
- เน้นผู้ใช้ที่เลือกเปิด Career Mode ไม่ infer สถานะจากอายุ/พฤติกรรมโดยอัตโนมัติ
- ปัญหาเฉพาะคือ transitional job-search context ไม่ใช่การตีตราว่ากลุ่มนี้มีความรู้ต่ำ

### Proposed Solution

เป้าหมาย: three-step flow รวมประมาณ 90–120 คำ

#### Step 1 — Prepare: เปิด Career Mode และกำหนดเงิน

- **[PROPOSED]** ผู้ใช้ opt-in Career Mode กำหนดช่วงเวลา และปิด/ให้หมดอายุได้
- **[REUSE]** `Job Search Budget` ต่อจาก My Budget; `เงินสำรองก่อนเงินเดือนแรก` ใช้ user-designated K-ePocket/sub-pocket
- แสดงคุณค่าทางการเงิน: แยกเงินค่าใช้จ่ายหางานออกจากเงินค่าใช้ชีวิตช่วงเริ่มงาน

#### Step 2 — Detect: ประเมินก่อนโอนด้วยหลายสัญญาณ

- **[PROPOSED]** policy รวม fund source, first-seen payee, repeated/cumulative transfers และ job-payment context
- **[REUSE/ASSUMPTION]** destination-risk เป็น simulated integration กับ bank-side fraud control; ห้ามอ้างว่าทีมเข้าถึงระบบจริง
- purpose answer เป็นเพียง signal หนึ่งและไม่มีสิทธิ์ลด tier

#### Step 3 — Intervene: friction ตามความเสี่ยง

- Low: flow ปกติ
- Medium: contextual warning + deliberate confirmation
- High: risk-based Cooling-off ที่พัก `Pending Instruction` ก่อนส่งเข้าสู่ระบบโอน/PromptPay + independent verification พร้อม `Pause & Verify` และ `Cancel/Report`
- own account/verified biller มี limited break-glass; หลังครบเงื่อนไขผู้ใช้ยังยืนยันต่อได้

### Value Proposition

เป้าหมายข้อความ: 45–65 คำ แบ่งสองฝั่ง

#### For First Jobbers

- **[PROPOSED VALUE]** ปกป้องเงินสำรอง ณ decision point ไม่ใช่ให้ความรู้หลังเกิดเหตุ
- เข้าใจเหตุผลที่เตือนจาก observable signals และยังทำธุรกรรมถูกต้อง/ฉุกเฉินได้
- **[HYPOTHESIS]** contextual warning จะเพิ่ม Pause/Cancel โดย friction ยังยอมรับได้—ต้องทดสอบ ไม่เขียนเป็นผลลัพธ์ที่พิสูจน์แล้ว

#### For K PLUS

- ต่อความสามารถ My Budget, K-ePocket และ fraud controls ที่มีอยู่ให้เป็น journey เฉพาะช่วงหางาน
- ขยับจาก awareness ไปสู่ pre-loss intervention โดยไม่ต้องอ่านข้อความส่วนตัวเป็นค่าเริ่มต้น
- ผลลัพธ์ทางธุรกิจ/ความเชื่อมั่นเป็น expected value ไม่ระบุตัวเลข reduction/adoption โดยไม่มีข้อมูล

### Track Perspective — Cyber Security & Digital Trust

เป้าหมายข้อความ: 70–90 คำ

- Threat: authorized transfer ภายใต้ fake-recruiter social engineering
- Detection: multi-signal policy จาก app state, fund source, payee history, cumulative behavior และ simulated destination risk
- Defense in depth: contextual explanation → deliberate confirmation → cooling-off/independent verification → Cancel/Report
- Privacy: transaction core ไม่อ่าน inbox; optional sharing ต้อง consent รายครั้งและ data minimization
- Resilience: test false positives, emergency access, warning fatigue และ coached bypass ด้วย synthetic scenarios
- ห้ามทำให้ section นี้อ่านเหมือน Track 2 ML model; policy/control design เป็นพระเอก

Core integration boundary: K-ePocket ให้บริบทแหล่งเงิน, K PLUS Transaction + Bank-side Fraud Risk ให้สัญญาณธุรกรรม/ปลายทาง และ K PLUS Security & Fraud Response ใช้แทรกแซงก่อนเงินออก

## 5. Three-Step Visual Content Map

```text
[1 PREPARE]
Career Mode
My Budget + user-designated K-ePocket
        ↓
[2 DETECT]
Fund source + New payee + Repetition + Destination risk
        ↓
[3 INTERVENE]
Low: Normal | Medium: Explain | High: Pause, Verify, Cancel/Report
```

Caption ที่ต้องสื่อ: `ความแตกต่างไม่ได้อยู่ที่ pocket หรือ warning แยกกัน แต่อยู่ที่การใช้บริบทและแหล่งเงินเปลี่ยน security policy ก่อนโอน`

## 6. One Warning Mockup Content Slot

ใช้ BC1-A จาก synthetic risk table เป็น hero scenario:

- User context: เปิด Career Mode และกำลังดึง ฿7,900 จาก `เงินสำรองก่อนเงินเดือนแรก`
- Destination: ผู้รับใหม่ที่ยังไม่ verified
- Reasons ที่แสดง: ผู้รับใหม่ / แตะเงินสำรองก่อนเงินเดือนแรก / จ่ายเพื่อเริ่มงาน
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

## 9. Content Cuts If The Page Is Crowded

ตัดตามลำดับนี้:

1. Optional/Future Email/Link sharing
2. verified-employer network และ Fraud Specialist future flow
3. technical signal detail ที่เกินสี่สัญญาณ
4. coded demo/ML/graph discussion
5. สถิติที่ต้องใช้ footnote ยาว

ห้ามตัด:

- First Jobbers อายุ 22–30
- การจัดเงิน/ออมผ่าน Job Search Budget + เงินสำรองก่อนเงินเดือนแรก
- fake-recruiter payment moment
- three-step pre-transfer flow
- Track 3 control mechanism
- privacy, false-positive/emergency boundary อย่างน้อยหนึ่งบรรทัด
- value ต่อทั้งผู้ใช้และ K PLUS

## 10. Pre-Draft Questions For Later User Approval

คำถามเหล่านี้ไม่ block skeleton แต่ต้องตอบก่อน final wording/layout:

1. Test Final Proposal 1 ใช้ชื่อ `K PLUS JobShield`; final submission ยังรอ user approval
2. Test Final Proposal 1 ไม่ใช้ตัวเลข 17% / มากกว่า 920 ล้านบาท เพื่อหลีกเลี่ยงการทำให้หมวด task scam ที่กว้างกว่าดูเหมือนเป็นสถิติของ fake recruiter/First Jobbers โดยตรง
3. **Resolved:** ใช้คำว่า `เงินสำรองก่อนเงินเดือนแรก` และอธิบายว่าเป็นเงินที่ผู้ใช้กำหนดวัตถุประสงค์ใน K-ePocket ไม่ใช่ผลิตภัณฑ์เงินฝากใหม่
4. Test Final Proposal 1 ใช้ High warning จาก BC1-A เป็น hero mockup
5. หลัง formative test ต้องปรับ copy/control ใดก่อนเริ่ม final Proposal

## 11. Exit Criteria Before Final Proposal

- threat model และ synthetic policy ผ่าน cross-review ของ technical owner
- visual owner แปลง three-step flow และ warning fixtureเป็น clickable Figma ได้โดยไม่เพิ่ม feature
- formative test เปรียบเทียบ contextual กับ generic warning และรายงานจำนวน/ผลจริง
- claim ทุกข้อ trace กลับไปที่ source, proposed behavior, hypothesis หรือ assumption ได้
- ผู้ใช้อนุมัติ final name, evidence choice และ wording direction ก่อนเริ่ม final Proposal
