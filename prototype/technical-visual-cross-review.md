# K PLUS JobShield — Technical/Visual Cross-Review

> Scope note — 6 กันยายน 2026: ตารางเดิมเป็น review history ก่อน V6; current scope อยู่ใน [figma-flow-spec-v6.md](./figma-flow-spec-v6.md) และต้อง cross-review ใหม่หลัง Figma V6 ถูกสร้าง

สถานะ: Cross-review completed at specification level; scope sync added — 5 กันยายน 2026  
ผู้รับผิดชอบตามแผน: ผู้สมัครหลัก = technical/content owner; สมาชิกคนที่สอง = visual/prototype owner  
ขอบเขต: ตรวจความสอดคล้องระหว่าง threat model, synthetic policy และ non-final content skeleton ก่อนสร้าง Figma  
ไม่ใช่: final visual approval, usability result หรือ final Proposal

## Review Inputs

- `research/threat-model.md`
- `research/synthetic-risk-table.md`
- `research/signal-feasibility.md`
- `research/competitor-gap.md`
- `proposal/content-skeleton.md`

## Executive Decision

Flow พร้อมแปลงเป็น prototype โดยใช้ BC1-A เป็น hero path และใช้ BC2-A/BC3-A เป็น low-friction validation paths ส่วน BC4-A/BC4-B ทดสอบ policy logic หลังฉาก ไม่ต้องสร้างทุก permutation เป็นหน้าจอ

มีข้อกำหนดสำคัญสี่ข้อ:

1. ห้ามทำให้ `Career Mode` ดูเป็น fraud detector ที่รับประกันผล; มันเป็น context layer
2. ห้ามเรียกผู้รับว่าเป็นมิจฉาชีพเมื่อระบบมีเพียง risk indicators
3. `verified biller/payment channel` ไม่เท่ากับ `verified employer`; prototype ต้องใช้คำให้ต่างกัน
4. High-Risk state ต้องเกิดก่อน payment instruction และไม่มีตัวเลข cooling-off/score ที่แต่งขึ้น

Scope ที่ล็อกเพิ่ม:

1. ใช้คำว่า `เงินสำรองก่อนเงินเดือนแรก`
2. Core มีเพียง `K-ePocket`, `K PLUS Transaction + Bank-side Fraud Risk` และ `K PLUS Security & Fraud Response`
3. `Dynamic Time Lock` เป็นกลไกภายใน risk-based Cooling-off; High-Risk state พักเป็น Pending Instruction ก่อนส่งเข้าสู่ระบบโอน/PromptPay
4. Email/Link scanning และ Fraud Specialist เป็น Optional/Future integration
5. Prototype ใช้ deterministic rules/policy และ synthetic data; ไม่มี ML model

## Cross-Artifact Consistency Matrix

| Decision | Threat model | Risk policy | Content skeleton | Review result |
|---|---|---|---|---|
| Core threat = authorized transfer under social engineering | ระบุชัด | BC1/BC4 จำลองผู้ใช้กดเอง | Problem/Track sections กล่าวถึง | Pass |
| Career Mode เป็น opt-in | Boundary B2/T10 | `career_mode` + BASE-1 | Step 1/Target Users | Pass |
| Job Search Budget/เงินสำรองก่อนเงินเดือนแรกใช้ของเดิมเป็นฐาน | Assets/control strategy | `fund_source` | REUSE labels | Pass |
| เงินสำรองก่อนเงินเดือนแรกเพียงอย่างเดียวไม่ใช่ High | SR-04 | N2 | emergency/false-positive boundary | Pass |
| Purpose ห้ามลด tier | B2/T4/SR-02 | BC4-A/N1 | Step 2 | Pass |
| Split payments ต้อง aggregate | T3/SR-03 | P3/BC4-B/N6 | Track Perspective | Pass |
| High เกิดก่อนโอน | B4/SR-01 | High action/acceptance criteria | Step 3 | Pass |
| Emergency/legitimate path ไม่ถูกกัก | T6/T7/SR-06 | BC2/BC3 | Value/Step 3 | Pass |
| Email/Link scanning ไม่ใช่ Core | B1/SR-08 | ไม่มีใน input core | assumptions/cuts | Pass |
| Destination risk เป็น integration assumption | Defenders/B3 | simulated flag | REUSE/ASSUMPTION | Pass |
| Cooling-off พักก่อน payment rail | B4/SR-01 | Pending Instruction | Step 3 | Pass |
| Core จำกัดที่ 3 integrations | Control architecture | 3 named integration boundaries | Current Scope Lock | Pass |

