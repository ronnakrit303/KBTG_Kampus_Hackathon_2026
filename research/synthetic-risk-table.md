# K PLUS JobShield — Synthetic Risk Policy & Test Table

> Superseded on 6 September 2026 by [synthetic-risk-table-v5.md](./synthetic-risk-table-v5.md). ไฟล์นี้เก็บ V4 policy ที่เคยใช้ career stage และชื่อเงินสำรองเดิมไว้เป็น prior specification

สถานะ: Working prototype specification; Build/Protect scope synced — 6 กันยายน 2026
ขอบเขต: deterministic policy สำหรับทดสอบ user flow ด้วยข้อมูลสมมติทั้งหมด  
ไม่ใช่: KBank production rule, fraud score, model accuracy claim หรือ final Proposal

## 1. Policy Goal

เลือก friction ให้เหมาะกับความเสี่ยงก่อนโอน โดยใช้หลายสัญญาณร่วมกันและรักษาสาม invariant:

1. คำตอบที่ผู้ใช้กรอกเองเพิ่มบริบทได้ แต่ไม่ใช้ลด risk tier ที่มาจากสัญญาณอื่น
2. ยอดเล็กหลายครั้งต้องถูกพิจารณาเป็น cumulative pattern ไม่ใช่แยกทุกครั้ง
3. การใช้เงินสำรองก่อนเงินเดือนแรกหรือเงินสำรองฉุกเฉินไม่เท่ากับ Scam โดยอัตโนมัติ; own account/verified biller ต้องมีทางผ่าน
4. `Savings Nudge` เป็นคำเตือนด้านวินัยการเงินที่กดข้ามได้ ไม่ใช่ risk tier และไม่มีสิทธิ์สร้าง Cooling-off

## 2. Synthetic Input Schema

| Field | Synthetic values | Source class | หมายเหตุ |
|---|---|---|---|
| `jobshield_enabled` | on / off | Proposed app state | ผู้ใช้ opt-in และปิดได้ |
| `career_stage` | job-search / waiting-first-salary / earning | User-provided context | ใช้เพิ่มบริบท แต่ห้ามลด risk tier โดยลำพัง |
| `fund_source` | บัญชีหลัก / เงินสำรองก่อนเงินเดือนแรก / เงินสำรองฉุกเฉิน | User-designated context | JobShield เพิ่มบริบทให้ protected reserve ก้อนเดียวที่เปลี่ยนวัตถุประสงค์ตามช่วงชีวิต; บัญชีหลักใช้แสดง baseline |
| `destination_class` | own account / verified biller / new unverified payee / known payee | Derived or assumed | `verified biller` ใช้เป็น test fixture ไม่อ้าง employer network จริง |
| `payee_history` | first-seen / seen before | Derived transaction feature | ไม่อ้างว่า KBank ใช้ feature นี้จริงใน fraud engine |
| `purpose_answer` | planned expense / job fee / emergency / other / skipped | User-provided | เป็น weak signal; ไม่มีสิทธิ์ลด tier |
| `transfer_pattern` | single / repeated / split-cumulative | Derived synthetic history | window และ threshold จริงยังไม่กำหนด |
| `destination_risk` | neutral / elevated / high | Simulated bank-side flag | แทน integration กับ control ที่มีอยู่ในระดับ high-level |
| `amount` | ค่าเงินบาทสมมติ | Transaction field | จำนวนใช้เล่า scenario ไม่ใช่ threshold เชิงนโยบาย |

## 3. Risk-Tier Actions

| Tier | Prototype action | UX requirement | User authority |
|---|---|---|---|
| Low | ทำรายการตาม flow ปกติ | ไม่แสดงคำเตือน Scam ที่ไม่จำเป็น | ผู้ใช้ยืนยันตามขั้นปกติ |
| Medium | Contextual warning + deliberate confirmation | แสดงเหตุผล 1–2 ข้อและทางเลือก `Pause & Verify` | ยืนยันต่อได้โดยไม่ใช้ High-Risk cooling-off |
| High | พัก Pending Instruction ก่อนส่งเข้าสู่ระบบโอน/PromptPay + Cooling-off + independent verification path | เหตุผล 2–3 ข้อ, ชื่อแหล่งเงินและจำนวน protected reserve ที่เสี่ยง, `Pause & Verify`, `Cancel/Report` | ทำต่อได้เมื่อครบเงื่อนไข; ไม่มี permanent lock |
| Baseline | JobShield-specific policy ไม่ทำงาน | ใช้ controls ปกติของธนาคาร | ใช้สำหรับวัด adoption gap เมื่อ JobShield off |

