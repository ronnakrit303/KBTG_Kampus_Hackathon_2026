# Phase A — Understanding & Research Plan

สถานะ: Evidence/novelty และ threat-model/risk-table/content-skeleton milestones completed 4 กันยายน 2026; final Proposal ยังไม่เริ่ม  
ขอบเขตของเอกสารนี้: แยกสิ่งที่ทราบออกจากสมมติฐาน วางแผนวิจัย และระบุคำถามก่อนล็อกแนวคิด ยังไม่ใช่ Proposal

> อัปเดต 4 กันยายน 2026: ตรวจแหล่งทางการด้าน fake-job payment scam, K PLUS/K-ePocket/MAKE, KBank anti-fraud controls และ signal feasibility แล้ว ผล research gates คือผ่านแบบมี claim/scope limits ดู `research/user-problem.md`, `research/competitor-gap.md`, `research/signal-feasibility.md` และ `research/sources.md`

## 1. หลักฐานที่มีอยู่ใน repository

- `AGENTS.md` เป็น working brief และข้อกำหนดการทำงาน
- `research/sources.md` บันทึกแหล่งข้อมูล วันที่เข้าถึง สิ่งที่รองรับ และข้อจำกัดของแต่ละ claim
- `research/user-problem.md` สรุปหลักฐานปัญหาและขอบเขต claim ต่อ First Jobbers
- `research/competitor-gap.md` เปรียบเทียบ K PLUS, K-ePocket, MAKE, money lock และมาตรการ anti-fraud
- `research/signal-feasibility.md` แยก bank-visible/derived signals ออกจาก integration assumptions
- ยังไม่มี user interview/usability result, Resume/CV, สำเนา Google Form ครบทุกหน้า หรือ final Proposal

## 2. การแยกสถานะข้อมูล

### 2.1 ข้อมูลผู้สมัครที่ใช้เป็นบริบทได้

ข้อมูลกลุ่มนี้เป็นข้อมูลที่ผู้สมัครให้ไว้ ใช้ปรับทิศทางงานได้ แต่ต้องไม่ขยายความเกินจริง:

- เป็นนักศึกษา Computer Science มหาวิทยาลัยธรรมศาสตร์
- สนใจและมีประสบการณ์ฝึกปฏิบัติด้าน Cyber Security, threat detection, network/endpoint security, fraud detection และ digital trust
- เคยใช้ Wazuh SIEM, Wireshark, Linux, Python, Bash, Docker และทำงานฝึกด้าน phishing, SSH brute force, IOC, incident reporting และ MITRE ATT&CK
- เคยทำแนวคิดตรวจจับบัญชีม้าจากพฤติกรรมธุรกรรมและความสัมพันธ์แบบกราฟ
- ต้องการให้ผลงานสอดคล้องกับการสมัคร Cyber Security internship ที่ KBTG

### 2.2 ข้อมูลจากผู้จัดตามที่บันทึกใน AGENTS.md — ต้องตรวจต้นฉบับ

- โจทย์คือออกแบบ feature/function/service/solution/digital experience ใหม่ใน K PLUS เพื่อช่วย First Jobbers จัดการการเงินและการออม พร้อมลดความเสี่ยง Scam หรือ Fraud
- กลุ่มเป้าหมายคือ First Jobbers อายุ 22–30 ปี
- สมัครเดี่ยวหรือทีมไม่เกิน 3 คน
- Track ที่เลือกคือ Track 3 — Cyber Security & Digital Trust ตำแหน่ง Cyber Security
- รอบสมัครต้องใช้ Resume/CV และ one-page pitch proposal แบบ PDF ซึ่งมี 5 ส่วน: Problem Statement, Proposed Solution, Target Users, Value Proposition และ Track Perspective
- กำหนดส่งที่บันทึกไว้คือ 21 กันยายน 2026 และงานระบุว่าดำเนินเป็นภาษาไทย
- มีลิงก์ Google Form และอีเมลผู้จัดสองรายตามที่บันทึกไว้

สถานะ: ยังไม่ถือว่า verified เพราะ repository ไม่มีประกาศต้นฉบับหรือสำเนาแบบฟอร์ม และข้อมูลอาจเปลี่ยนได้

