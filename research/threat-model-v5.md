# K PLUS JobShield — V5 Threat Model

สถานะ: Working threat model — 6 กันยายน 2026

ขอบเขต: `เงินสำรองตั้งหลัก + Auto-Routing + Risk-based Protection`

## Security Objective

ลดโอกาสที่ First Jobber จะโอน `เงินสำรองตั้งหลัก` ให้ผู้หลอกลวงภายใต้ social engineering โดยเพิ่ม friction ตามหลายสัญญาณก่อนคำสั่งเข้าสู่ PromptPay ขณะเดียวกันต้องไม่ทำให้เงินถูกล็อกถาวรหรือขัดขวางค่าใช้จ่ายจำเป็น

## Target User And Hero Threat

- Target: First Jobbers อายุ 22–30 ที่กำลังสมัครงาน รอเงินเดือนแรก หรือเริ่มมีรายได้
- ระบบไม่ถามหรืออนุมานสถานะงาน
- Hero threat: Fake Recruiter แอบอ้างบริษัทและขอค่าสมัคร ค่าอบรม ค่าอุปกรณ์ หรือเงินมัดจำไปยังบัญชีบุคคลใหม่
- ผู้ใช้อาจเป็นผู้ยืนยันรายการจริง จึงเป็น authorized transfer under deception ไม่ใช่ account takeover เสมอไป

## Assets

- เงินสำรองตั้งหลักและสภาพคล่องสำหรับค่าใช้จ่ายจำเป็น
- ความสามารถของผู้ใช้ในการหยุด ตรวจสอบ ยกเลิก และรายงานก่อนเงินออก
- ความถูกต้องของ Pending Instruction และ Auto-Routing rule
- ความเป็นส่วนตัวของข้อมูลธุรกรรมและข้อมูลที่ผู้ใช้กรอก
- ความเชื่อมั่นต่อ K PLUS และคำเตือนของระบบ

## Actors

- User: เปิด JobShield กำหนดเป้าหมายและทำรายการ
- Attacker/Fake Recruiter: กดดัน ชี้นำ purpose answer แบ่งยอด หรือเปลี่ยนบัญชีรับเงิน
- K-ePocket: money container/source designation
- K PLUS Transaction + Bank-side Fraud Risk: transaction/payee/destination signals
- K PLUS Security & Fraud Response: warning, verification, Cooling-off และ Cancel/Report

## Trust Boundaries

1. ข้อความ/อีเมลภายนอก K PLUS — JobShield ไม่อ่านเป็นค่าเริ่มต้น
2. User-provided purpose — attacker coach ได้ จึงเป็น weak signal
3. K-ePocket designation — บอกว่าเป็น protected reserve แต่ไม่พิสูจน์ว่า transaction เป็น Scam
4. Simulated destination risk — เป็น integration assumption ไม่ใช่ข้อมูลจริงที่ทีมเข้าถึง
5. Pending Instruction → PromptPay — จุดควบคุมสำคัญ; High transaction ต้องถูกพักก่อนข้าม boundary นี้

## Attack Paths And Controls

| ID | Attack path | Proposed control | Residual risk |
|---|---|---|---|
| T1 | Fake Recruiter ขอให้โอนไปบัญชีใหม่ | multi-signal policy + contextual warning + Cooling-off | new account may have no negative history |
| T2 | Coach ให้ตอบ purpose ผิด | purpose cannot lower tier from other signals | attacker may still persuade user after delay |
| T3 | แบ่งยอดเล็กหลายครั้ง | cumulative/repetition aggregation | distributed recipients can reduce linkage |
| T4 | ใช้บัญชีม้าหรือบัญชีที่เคยดูปกติ | destination-risk integration assumption | risk signal may be incomplete or stale |
| T5 | กดยืนยันรัวหรือแตะซ้ำ | idempotency + one Pending Instruction | implementation defect could duplicate instruction |
| T6 | เปลี่ยน/ปิด JobShield ระหว่าง High flow | current event tier is immutable unless bank risk changes | user can turn protection off for future events |
| T7 | False positive ต่อค่าใช้จ่ายจำเป็น | own/verified neutral route is Low; new neutral route is Medium | verified data may be unavailable |
| T8 | Warning fatigue | High requires multiple signals; general spending uses separate nudge | poorly tuned thresholds can still annoy users |
| T9 | Privacy overreach | transaction data minimization; no inbox/Resume scanning | optional future sharing would need separate consent |
| T10 | Auto-Routing rule ถูกแก้โดยไม่ได้รับอนุญาต | stronger authentication, audit and change confirmation | production control unvalidated in prototype |

## Control Strategy

1. **Set up:** ผู้ใช้สร้าง/เชื่อมเงินสำรองตั้งหลัก ตั้งเป้าหมายและยอดเริ่มต้น
2. **Build:** Auto-Routing เป็น opt-in เปิดภายหลังได้ และมี edit/pause/off/stop-at-goal
3. **Observe:** รับ JobShield state, fund source, payee history, amount/repetition, purpose และ destination-risk assumption
4. **Decide:** deterministic policy เลือก Baseline, Low, Medium หรือ High
5. **Act:** normal flow, contextual warning หรือ Pending Instruction + Cooling-off
6. **Recover:** Cancel/Report และเก็บ audit indicators ที่จำเป็น

## Security Requirements

- **SR-01:** reserve source alone cannot create High
- **SR-02:** purpose answer cannot downgrade a tier
- **SR-03:** split transfers must be aggregated within a policy-defined window
- **SR-04:** High action pauses exact instruction/amount before PromptPay; no whole-account freeze
- **SR-05:** repeated taps are idempotent
- **SR-06:** own account/verified biller with neutral risk has no fixed delay
- **SR-07:** Savings Nudge is dismissible and never creates Pending Instruction
- **SR-08:** Auto-Routing consent is explicit and not preselected
- **SR-09:** changing Auto-Routing requires appropriate authentication and audit
- **SR-10:** system does not read email, messages or Resume by default
- **SR-11:** warnings show 2–3 observable reasons without exposing full thresholds
- **SR-12:** user can continue after agreed conditions; no claim of complete prevention

## Privacy And Data Minimization

- process only necessary app state, reserve designation, transaction/payee features and audit indicators
- do not store real customer data in the prototype
- synthetic names, amounts and destination flags only
- production design requires defined purpose, lawful basis/consent, retention, access control, encryption in transit/at rest and bank-approved key management

## Validation Scenarios

1. fake recruiter + protected reserve + new personal payee + job-payment/elevated risk → High
2. verified rent/bill + neutral risk → Low
3. own-account access + neutral risk → Low
4. new unverified essential payee without High combination → Medium
5. general spending to known payee → Savings Nudge only
6. false purpose and split-transfer bypass attempts remain High when other signals support it

รายละเอียด fixture และ oracle อยู่ใน [synthetic-risk-table-v5.md](./synthetic-risk-table-v5.md)

## Residual Risk Statement

JobShield ลดความเสี่ยงแต่ไม่รับประกันว่าจะหยุด Scam ทุกกรณี ผู้ใช้ที่ยังเชื่อผู้หลอกลวงหลังผ่าน Cooling-off อาจยืนยันต่อได้ และความแม่นยำจริงขึ้นกับข้อมูล นโยบาย และการทดสอบ production ที่ Prototype นี้ไม่สามารถพิสูจน์ได้