## Issues Found And Resolution

### CR-01 — “Verified employer” อาจทำให้เข้าใจเกิน capability

- ความเสี่ยง: ผู้ใช้และกรรมการอาจคิดว่า KBank รับรองนายจ้างหรือ offer งาน
- การแก้: Core UI ใช้ `verified payment channel` หรือ `verified biller` เท่านั้น
- Future label: employer directory/registry lookup แสดงเป็น future integration และไม่อยู่ใน hero flow

### CR-02 — Purpose question อาจกลายเป็น bypass switch

- ความเสี่ยง: attacker coach ให้เลือก `อื่น ๆ` หรือ `ไม่เกี่ยวกับงาน`
- การแก้: purpose เพิ่มเหตุผลที่แสดงได้ แต่ไม่ลด tier จาก payee/fund/pattern/destination signals
- Visual requirement: ไม่บอกผู้ใช้ว่าเลือกคำตอบใดแล้วจะ “ผ่าน”

### CR-03 — Career Mode + new payee ทุกคนอาจสร้าง warning fatigue

- ความเสี่ยง: การโอนที่ถูกต้องให้เพื่อน/ร้านค้าใหม่ถูกเตือนบ่อย
- การแก้: new unverified payee ใน Career Mode อยู่ Medium ไม่ใช่ High; verified biller, known payee และ own account ใช้ flow ต่ำกว่าเมื่อไม่มี conflict
- Test requirement: BC2-B ต้องวัดว่าคำเตือน Medium รบกวนเกินไปหรือไม่

### CR-04 — Static countdown ทำให้ prototype แสร้งเป็น policy จริง

- ความเสี่ยง: ตัวเลขเช่น 30 นาที/24 ชั่วโมงดูเหมือนผ่าน legal/operational review แล้ว
- การแก้: ใช้ข้อความ `พักรายการตามระดับความเสี่ยง` และ prototype control `จำลองว่าผ่านเงื่อนไขแล้ว`
- Later decision: ระยะจริงต้องมาจาก policy, risk และ usability validation

### CR-05 — Face verification อาจถูกตีความว่าแก้ social engineering

- ความเสี่ยง: biometric พิสูจน์ผู้ถือบัญชี แต่ไม่พิสูจน์ว่าเจตนาปลอดการหลอกลวง
- การแก้: วาง stronger verification เป็น secondary control หลัง contextual pause ไม่ใช้เป็น value proposition หลัก

### CR-06 — “Cancel/Report” ต้องแยกผลของแต่ละ action

- ความเสี่ยง: ผู้ใช้เข้าใจว่ารายงานแล้วธนาคารเรียกเงินคืนหรือ freeze ได้แน่นอน
- การแก้: `Cancel transfer` ยกเลิกรายการที่ยังไม่ส่ง และ `Report concern` เปิดช่องทางแจ้งเหตุโดยไม่รับประกัน recovery
- Visual requirement: หน้ายืนยันต้องบอกชัดว่า “รายการนี้ยังไม่ถูกส่ง”

### CR-07 — High warning อาจมีข้อความแน่นเกินไป