### 2.3 ข้อมูลผลิตภัณฑ์/มาตรการจากหน้าเว็บทางการ — ตรวจรอบล่าสุดแล้ว

`AGENTS.md` รายงานว่า:

- K PLUS มีสรุปรายรับรายจ่าย เครื่องมือสนับสนุนการออม และ K-ePocket
- K-ePocket แยกเงินเป็นส่วนใช้จ่าย ออม และเป้าหมายได้
- MAKE by KBank มี Cloud Pocket, budgeting, saving goals และการจัดหมวดธุรกรรม
- KBank มีมาตรการบางส่วน เช่น risk-aligned transaction limits, facial verification, suspicious destination detection, alerts และ fraud-reporting support

สถานะ ณ 4 กันยายน 2026: ตรวจหน้า public product/control แล้วและใช้สรุป novelty แบบมีข้อจำกัดได้ การไม่พบ end-to-end flow ใน public sources ไม่ยืนยันว่าไม่มีระบบภายในที่คล้ายกัน

### 2.4 สมมติฐานของแนวคิดที่ยังไม่มีหลักฐานพอ

- First Jobbers มี pain point เฉพาะที่รุนแรงพอในจังหวะนำเงินฉุกเฉิน/เงินเป้าหมายออกไปโอนภายใต้แรงกดดันจากมิจฉาชีพ
- การผูก “Protected Savings” เข้ากับ contextual scam intervention เป็นช่องว่างที่ K PLUS/MAKE/K-ePocket ยังไม่มี
- ผู้ใช้ต้องการ Safe-to-Spend และ Protected Savings ใน flow เดียวกัน และจะเข้าใจคุณค่าได้ทันที
- สัญญาณ เช่น new payee, unusual amount/time, protected-fund withdrawal, device/session change, behavioral anomaly และ recipient-risk relationship มีให้ใช้จริงหรือจำลองอย่างสมเหตุผล
- risk score และ explainable warning จะช่วยให้ผู้ใช้หยุดคิดได้ โดยไม่สร้าง false positives, warning fatigue หรือภาระเกินยอมรับ
- stronger verification หรือ cooling-off step ลดความเสียหายได้ แม้ผู้ใช้เชื่อมิจฉาชีพและตั้งใจยืนยันทุกขั้นตอน
- Rapid Response สามารถ pause ธุรกรรมหรือเชื่อมกระบวนการ fraud response ได้ตามข้อจำกัดจริงของธนาคาร
- แนวคิดนี้มี Track 3 เป็นแกน ไม่ถูกมองว่าเป็น budgeting feature หรือ data-science scoring project
- K PLUS ควรสร้างคุณสมบัตินี้เอง และคุณค่าที่เพิ่มขึ้นเหนือมาตรการเดิมมากพอกับต้นทุน/ความเสี่ยง
- สามารถวัดผลลัพธ์ด้าน security, user experience และ business value ได้อย่างน่าเชื่อถือโดยไม่ใช้ข้อมูลลูกค้าจริง

### 2.5 เรื่องที่ต้องค้นคว้าก่อนล็อกแนวคิด

