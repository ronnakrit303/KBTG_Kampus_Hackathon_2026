# JobShield — Consolidated Savings Lifecycle (Figma-ready)

> Superseded on 6 September 2026 by [protected-reserve-v5-spec.md](./protected-reserve-v5-spec.md). ไฟล์นี้เก็บ V4 lifecycle ที่เคยแยกช่วงก่อน/หลังเงินเดือนไว้เป็น decision history เท่านั้น

วันที่: 5 กันยายน 2026  
สถานะ: **V4 SPEC READY — NOT APPLIED TO FIGMA CANVAS**; scope approved 6 กันยายน 2026  
Target: [K PLUS JobShield — Clickable Prototype](https://www.figma.com/design/5uoF2s6cq2JMGRFfwmdpc2)  
ขอบเขต: เส้นทางเงินตั้งแต่ช่วงหางานไปจนสร้างเงินสำรองฉุกเฉิน โดยทุกการโอนออกกลับเข้าสู่ Core Track 3 protection flow เดียวกัน

## Product Position

JobShield ใน Prototype มีสามช่วงที่เชื่อมเป็นผลิตภัณฑ์เดียว:

1. **Set up** — ผู้ใช้เลือก career stage และจัดเงินตามช่วงชีวิต
2. **Build** — หลังเริ่มมีรายได้ ช่วยสร้างเงินสำรองฉุกเฉินด้วย Auto-Routing แบบ opt-in และเป้าหมายที่ผู้ใช้กำหนด
3. **Protect** — ประเมินความเสี่ยงเมื่อเงินกำลังออกไปยังผู้รับภายนอก แล้วเลือก Allow, Warn หรือ Cooling-off

K-ePocket ทำหน้าที่แยกเงิน ส่วน JobShield เป็น security policy layer ก่อนโอน ไม่ใช่ Escrow และไม่ใช่บัญชีเงินฝากชนิดใหม่

Current scope ใช้ protected reserve เพียงก้อนเดียว ไม่มี `Job Search Budget`: ก่อนรับเงินเดือนใช้ชื่อ `เงินสำรองก่อนเงินเดือนแรก` และหลังเริ่มมีรายได้จึงเปลี่ยนเป็น `เงินสำรองฉุกเฉิน` เมื่อผู้ใช้ยืนยัน

## Terminology Lock

- `เงินสำรองก่อนเงินเดือนแรก` — เงินระยะสั้นสำหรับช่วงเริ่มงานจนได้รับเงินเดือนก้อนแรก
- `เงินสำรองฉุกเฉิน` — เงินระยะยาวสำหรับเหตุจำเป็นหรือช่วงขาดรายได้ ตั้งเป้าจากค่าใช้จ่ายจำเป็นหลายเดือน
- ห้ามใช้สองคำนี้แทนกันบนหน้าจอเดียวกันโดยไม่มีคำอธิบายการเปลี่ยนผ่าน

## Entry And Transition

```text
S00 เปิด JobShield และเลือก career stage
        ├─ กำลังหางาน/รอเงินเดือนแรก
        │      ↓
        │   S01 สร้างหรือเชื่อมเงินสำรองก่อนเงินเดือนแรก
        │      ↓
        │   ใช้เงินตามบริบท และทุก External Transfer เข้า Protect flow
        │      ↓ เมื่อเริ่มมีรายได้และผู้ใช้ยืนยัน
        └──────→ R00 เปลี่ยนผ่านสู่เงินสำรองฉุกเฉิน
                 ↓
R01 อธิบายเงินสำรอง + ระบุค่าใช้จ่ายจำเป็นต่อเดือน
        ↓
R02 เลือกเป้าหมาย 3 / 6 เดือน / กำหนดเอง
        ↓
R03 ตั้ง Auto-Routing + ดูระยะเวลาประมาณการ
        ↓
R04 ตรวจสอบและให้ความยินยอม
        ↓
R05 Dashboard ความคืบหน้าและแรงจูงใจ
        ↓
R06 ต้องการนำเงินออก
        ├─ บัญชีตนเอง/verified biller → R07A
        ├─ ค่าใช้จ่ายทั่วไป → R07B
        └─ ผู้รับใหม่/สัญญาณ Scam สูง → H05 → H06
```

เงินที่เหลือจาก `เงินสำรองก่อนเงินเดือนแรก` สามารถใช้เป็นยอดตั้งต้นของ `เงินสำรองฉุกเฉิน` ได้เมื่อผู้ใช้ตรวจสอบและยืนยันเองเท่านั้น ระบบห้ามย้ายเงินให้อัตโนมัติ

## Screen Specification

### R00 — Career Stage Transition

- Heading: `เริ่มสร้างเงินสำรองฉุกเฉิน`
- Supporting copy: `คุณจะใช้ยอดเดิมเป็นเงินตั้งต้นหรือเริ่มใหม่ก็ได้ และตั้งแผนออมอัตโนมัติที่ปรับหรือปิดได้ทุกเมื่อ`
- Optional choice: `ใช้เงินที่เหลือเป็นยอดตั้งต้น` / `เริ่มกระเป๋าใหม่`
- Primary: `เริ่มตั้งแผน`
- Secondary: `ไว้ภายหลัง`
- Prototype tag: `เหตุการณ์เงินเดือนเป็นข้อมูลจำลอง`

### R01 — Reserve Goal Input

- Heading: `เตรียมพร้อมเมื่อรายได้สะดุด`
- Copy: `ตั้งเป้าจากค่าใช้จ่ายจำเป็นที่คุณต้องใช้ในแต่ละเดือน เริ่มจากเป้าหมายเล็กแล้วค่อยเพิ่มได้`
- Visual: progress illustration/character แบบเป็นมิตร ไม่แสดงว่าเป็นคำแนะนำการลงทุน
- Input: `ค่าใช้จ่ายจำเป็นต่อเดือน`
- Helper: `เช่น ค่าเช่า ค่าเดินทาง ค่าอาหาร และภาระที่จำเป็น`
- Privacy note: `JobShield ใช้เฉพาะตัวเลขที่คุณกรอกเพื่อคำนวณเป้าหมายนี้`
- ห้ามขอ Resume, อีเมล, ข้อความส่วนตัว หรือรายละเอียดหมวดที่ไม่จำเป็น
- Primary: `เลือกเป้าหมาย`

### R02 — Target Selection

- Options: `3 เดือน`, `6 เดือน`, `กำหนดเอง`
- Formula: `ค่าใช้จ่ายจำเป็นต่อเดือน × จำนวนเดือน`
- Example fixture: `฿15,000 × 3 เดือน = เป้าหมาย ฿45,000`
- User can edit; recommendation is informational, not mandatory

### R03 — Auto-Routing Rule And Estimate

- Choose: fixed amount or percentage of incoming salary
- Example options: `5%`, `10%`, `15%`, `กำหนดเอง`
- User selects source account and expected salary date
- Toggle: `หยุดอัตโนมัติเมื่อถึงเป้าหมาย`
- Implementation boundary: MVP uses a user-configured schedule/synthetic salary event; automatic payroll classification is an internal-data assumption
- Heading: `แผนตามเป้าหมายของคุณ`
- Show rule inputs: target, contribution, estimated months to target
- Copy: `คำแนะนำนี้คำนวณจากข้อมูลที่คุณตั้งไว้ คุณปรับจำนวนได้เสมอ`
- Prototype uses deterministic calculation; do not use `AI`, model score or guaranteed outcome

### R04 — Review And Consent

- Show: source, percentage/fixed amount, destination pocket, cap, next scheduled route
- Consent: `ยืนยันให้แบ่งเงินตามกฎนี้จนถึงเป้าหมาย หรือจนกว่าฉันจะปิด`
- Controls: edit, pause Auto-Routing, delete rule
- No preselected consent checkbox

### R05 — Progress And Motivation

- Progress: current balance / target / estimated months covered
- Example: `ออมแล้ว ฿24,000 จากเป้าหมาย ฿45,000 — ครอบคลุมประมาณ 1.6 เดือน`
- Reinforcement: milestone badge or contribution streak
- Reward card: `แนวคิด K Point ในอนาคต` เท่านั้น และไม่เป็น dependency ของ flow
- K Point ต้องติดป้าย `ต้องผ่าน Business/Product approval`; ไม่แสดงอัตรา earn rate หรือสิทธิที่รับรองแล้ว
- Never punish or remove all progress because a user makes a legitimate emergency withdrawal

### R06 — Withdrawal Context

- User selects amount, destination and broad purpose
- Purpose is one signal, not a bypass switch
- Show remaining balance and estimated months covered before confirmation

### R07A — Legitimate Emergency

- Applies to own account or verified biller
- Copy: `หลังทำรายการ เงินสำรองจะเหลือประมาณ 1.2 เดือนของค่าใช้จ่ายจำเป็น`
- Primary: `ยืนยันใช้เงินฉุกเฉิน`
- Secondary: `กลับไปตรวจสอบ`
- No fixed delay and no High-Risk Scam warning

### R07B — General Spending Nudge

- Friendly character may be used here
- Heading: `ขอชวนคิดอีกครั้งก่อนใช้เงินก้อนนี้`
- Copy: `รายการนี้จะทำให้เงินสำรองของคุณลดลง ฿3,500 คุณยังดำเนินการต่อได้`
- Primary safe action: `เก็บเงินไว้ก่อน`
- Secondary: `ยังต้องการใช้เงิน`
- This is a self-control nudge, not a fraud finding and not a forced Cooling-off
- ผู้ใช้กดทำรายการต่อได้ทันที; Nudge ห้ามสร้าง Pending Instruction

### R07C — High-Risk External Transfer (routing rule; no additional screen)

- Triggered only by multi-signal policy, not by reserve withdrawal alone
- Examples: new personal payee + repeated transfer/job-payment context + simulated destination-risk flag
- Route into existing `H05 contextual warning → H06 Pending Instruction`
- Pause only the transfer instruction and exact amount; do not freeze the whole account or pocket
- Repeated taps must not create duplicate instructions or bypass Cooling-off

## Alert-Fatigue And False-Positive Guardrails

- Internal transfer to the user's own pocket: no warning
- Normal Auto-Routing: quiet confirmation/receipt, not an interruptive alert every cycle
- Own account/verified biller emergency: one clear reminder, no High-Risk flow
- General spending: dismissible nudge; do not accuse the user or recipient
- High-Risk warning: require multiple signals and show only 2–3 observable reasons
- Keep primary action placement consistent; illustration may vary, but color must not be the only risk cue
- Measure warning recall, dismissal, opt-out intent and legitimate task success in formative testing

## Security And PDPA Design Notes

Prototype stores no real customer data. A production design would require:

- data minimization: target amount, user-set rule, source/destination reference and necessary audit indicators only
- clear purpose and per-feature consent; no email/message reading
- encryption in transit and at rest using bank-approved controls
- cryptographic keys kept in approved keystore/key-management infrastructure, not in app code
- least-privilege access, role-based access control and audit logs without unnecessary sensitive content
- explicit retention period and deletion/withdraw-consent handling where applicable
- stronger authentication for changing Auto-Routing rules or releasing a High-Risk Pending Instruction
- idempotency key for each route/transfer so repeated taps cannot duplicate an instruction

Encryption is an implementation requirement, not a visible benefit claim and not something a Figma prototype proves.

## Feasibility Classification

| Item | Prototype | Production claim |
|---|---|---|
| Goal calculator and progress | Feasible with deterministic synthetic data | Plausible |
| User-configured scheduled Auto-Routing | Fully demonstrable | Requires internal KBank/K-ePocket API validation |
| Automatic salary recognition | Simulated event only | Unconfirmed internal-data capability |
| Risk-based withdrawal flow | Reuse existing synthetic JobShield policy | Requires policy, legal and payment-operations validation |
| K Point reward | Concept card only | Requires campaign economics and Business approval |
| Encryption/access control | Documented architecture note | Must use bank-approved standards; not validated by Figma |

## Business Hypotheses — Do Not Present As Proven

- Higher engagement and retention from a visible savings goal
- More consistent balances/deposit relationship
- Fewer preventable Scam transfers may reduce fraud-support and dispute workload
- K Point concept may improve continued contributions

Do not say the bank can simply invest an individual customer's emergency money, and do not quantify acquisition, cost saving, loss reduction or deposit growth without internal evidence.

ดอกเบี้ยพิเศษและอัตราผลตอบแทนแบบขั้นบันไดถูกตัดออกจาก Prototype/Proposal ปัจจุบัน ไม่ใช่ Future card ในหน้าจอ

## Evidence Used

- SET: emergency reserve should remain liquid and is commonly framed as 3–6 times monthly expenses: https://www.set.or.th/th/about/mediacenter/insights/video/1253-ruthunpakthong-emergency-reserve
- Somville & Vandewalle, randomized field experiment on saving by default: https://www.aeaweb.org/articles?id=10.1257/app.20160547
- Anderson et al., security-warning habituation and polymorphic warnings: https://www.jmis-web.org/articles/1304
- FCA: risk-based warnings and positive friction in payment journeys: https://www.fca.org.uk/publications/multi-firm-reviews/anti-fraud-controls-complaint-handling-firms-focus-app-fraud
- KBank K Point public page confirms an existing reward ecosystem, not eligibility for this concept: https://www.kasikornbank.com/th/personal/Digital-banking/kplus-kpoint
- GPPC/PDPC privacy notice illustrates purpose limitation, consent for changed purposes and retention boundaries: https://gppc.pdpc.or.th/privacy-policy/
- OWASP MASVS storage, cryptography and privacy controls: https://mas.owasp.org/MASVS/05-MASVS-STORAGE/ , https://mas.owasp.org/MASVS/06-MASVS-CRYPTO/ , https://mas.owasp.org/MASVS/controls/MASVS-PRIVACY-1/

Evidence supports the problem and design rationale; it does not prove demand, KBank production feasibility or the effectiveness of this exact feature. Those remain validation questions.
