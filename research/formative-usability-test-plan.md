# K PLUS JobShield — Formative Usability Test Plan

สถานะ: Clickable prototype built; `0 pilot sessions conducted`; `0 participant sessions conducted` — 4 กันยายน 2026  
ขอบเขต: เปรียบเทียบ contextual JobShield warning กับ generic warning และตรวจ legitimate/emergency friction  
ห้ามทำ: สร้างผลทดสอบ ผู้เข้าร่วม คำพูด เวลา หรือสถิติขึ้นเอง

## 1. Research Questions

1. ผู้ใช้เข้าใจหรือไม่ว่าทำไมรายการหนึ่งจึงถูกเตือน โดยไม่ต้องเห็น technical score
2. Contextual warning ทำให้ผู้ใช้เลือก Pause/Cancel ใน scam scenario มากกว่า generic warningในเชิงทิศทางหรือไม่
3. ผู้ใช้ยังทำ legitimate payment และ emergency transfer สำเร็จได้หรือไม่
4. ผู้ใช้เข้าใจความแตกต่างระหว่าง `verified payment channel` กับการรับรองว่า employer/offer งานเป็นของจริงหรือไม่
5. Career Mode, Job Search Budget และ `เงินสำรองก่อนเงินเดือนแรก` มี mental model ที่ชัดหรือสร้างความสับสนหรือไม่
6. ข้อความ/ขั้นตอนใดทำให้เกิด warning fatigue, ความกลัว หรือความรู้สึกว่าธนาคารกักเงิน

## 2. Study Type And Limits

- รูปแบบ: moderated formative usability test แบบ remote หรือ in-person
- กลุ่มเป้าหมาย: 5–8 คนที่เป็น First Jobbers อายุใกล้เคียง 22–30 หรืออยู่ในช่วงสมัคร/เริ่มงาน
- ระยะเวลา: 20–30 นาทีต่อคน
- Data: synthetic prototype เท่านั้น ไม่ขอเลขบัญชี Resume อีเมล หรือประวัติการเงินจริง
- Analysis: รายงานจำนวนคน ตัวอย่างพฤติกรรม และ median time เมื่อเหมาะสม; ไม่ทำ population inference หรืออ้าง statistical significance
- Incentive/recording: ผู้จัดทดสอบต้องแจ้งและขอ consent จริงก่อนใช้; เอกสารนี้ไม่กำหนดเงินตอบแทนหรืออนุญาต recording อัตโนมัติ

## 3. Participant Screener

เก็บเฉพาะข้อมูลขั้นต่ำ:

1. อายุอยู่ในช่วง 22–30 หรือใกล้เคียงหรือไม่
2. ปัจจุบัน/ช่วง 12 เดือนที่ผ่านมาเคยสมัครงาน รอเริ่มงาน หรือเริ่มงานแรกหรือไม่
3. ใช้ mobile banking เป็นประจำหรือไม่
4. เคยเห็นคำเตือนก่อนโอนหรือไม่ — ตอบได้ว่าไม่แน่ใจ
5. ต้องการ accessibility accommodation อะไรในการทดสอบหรือไม่

ไม่ถามว่าผู้เข้าร่วมเคยตกเป็นเหยื่อหรือสูญเงินหรือไม่ เว้นแต่ผู้เข้าร่วมเลือกเล่าเอง และห้ามบันทึกรายละเอียดระบุตัวตน

## 4. Consent Script

> การทดสอบนี้ประเมินต้นแบบ ไม่ได้ทดสอบความฉลาดหรือความระมัดระวังของคุณ ทุกชื่อบริษัท บัญชี และจำนวนเงินเป็นข้อมูลสมมติ คุณหยุดหรือข้ามคำถามได้ทุกเมื่อ เราจะไม่ขอข้อมูลธนาคาร รหัสผ่าน Resume หรือข้อความส่วนตัว หากมีการบันทึกเสียง/หน้าจอ ผู้ดำเนินการจะขออนุญาตแยกก่อนเริ่ม

บันทึก consent เป็น `yes/no` และ recording consent แยกต่างหาก

## 5. Experimental Structure

ใช้ within-participant comparison ด้วย scam scenarios ที่ matched แต่ไม่เหมือนกันทั้งหมด และ counterbalance order เพื่อลด learning effect

### Warning variants