- ข้อกำหนดล่าสุดของผู้จัด: deadline, ภาษา,รูปแบบไฟล์/ขนาดไฟล์, เกณฑ์ตัดสิน, prototype expectation และข้อจำกัดทีม
- นิยามและพฤติกรรมทางการเงินจริงของ First Jobbers ไทยอายุ 22–30: รายได้ ค่าใช้จ่าย หนี้ เงินสำรอง การออม และ financial stress โดยไม่เหมารวมจาก Gen Z ทั้งหมด
- Scam/Fraud ที่กระทบคนกลุ่มนี้: ประเภทเหตุการณ์ ช่องทาง การโน้มน้าว ลำดับเหตุการณ์ จำนวน/แนวโน้มความเสียหาย และ “จังหวะก่อนเงินออก” ที่ระบบยังแทรกแซงได้
- ความสามารถล่าสุดและข้อจำกัดของ K PLUS, K-ePocket, MAKE by KBank และมาตรการ anti-fraud ของ KBank
- ความแตกต่างระหว่างแนวคิดกับมาตรการของธนาคารอื่น/แนวปฏิบัติที่มีอยู่ เพื่อหลีกเลี่ยงการอ้าง novelty เกินจริง
- ความเป็นไปได้ของข้อมูลและระบบ: สัญญาณใดอยู่ใน mobile app, transaction system, fraud engine หรือเป็นข้อมูลภายในที่เราไม่มีสิทธิ์สมมติ
- หลักฐานด้านพฤติกรรมว่าคำเตือนแบบ contextual, friction, cooling-off, beneficiary confirmation หรือ human escalation แบบใดช่วยลดการหลอกโอนได้
- ข้อกำกับเรื่อง privacy, consent, accessibility, auditability และสิทธิผู้ใช้ โดยเฉพาะเมื่อแตะข้อมูลอุปกรณ์/พฤติกรรมหรือการชะลอธุรกรรม
- ขอบเขต demo ที่ทำได้ด้วย synthetic data และไม่อ้างว่าเชื่อมระบบธนาคารจริง

## 3. แผนวิจัย

### ผล milestone 4 กันยายน 2026

- Workstream B: ผ่านแบบจำกัด claim — fake-job/recruitment-payment scam มีหลักฐานทางการ แต่ยังไม่มี comparative evidence ว่า First Jobbers 22–30 เสี่ยงกว่ากลุ่มอื่น
- Workstream D: ผ่านแบบต้องลด scope — pockets, money lock, destination risk, face verification, alert และ report path มีอยู่แล้ว; novelty เหลือที่ scenario-aware orchestration
- Workstream E: ผ่านระดับ concept/prototype — core ใช้ Career Mode state, source pocket, payee history, amount/repetition และ simulated destination-risk flag ได้; production data/authority ยังต้องเป็นสมมติฐาน
- Workstream C: เสร็จระดับ working prototype specification แล้วใน `research/threat-model.md` และ `research/synthetic-risk-table.md`; ยังต้อง cross-review และ validate ผ่าน Figma/usability test
- Workstream A: deadline และ team limit ตรวจจาก KBTG official LinkedIn แล้ว; ภาษา/ขนาดไฟล์/prototype requirement ยังต้องตรวจจาก form/ประกาศเต็มก่อน final submission

### Workstream A — ยืนยันโจทย์และข้อกำหนดการสมัคร (Priority 0)

คำถาม: ต้องส่งอะไร เมื่อไร ภาษาใด และกรรมการประเมินจากอะไร  
แหล่งหลัก: ประกาศ KBTG/KBank, หน้าโครงการ และ Google Form ที่ผู้จัดให้  
ผลลัพธ์: `research/sources.md` ส่วน organizer facts พร้อม URL, วันที่เข้าถึง, ข้อความสรุป และภาพ/สำเนาหลักฐานเมื่อเหมาะสม  
เกณฑ์ผ่าน: ทุกข้อกำหนดที่เข้า Proposal ตรวจย้อนกลับไปยังต้นฉบับได้

### Workstream B — First Jobber problem evidence (Priority 1)

คำถาม: ปัญหาการเงินและ Scam/Fraud ใดเกิดกับคนเริ่มทำงานอายุ 22–30 อย่างมีหลักฐาน และอะไรเป็น pain point เฉพาะกลุ่ม  
แหล่งหลัก: ธนาคารแห่งประเทศไทย, สำนักงานสถิติแห่งชาติ, สภาพัฒน์, หน่วยงานกำกับ/งานวิจัยต้นฉบับ และงานวิจัยเชิงพฤติกรรมที่ระบุกลุ่มอายุชัดเจน  
วิธี: แยกข้อมูล “First Jobber โดยตรง” ออกจากข้อมูล “Gen Z/วัยทำงานโดยอนุมาน”; เก็บปี กลุ่มตัวอย่าง วิธีวิจัย และข้อจำกัด  
ผลลัพธ์: `research/user-problem.md` ที่สรุป 2–3 pain points, user scenario และหลักฐานตรง/หลักฐานอนุมาน  
เกณฑ์ผ่าน: เลือกได้หนึ่งสถานการณ์เสี่ยงที่เฉพาะเจาะจง เกิดก่อนธุรกรรมเสร็จ และเชื่อมกับการจัดการเงิน/เงินออมจริง