ไม่มีการกำหนดระยะ cooling-off, score, weight หรือ probability ใน prototype เพราะยังไม่มีข้อมูล/อำนาจเชิงนโยบายรองรับ

## 4. Deterministic Rule Precedence

ประเมินกฎที่เกี่ยวข้องทั้งหมดและใช้ tier สูงสุด; `P0` ใช้เฉพาะเมื่อ JobShield ปิดและไม่มี existing bank-risk outcome ที่จำลอง:

| Rule | Condition | Tier | Rationale |
|---|---|---|---|
| P0 | `jobshield_enabled = off` และไม่มี existing bank-risk outcome ที่จำลอง | Baseline | แสดงขอบเขตว่า JobShield เป็น opt-in context layer |
| P1 | `destination_risk = high` | High | purpose/self-report ต้องไม่ override bank-side risk |
| P2 | `destination = new unverified` + `fund_source = protected reserve` + (`purpose = job fee` หรือ `transfer_pattern = repeated/split` หรือ `destination_risk = elevated`) | High | red-flag combination ที่เชื่อมเงินสำคัญ ผู้รับใหม่ และบริบท/พฤติกรรมธุรกรรม |
| P3 | `destination = new unverified` + `transfer_pattern = split-cumulative` + (`jobshield_enabled = on` หรือ `destination_risk = elevated`) | High | ป้องกันการหลบด้วยยอดเล็กหลายครั้ง |
| P4 | `jobshield_enabled = on` + `destination = new unverified`; ยังไม่เข้าเงื่อนไข High | Medium | เพิ่มการตรวจผู้รับใหม่โดยยังไม่กล่าวหาปลายทาง; career stage และ contextual signal อื่นใช้เพิ่มเหตุผล |
| P5 | `destination = own account/verified biller` + `destination_risk = neutral` | Low | trusted route/limited break-glass ลด false positive และ emergency harm |
| P7 | อื่น ๆ ที่ JobShield เปิดและไม่มี signal ร่วมเพียงพอ | Low | source, career stage หรือ purpose เพียงตัวเดียวไม่เพียงพอให้เตือนแรง |

ข้อจำกัด: `destination_class` และ `destination_risk` เป็น fixture ของ prototype บางส่วน ไม่ใช่การยืนยัน interface หรือ coverage ของระบบจริง

## 5. Boundary Scenario Table

ชื่อบุคคล บริษัท บัญชี และจำนวนเงินต่อไปนี้เป็นข้อมูลสมมติทั้งหมด