- **G — Generic:** `โปรดระวัง มิจฉาชีพอาจหลอกให้โอนเงิน ตรวจสอบข้อมูลก่อนทำรายการ` พร้อม `ยืนยัน`/`ยกเลิก`
- **C — Contextual JobShield:** เหตุผลจาก transaction 2–3 ข้อ + ผลกระทบต่อเงินสำรองก่อนเงินเดือนแรก + `Pause & Verify`/`Cancel/Report`

### Counterbalanced orders

| Participant | Scam warning order | Legitimate/emergency order |
|---|---|---|
| P01, P03, P05, P07 | G → C | Legitimate → Emergency |
| P02, P04, P06, P08 | C → G | Emergency → Legitimate |

หากผู้เข้าร่วมน้อยกว่าแปด ให้ใช้ลำดับสลับตามเลขคี่/คู่และรายงานจำนวนจริง

## 6. Scenario Set

รายละเอียดทุกอย่างเป็น synthetic fixture

### Task S1 — Scam warning comparison

สถานการณ์: บริษัทที่อ้างว่ารับคุณเข้าทำงานขอค่าอุปกรณ์ก่อนเริ่มงาน โดยให้โอนจากเงินสำรองไปยังผู้รับใหม่

ผู้เข้าร่วมกลุ่มตาม order จะเห็น Generic หรือ Contextual warning ก่อน ห้าม facilitator บอกว่าเป็น Scam

Task prompt:

> คุณกำลังรอเริ่มงานและได้รับคำขอให้จ่ายค่าอุปกรณ์ ฿7,900 ภายในวันนี้ โปรดทำสิ่งที่คุณคิดว่าจะทำจริงจนถึงหน้าสุดท้ายของภารกิจ

### Task S2 — Matched second warning

สถานการณ์: ผู้ติดต่ออีกบริษัทขอเงินประกันอบรมจำนวนสมมติผ่านผู้รับใหม่ เปลี่ยนชื่อ/จำนวนเพื่อไม่ให้จำคำตอบเดิม แต่รักษาสัญญาณหลักให้เทียบกันได้

ใช้ warning variant อีกแบบตาม counterbalanced order

### Task L — Legitimate payment

สถานการณ์: ชำระค่าสอบหรือใบรับรองที่วางแผนไว้จาก Job Search Budget ไป verified payment channel

Task prompt:

> คุณวางแผนค่าสอบ ฿1,200 ไว้ใน Job Search Budget แล้ว โปรดชำระผ่านช่องทางที่แสดงในต้นแบบ

Expected: ทำรายการสำเร็จโดยไม่เจอ High-Risk cooling-off

### Task E — Emergency transfer

สถานการณ์: โอนเงินจาก `เงินสำรองก่อนเงินเดือนแรก` ไปบัญชีตนเองเพื่อใช้จ่ายฉุกเฉิน

Task prompt:

> คุณต้องย้ายเงิน ฿6,000 จากเงินสำรองก่อนเงินเดือนแรกไปบัญชีของคุณเองเพื่อใช้จ่ายจำเป็น โปรดทำรายการจนเสร็จ

Expected: ทำรายการสำเร็จโดยไม่เข้า High-Risk flow

### Optional Task M — Medium false-positive probe

สถานการณ์: ค่าเอกสารสมัครงานจริง ฿900 แต่ปลายทางเป็นผู้รับใหม่ที่ยังไม่ verified

ใช้เมื่อเวลาเหลือเพื่อทดสอบว่า Medium warning ให้ข้อมูลพอโดยไม่ทำให้ผู้ใช้รู้สึกถูกกล่าวหา

## 7. Facilitator Guide

### Opening

1. อ่าน consent script และบันทึก consent
2. ย้ำว่าให้คิดดัง ๆ แต่ไม่มีคำตอบถูกผิด
3. ห้ามสอนความหมายของปุ่มหรือเฉลยว่า scenario ใดเป็น Scam ก่อนจบ task

### Neutral prompts

- `ตอนนี้คุณคิดว่าเกิดอะไรขึ้น?`
- `คุณคาดว่าปุ่มนี้จะพาไปไหน?`
- `อะไรทำให้คุณเลือกทำหรือไม่ทำรายการต่อ?`
- `มีคำไหนที่ไม่ชัดเจนไหม?`