### Workstream C — Scam/Fraud threat journey (Priority 1)

คำถาม: ผู้โจมตีเข้าหา โน้มน้าว และพาเหยื่อโอนเงินอย่างไร; control ใดมีโอกาสหยุดเหตุการณ์ ณ จุดใด  
แหล่งหลัก: ศูนย์ AOC 1441/กระทรวงดิจิทัลฯ, ตำรวจไซเบอร์ (CCIB), ธปท., ปปง., สมาคมธนาคารไทย และสถิติ/คำเตือนทางการ  
วิธี: สร้าง threat model แยก victim, attacker, asset, attack path, trust boundary, observable signal และ intervention point; ไม่รวมตัวเลขจากข่าวรองหากย้อนหาต้นทางไม่ได้  
ผลลัพธ์: แผนภาพ attack journey 1–2 แบบ และตาราง signal → risk → control → failure mode  
เกณฑ์ผ่าน: อธิบายได้ว่าระบบแทรกแซง “เมื่อไร เพราะอะไร และถ้าผู้ใช้กดยืนยันต่อจะเกิดอะไรขึ้น”

### Workstream D — KBank capability and novelty gap (Priority 1)

คำถาม: K PLUS/K-ePocket/MAKE และ anti-fraud controls ทำอะไรได้แล้ว; แนวคิดเพิ่ม control ใหม่จริงหรือเพียงรวมของเดิม  
แหล่งหลัก: หน้า K PLUS, K-ePocket, MAKE by KBank, KBank cyber-risk/anti-fraud, เงื่อนไขผลิตภัณฑ์และ FAQ ทางการ; ใช้ app-store material เป็นหลักฐานรองและระบุวันที่  
วิธี: ทดลอง/บันทึก user flow ได้เฉพาะสิ่งที่ผู้สมัครเข้าถึงอย่างถูกต้อง; ห้ามอนุมานระบบหลังบ้านจากหน้าจอ  
ผลลัพธ์: `research/competitor-gap.md` เป็น feature/control matrix: existing, proposed, overlap, unresolved, evidence  
เกณฑ์ผ่าน: เขียน novelty statement ที่แคบ ตรวจสอบได้ และไม่กล่าวว่า KBank “ไม่มี” สิ่งใดหากยังพิสูจน์ไม่ได้

### Workstream E — Intervention evidence, feasibility, privacy (Priority 2)

คำถาม: intervention แบบใดมีหลักฐานสนับสนุน; ต้องใช้ข้อมูลอะไร; friction และสิทธิผู้ใช้จะถูกควบคุมอย่างไร  
แหล่งหลัก: เอกสาร regulator/industry, มาตรฐาน/งานวิจัยต้นฉบับด้าน scam warnings, risk-based authentication, privacy และ human factors  
วิธี: ทำ data-availability matrix แยก public-known, reasonable bank-side assumption และ unavailable/unsafe; ระบุ false-positive และ evasion cases  
ผลลัพธ์: minimum viable control, privacy constraints, fallback/emergency path และรายการสิ่งที่ demo ด้วย synthetic data  
เกณฑ์ผ่าน: core solution ไม่ต้องอ่านแชต/สายโทรโดยปริยาย ไม่พึ่งข้อมูลภายในที่ไม่ระบุเป็นสมมติฐาน และยังทำ demo ได้

### Workstream F — Synthesis and decision gate

เปรียบเทียบอย่างน้อย 3 solution directions ด้วยเกณฑ์เดียวกัน: ความรุนแรงของปัญหา, evidence strength, Track 3 fit, novelty gap, data feasibility, user friction, demoability และ value ต่อ K PLUS  
ผลลัพธ์: decision matrix, assumptions log, success/failure criteria และข้อเสนอแนะว่าจะไปต่อ/ปรับ/ยกเลิกแต่ละทาง  
เงื่อนไขก่อนเข้า Phase B/C: Workstream A–D ต้องมีหลักฐานขั้นต่ำและไม่มี critical unknown ที่ทำให้ core concept เปลี่ยนโดยสิ้นเชิง