| ID | Boundary case | Synthetic inputs | Triggered rule | Expected tier | Observable reasons shown | Expected action / oracle |
|---|---|---|---|---|---|---|
| BC1-A | Fake recruiter ขอ “ค่าอุปกรณ์” จากเงินสำรองก่อนเงินเดือนแรก | JobShield on; stage=waiting-first-salary; reserve-before-first-salary; ฿7,900; new unverified; first-seen; purpose=job fee; single; elevated | P2 | High | ผู้รับใหม่; แตะเงินสำรองก่อนเงินเดือนแรก; การจ่ายเพื่อเริ่มงาน | พักเป็น Pending Instruction ก่อนส่งเข้าสู่ระบบโอน/PromptPay แสดง Cooling-off และ `Pause & Verify`/`Cancel/Report` |
| BC1-B | Fake recruiter ใช้บัญชีใหม่ที่ bank flag สูง | JobShield on; stage=job-search; reserve-before-first-salary; ฿3,500; new unverified; purpose=other; single; high | P1 | High | ปลายทางมีสัญญาณเสี่ยง; ผู้รับใหม่ | คำตอบ “other” ต้องไม่ลด tier; ต้องเข้าทาง High |
| BC2-A | จ่ายค่าเช่าที่พักผ่านช่องทางตรวจสอบแล้ว | JobShield on; stage=waiting-first-salary; reserve-before-first-salary; ฿4,500; verified biller; essential expense; single; neutral | P5 | Low | แสดงแหล่งเงินและยอดคงเหลือตามปกติ ไม่แสดง Scam warning | ค่าใช้ชีวิตที่ถูกต้องสำเร็จโดยไม่มี High-Risk friction |
| BC2-B | ค่าใช้ชีวิตจริงแต่โอนไปผู้รับใหม่ | JobShield on; stage=waiting-first-salary; reserve-before-first-salary; ฿900; new unverified; essential expense; single; neutral | P4 | Medium | ผู้รับนี้ยังไม่เคยได้รับเงิน; ปลายทางยังไม่ verified | เตือนแบบไม่กล่าวหา ผู้ใช้ Pause เพื่อตรวจหรือยืนยันอย่างตั้งใจได้ |
| BC3-A | เหตุฉุกเฉิน โอนเงินสำรองฉุกเฉินไปบัญชีตนเอง | JobShield on; stage=earning; emergency reserve; ฿6,000; own account; emergency; single; neutral | P5 | Low | แสดงผลกระทบต่อยอดคงเหลือ แต่ไม่แสดง Scam warning | limited break-glass; ทำรายการตามขั้นปกติ |
| BC3-B | จ่ายค่ารักษาจากเงินสำรองฉุกเฉิน | JobShield on; stage=earning; emergency reserve; ฿4,500; verified biller; emergency; single; neutral | P5 | Low | แสดงจำนวนเดือนที่เหลือ แต่ไม่แสดง Scam warning | ไม่เกิด fixed Cooling-off ที่ทำให้เสียหายจากความล่าช้า |
| BC3-C | ถอนเงินสำรองฉุกเฉินเพื่อซื้อของทั่วไปให้ผู้รับเดิม | JobShield on; stage=earning; emergency reserve; ฿3,500; known payee; other; single; neutral | P7 | Low + Savings Nudge | เงินสำรองจะลดลงและเหลือครอบคลุมกี่เดือน | Nudge กดข้ามได้ทันที; ห้ามสร้าง Pending Instruction หรืออ้างว่าเป็น Scam |
| BC4-A | Attacker coach ให้ตอบ purpose ผิด | JobShield on; stage=waiting-first-salary; reserve-before-first-salary; ฿4,900; new unverified; other; repeated; elevated | P2 | High | ผู้รับใหม่; แตะ protected reserve; มีการโอนซ้ำ/สัญญาณปลายทาง | false purpose ห้าม downgrade; High action เหมือนเดิม |
| BC4-B | Attacker แบ่งยอดเพื่อหลบ threshold | JobShield on; stage=job-search; reserve-before-first-salary; 3 × ฿1,500 ในช่วงสั้น; new unverified; other; split-cumulative; elevated | P3 | High | โอนหลายครั้งไปผู้รับใหม่; ยอดสะสม; สัญญาณปลายทาง | รวมเหตุการณ์ก่อนประเมิน; ห้ามมองแต่ยอดล่าสุด |
| BASE-1 | ผู้ใช้ไม่ได้เปิด JobShield | JobShield off; บัญชีหลัก; ฿2,000; new unverified; skipped; single; neutral | P0 | Baseline | ไม่มี JobShield-specific message | ใช้ controls ปกติของธนาคาร; บันทึกเป็น adoption limitation |

## 6. Negative And Conflict Tests