ห้ามถามแบบชี้นำ เช่น `เห็นไหมว่าผู้รับนี้เสี่ยง` หรือ `คุณจะกดยกเลิกใช่ไหม`

### After each warning

ถามโดยไม่เปิดหน้าจอซ้ำก่อน:

1. `ข้อความนี้กำลังเตือนเรื่องอะไร?`
2. `จำเหตุผลที่ระบบแสดงได้กี่ข้อ และมีอะไรบ้าง?`
3. `รายการถูกส่งไปแล้วหรือยัง?`
4. `ถ้ากด Pause & Verify คุณคิดว่าจะเกิดอะไรขึ้น?`
5. `คุณมั่นใจในการตัดสินใจแค่ไหน 1–5? เพราะอะไร?`

### Closing

- `Career Mode มีประโยชน์พอให้คุณเปิดหรือไม่?`
- `ขั้นตอนไหนรบกวนหรือทำให้ไม่ไว้ใจระบบ?`
- `เงินสำรองก่อนเงินเดือนแรก หมายถึงอะไรในความเข้าใจของคุณ?`
- `verified payment channel รับรองอะไร และไม่ได้รับรองอะไร?`
- `ถ้าแก้ได้หนึ่งอย่าง คุณจะเปลี่ยนอะไร?`

## 8. Measures And Coding

| Measure | Coding | ประเภท |
|---|---|---|
| Primary action in scam task | continue / pause / cancel / report | Behavioral |
| Warning comprehension | 0 = ไม่เข้าใจ, 1 = เข้าใจภัยทั่วไป, 2 = ระบุเหตุผลได้ ≥1, 3 = ระบุเหตุผลสำคัญได้ ≥2 | Comprehension rubric |
| Transaction-state comprehension | correct/incorrect: รู้ว่ารายการยังไม่ถูกส่ง | Safety comprehension |
| Legitimate task success | success / assisted / fail | Usability |
| Emergency task success | success / assisted / fail | Safety/usability |
| Time to first warning action | seconds from warning shown | Efficiency |
| Task completion time | seconds per task | Efficiency |
| Confidence | 1–5 + reason | Self-report |
| Perceived friction | 1–5 + reason | Self-report |
| Warning trust | 1–5 + reason | Self-report |
| Terminology issue | free-text + observed confusion | Qualitative |

ห้ามแปลง rubric ขนาดเล็กนี้เป็น model accuracy หรือ real-world fraud-prevention rate

## 9. Session Observation Template

```text
Participant ID: P__
Date/time:
Format: remote / in-person
Relevant profile (minimal):
Consent: yes/no
Recording consent: yes/no/not recorded
Order: G→C or C→G

Task S1
- Warning variant:
- First action:
- Final action:
- Time to first action:
- Comprehension 0–3:
- Believes transaction already sent? yes/no/unclear
- Quote/observation:
- Assistance given:

Task S2
- Warning variant:
- First action:
- Final action:
- Time to first action:
- Comprehension 0–3:
- Believes transaction already sent? yes/no/unclear
- Quote/observation:
- Assistance given:

Task L
- Success/assisted/fail:
- Completion time:
- Unexpected warning/confusion:

Task E
- Success/assisted/fail:
- Completion time:
- Believes เงินสำรองก่อนเงินเดือนแรก is locked? yes/no/unclear

Post-test
- Career Mode value 1–5 + reason:
- Friction 1–5 + reason:
- Warning trust 1–5 + reason:
- Terminology issues:
- One requested change:
```

ใช้ Participant ID เท่านั้น แยก consent record จาก observation notes หากมีข้อมูลติดต่อสำหรับนัดหมาย

## 10. Synthesis Template

### Participant accounting

- Recruited:
- Completed:
- Excluded/withdrawn พร้อมเหตุผลที่ไม่ระบุตัวตน:
- Generic-first / Contextual-first:

### Results table — fill only after sessions

| Outcome | Generic | Contextual | Interpretation |
|---|---:|---:|---|
| Pause/Cancel count | — | — | Directional comparison only |
| Median comprehension score | — | — | Small formative sample |
| Median time to first action | — | — | Check hesitation vs understanding |
| Misunderstood transaction state | — | — | Safety issue if present |