## 4. คำถามสำคัญก่อนล็อกแนวคิด

1. First Jobber ถูกเสี่ยงด้วย Scam/Fraud แบบใดเป็นพิเศษ และมีหลักฐานแยกจากประชาชนทั่วไปหรือไม่?
2. เหตุการณ์ใช้งานหนึ่งเหตุการณ์ที่เราจะชนะคืออะไร: ใครกำลังจะโอนเงินอะไร ให้ใคร ภายใต้แรงกดดันแบบใด?
3. ปัญหาหลักคือการจัดเงินไม่ดี การถูก social engineering หรือการป้องกันเงินสำรอง—และเหตุใดจึงต้องแก้สองมิตินี้ร่วมกัน?
4. K PLUS, K-ePocket, MAKE และ anti-fraud control ปัจจุบันหยุดตรงไหน แล้วช่องว่างที่พิสูจน์ได้คืออะไร?
5. เหตุใด Protected Savings จึงเป็น security control ใหม่ ไม่ใช่ saving pocket เดิมที่เพิ่มคำเตือน?
6. สัญญาณขั้นต่ำที่จำเป็นมีอะไรบ้าง แหล่งข้อมูลอยู่ที่ใด และข้อใดเป็นเพียงสมมติฐานเกี่ยวกับระบบธนาคาร?
7. ระบบจะทำอะไรแตกต่างกันสำหรับ low/medium/high risk และใครมีสิทธิ์ override?
8. ถ้าผู้ใช้เชื่อมิจฉาชีพเต็มที่และยืนยันทุกขั้น ระบบยังลดความเสียหายได้อย่างไรโดยไม่กักเงินผู้ใช้เกินควร?
9. จะลด false positives, warning fatigue, การขัดขวางเหตุฉุกเฉิน และผลกระทบต่อผู้ใช้ที่มีพฤติกรรมไม่สม่ำเสมออย่างไร?
10. ผู้โจมตีจะเลี่ยงระบบด้วยการแบ่งยอด เปลี่ยนเวลา ใช้บัญชีใหม่ หรือฝึกเหยื่อให้ตอบ warning อย่างไร?
11. จะอธิบายเหตุผลความเสี่ยงให้ผู้ใช้เข้าใจ โดยไม่เปิดรายละเอียดที่ช่วยผู้โจมตีหลบ rule/model ได้อย่างไร?
12. ต้องเก็บข้อมูลใดจริง ข้อมูลใดไม่ควรเก็บ และ consent/accessibility/auditability จะออกแบบอย่างไร?
13. prototype ใดพิสูจน์ core hypothesis ได้ด้วย synthetic data โดยไม่แสร้งว่าเข้าถึง KBank internal APIs?
14. metric ใดบอกว่า control ช่วยจริง: detection/precision, cancellation/pause, warning comprehension, legitimate-task time หรือ protected-fund retention?
15. อะไรคือ failure condition ที่ทำให้ควรตัด feature นี้หรือเปลี่ยน direction?
16. เหตุใด K PLUS ควรสร้างสิ่งนี้ แทนการปรับคำเตือน/limit/verification ที่มีอยู่ และเหตุใดแกนหลักจึงเป็น Track 3 ไม่ใช่ Track 2?

## 5. ข้อมูลจากผู้สมัครที่ยังต้องยืนยันก่อนวางแผน Phase B

- สมัครเดี่ยวหรือทีม และถ้าเป็นทีม สมาชิกมีทักษะอะไร
- ภาษาที่ต้องการใช้ในเนื้อหา Proposal (คงหัวข้อภาษาอังกฤษไว้จนกว่าจะตัดสินใจ)
- เวลาที่ทำงานได้จริงต่อสัปดาห์และวันที่ต้องการ freeze เนื้อหาก่อน 21 กันยายน 2026
- ต้องการทำ prototype ก่อนส่งรอบแรกหรือเตรียมไว้เฉพาะกรณีผ่านเข้ารอบ