| Test | Mutation | Expected result |
|---|---|---|
| N1 — Purpose downgrade resistance | เปลี่ยน BC1-A จาก `job fee` เป็น `other` แต่เพิ่ม repeated/elevated signal | ยังคง High ตาม P2/P3 |
| N2 — Source-only restraint | JobShield on + protected reserve + known payee + single + neutral | Low; protected reserve เพียงอย่างเดียวไม่ควรถูก block และ Savings Nudge ต้องไม่กลายเป็น Fraud warning |
| N3 — Verified destination precedence | BC2-A เปลี่ยน purpose เป็น `job fee` แต่ปลายทางเป็น verified billerและไม่มี signal อื่น | Low; purpose เพียงอย่างเดียวไม่สร้าง High |
| N4 — Destination-risk override | BC2-A เปลี่ยน destination risk เป็น high | High ตาม P1; verified label ห้ามกลบ current risk signal |
| N5 — Emergency to new payee | BC3-A เปลี่ยน own account เป็น new unverified | Medium เป็นอย่างน้อย; emergency answerไม่ใช่ bypass |
| N6 — Split-memory | ประเมินเฉพาะรายการที่สามของ BC4-B โดยไม่มี history | ถือว่าทดสอบไม่ผ่าน เพราะระบบต้อง aggregate history ก่อน policy |
| N7 — State toggle during warning | ปิด JobShieldหรือเปลี่ยน career stage หลังเกิด High event | High event ปัจจุบันไม่ถูก downgrade; การเปลี่ยนมีผลกับรายการถัดไปตาม policy |

## 7. Warning Content Fixtures

### Medium fixture

- Heading: `ตรวจสอบผู้รับก่อนโอน`
- Reasons: `คุณยังไม่เคยโอนให้บัญชีนี้` และ `ปลายทางนี้ยังไม่ใช่ verified biller`
- Actions: `Pause & Verify` เป็น primary; `ยืนยันต่อ` เป็น secondary
- Tone: ไม่ใช้คำว่า “บัญชีมิจฉาชีพ” เมื่อหลักฐานไม่เพียงพอ

### High fixture

- Heading: `พักรายการนี้และตรวจสอบก่อน`
- Reasons สูงสุดสามข้อจาก: new payee, การใช้ protected reserve, repeated/cumulative transfers, destination-risk, job-payment context
- Impact: แสดงชื่อแหล่งเงินและจำนวน protected reserve ที่จะลดลงหากทำรายการ
- Actions: `Pause & Verify` และ `Cancel/Report`; continuation แสดงหลังผ่าน cooling-off/verification condition
- Detail: weights/thresholds อยู่หลังระบบและไม่แสดงในข้อความหลัก

ข้อความทั้งหมดเป็น content fixture สำหรับ usability test ยังไม่ใช่ final UI copy

## 8. Synthetic Event Log For Auditability

แต่ละ test event เก็บเฉพาะ:

- scenario/test ID
- input categories ที่ไม่ใช่ข้อมูลจริง
- rules ที่ trigger
- expected/actual tier
- reasons ที่แสดง
- user action: continue / pause / cancel / report / break-glass
- timestamps สมมติเพื่อทดสอบ sequence

ไม่เก็บ email/chat content, Resume, credential, เลขบัญชีจริง หรือข้อมูลลูกค้า

## 9. Prototype Acceptance Criteria

- ทั้ง BC1-A และ BC1-B ไป High ก่อน payment instruction
- BC2-A และ BC3-A/BC3-B สำเร็จโดยไม่มี High-Risk cooling-off
- BC3-C แสดง Savings Nudge ที่กดข้ามได้ โดยไม่สร้าง Pending Instruction
- BC2-B อยู่ Medium และใช้ภาษาที่ไม่กล่าวหา
- BC4-A ไม่ถูกลดระดับด้วย false purpose
- BC4-B ตรวจจาก cumulative history และไป High
- เหตุผลทุกหน้ามาจาก input ที่ผู้ใช้สังเกตได้ไม่เกินสามข้อ
- ผู้ใช้มี Cancel/Report และไม่มีข้อความรับประกันว่าจะกู้เงินคืน
- ไม่มีการอ้าง accuracy, loss reduction หรือ production KBank API

## 10. Metrics For Later Formative Test

รายงานเป็น exploratory result เท่านั้น:

- warning comprehension
- Pause/Cancel choice ใน scam scenarios
- legitimate task completion
- task time และ friction feedback
- warning-dismissal behavior
- ความเข้าใจว่า protected reserve/new payee/repetition เพิ่มความเสี่ยงเมื่อใช้ร่วมกันอย่างไร และแยก Savings Nudge จาก Fraud/Scam warning ได้หรือไม่

จำนวนผู้ทดสอบเป้าหมาย 5–8 คนเป็น formative sample ไม่ใช้สรุปแทนประชากรหรือคำนวณ fraud-detection accuracy