| Legitimate/emergency outcome | Count | Interpretation |
|---|---:|---|
| Legitimate success without assistance | — | |
| Emergency success without assistance | — | |
| Mistook verified payment for verified employer | — | |
| Believed เงินสำรองก่อนเงินเดือนแรก was permanently locked | — | |

### Severity coding

- **Critical:** ทำให้ผู้ใช้คิดว่ารายการยังไม่ส่งทั้งที่ส่งแล้ว, ส่งโดยไม่ตั้งใจ หรือเข้าใจว่า bank รับรอง employer
- **High:** ขัดขวาง legitimate/emergency task หรือทำให้ safety action หาไม่เจอ
- **Medium:** comprehension/terminology confusion ที่ต้องใช้ facilitator
- **Low:** cosmetic หรือ preference ที่ไม่เปลี่ยน task outcome

## 11. Decision Rules

### Continue with current direction when

- Contextual variant แสดงทิศทางที่ดีกว่า Generic ใน comprehension และ Pause/Cancel โดยไม่ต้องอ้าง significance
- ผู้เข้าร่วมส่วนใหญ่ทำ legitimate และ emergency tasks ได้โดยไม่ต้องช่วย
- ไม่มี Critical misunderstanding เรื่อง transaction state หรือ employer verification

### Revise before Proposal when

- ผู้เข้าร่วมจำเหตุผลไม่ได้หรือคิดว่าคะแนนของระบบยืนยันว่าเป็น Scam แน่นอน
- `Pause & Verify`, `Cancel` และ `Report` ให้ผลที่ผู้ใช้คาดไม่ตรง
- Medium warning ขัดขวางค่าใช้จ่ายจริงซ้ำ ๆ
- `เงินสำรองก่อนเงินเดือนแรก` ถูกเข้าใจว่าเป็นเงินที่ถอนออกไม่ได้

### Fail/pivot condition

- Contextual warning ไม่ดีกว่า Generic ใน action/comprehension ของกลุ่มทดสอบ
- legitimate/emergency friction ทำให้หลายคนทำ task ไม่สำเร็จหรือไม่ต้องการเปิด Career Mode
- คุณค่าที่ผู้ใช้รับรู้เหลือเพียง “pocket + warning” และอธิบาย context-aware policy ไม่ได้

## 12. Data Handling And Reporting

- เก็บเฉพาะ Participant ID, task outcomes และ notes ที่จำเป็น
- ไม่ใส่ชื่อจริง บริษัทจริง เลขบัญชี หรือรายละเอียดประสบการณ์ Scam ที่ระบุตัวได้ใน repository
- หากบันทึกเสียง/วิดีโอ ให้ผู้ใช้กำหนดสถานที่เก็บ สิทธิ์เข้าถึง และระยะเวลาลบก่อนเริ่ม; ห้ามสมมติ retention period
- รายงาน negative findings และ withdrawals ตามจริง
- ห้ามเติมช่องผลลัพธ์ด้วยข้อมูลจำลอง ผู้วิจัยต้องแยก `test fixture` ออกจาก `participant evidence`

## 13. Readiness Checklist

- [x] Research questions และ failure conditions กำหนดแล้ว
- [x] Warning variants และ counterbalanced order กำหนดแล้ว
- [x] Synthetic scam, legitimate และ emergency tasks กำหนดแล้ว
- [x] Consent/facilitator scripts พร้อม
- [x] Measures, observation และ synthesis templates พร้อม
- [x] Clickable Figma prototype สร้างแล้วและผ่าน structural/reaction audit: 31 screens, 44/44 links, 10 start points
- [ ] Full technical/visual review — visual spot-check ผ่าน 2 หน้าจอ; ยังต้องตรวจ High-Risk/variant screens, contrast, text scaling และ focus order
- [ ] Pilot 1 คนเพื่อตรวจเวลาหรือจุดเสียของ prototype
- [ ] รับสมัครผู้เข้าร่วมจริง 5–8 คน
- [ ] ดำเนิน sessions และกรอกผลจริง
- [ ] Synthesize findings และตัดสิน continue/revise/pivot

Study gate: ห้ามเริ่ม participant sessions 5–8 คนก่อน pilot จริง 1 คนและแก้ Critical/High flow defects แล้ว Automated link audit หรือการตรวจโดยผู้สร้างไม่ถือเป็น participant pilot