- ความเสี่ยง: ผู้ใช้ภายใต้แรงกดดันไม่อ่าน
- การแก้: หน้าหลักใช้เหตุผลสูงสุดสามข้อ หนึ่ง impact statement และสอง primary safety actions; รายละเอียดอยู่ `Learn more`

## Technical Review Decisions

- ใช้ deterministic tier labels ใน prototype; ไม่แสดงคะแนนหรือเปอร์เซ็นต์ความเสี่ยง
- เก็บ event category และ rule ID สำหรับ test audit แต่ไม่โชว์ rule ID ใน consumer UI
- Current High event ไม่ถูก downgrade หากผู้ใช้ปิด Career Mode ระหว่าง flow
- Re-evaluate ทุก transfer และรวมประวัติรายการซ้ำก่อนตัดสิน tier
- `Pause & Verify` พักเป็น Pending Instruction และไม่ส่งเข้าสู่ระบบโอน/PromptPay
- `Continue after conditions` เป็นเส้นทางรองและต้องไม่แสดงก่อน pause state
- `Report concern` เป็น handoff ไปช่องทางที่มีอยู่/สมมติอย่างชัดเจน ไม่แสร้งว่ามี specialist SLA

## Visual Review Decisions

- Hero story มีสามช่วงเท่านั้น: `Prepare → Detect → Intervene`
- ใช้ source-of-funds card ให้เห็นว่าเงินมาจาก `เงินสำรองก่อนเงินเดือนแรก`
- Risk reasons ใช้ข้อความ + icon; ห้ามพึ่งแดง/เหลือง/เขียวเพียงอย่างเดียว
- Tap target อย่างน้อย 44 × 44 px; body text อย่างน้อย 16 px ใน frame 390 × 844
- รองรับภาษาไทยหลายบรรทัดและ text scaling; ไม่วางข้อความสำคัญในภาพ raster
- High warning ใช้ neutral, non-blaming language และไม่กล่าวว่า “บัญชีนี้โกง”
- Visual style, brand tokens และ final typography เป็นสิทธิ์ตัดสินใจของ visual owner; spec ใช้ semantic roles ไม่อ้าง official K PLUS design system

## Screen-Level Traceability

| Prototype moment | Requirement shown | Scenario evidence | Must not imply |
|---|---|---|---|
| Career Mode onboarding | opt-in, expiry, Job Search Budget/เงินสำรองก่อนเงินเดือนแรก | T10/BASE-1 | ระบบรู้สถานะงานเอง |
| Transfer review | source, amount, destination | B3 | อ่าน email/chat แล้ว |
| Context question | purpose เป็น optional/weak signal | T4/BC4-A | คำตอบหนึ่งทำให้ปลอดภัย |
| High warning | reasons + amount at risk | BC1-A/SR-07 | fraud certainty หรือ model score |
| Pause state | Pending Instruction ยังไม่ส่งเข้าสู่ระบบโอน/PromptPay | B4/SR-01 | bank recovered completed transfer |
| Verification path | independent source principle | B5 | KBank รับรอง employer แล้ว |
| Cancel/Report | separate consequences | T7/SR-10 | guaranteed freeze/reimbursement |
| Legitimate/emergency branches | limited friction | BC2/BC3 | เงินสำรองก่อนเงินเดือนแรกถูกล็อกถาวร |

## Cross-Review Exit Result

**PASS FOR FIGMA SPECIFICATION** โดยมีเงื่อนไข:

- visual owner ต้องยืนยันคำว่า `verified payment channel` และ semantic hierarchy
- actual Figma file ต้องรักษา branch สำหรับ legitimate และ emergency flow ไม่ใช่แสดงแต่ Scam flow
- usability test ต้องตรวจความเข้าใจคำว่าเงินสำรองก่อนเงินเดือนแรก, verified payment channel และผลของ Pause/Cancel/Report
- การเปลี่ยน rule/flow ที่มีผลต่อ High/Medium ต้องย้อนมาแก้ risk table ก่อนแก้ภาพ
