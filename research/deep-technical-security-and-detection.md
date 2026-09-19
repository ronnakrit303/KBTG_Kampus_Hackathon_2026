# JobShield — Deep Technical Security & Detection

**สถานะ:** Technical research / architecture baseline — ยังไม่ใช่ข้อยืนยันว่า K PLUS Production ใช้กลไกตามเอกสารนี้ทั้งหมด  
**วันที่ปรับปรุง:** 19 กันยายน 2026  
**ขอบเขต:** Mobile security, transaction-risk detection, incident detection และวิธีวัดผลของ K PLUS JobShield

## 1. ข้อสรุปสำหรับผู้บริหาร

จุดอ่อนของ Scam ไม่ได้อยู่ที่ระบบหรือผู้ใช้อย่างใดอย่างหนึ่ง แต่เกิดจากผู้โจมตีทำให้ **ผู้ใช้ที่ผ่านการยืนยันตัวตนแล้วอนุมัติธุรกรรมที่เป็นอันตรายด้วยตนเอง** ดังนั้น PIN, Biometrics หรือ OTP ตอบได้ว่า “ใครกำลังทำรายการ” แต่ยังตอบไม่ได้ว่า “ผู้ใช้อยากทำรายการนี้จริง หรือกำลังถูกหลอกและกดดันอยู่”

JobShield จึงต้องป้องกันพร้อมกันสองคำถาม:

1. **Technical authenticity:** แอป อุปกรณ์ เซสชัน และคำสั่งโอนเป็นของจริงและไม่ถูกแก้ไขหรือเล่นซ้ำหรือไม่
2. **Intent integrity:** วัตถุประสงค์ ปลายทาง และรูปแบบธุรกรรมมีสัญญาณว่าผู้ใช้กำลังถูก Social Engineering หรือไม่

แนวทางที่เสนอคือ **Lightweight, risk-based, defense-in-depth control**: ตรวจสัญญาณราคาถูกและรวดเร็วก่อนทุกครั้ง แล้วเรียกการตรวจที่หนักขึ้นเฉพาะรายการที่เริ่มมีความเสี่ยง ระบบฝั่ง Server เป็นผู้ตัดสินและควบคุมสถานะ Cooling-off ก่อนส่งคำสั่งเข้าสู่ระบบโอน ส่วน Mobile App แสดงเหตุผลและรับการตัดสินใจจากผู้ใช้

> แกนเทคนิค: `Trusted Mobile Request + Multi-signal Risk Correlation + Server-side Policy Enforcement + Auditable Incident Response`

---

## 2. Security model: แยก “ตัวตนถูกต้อง” ออกจาก “เจตนาถูกหลอก”

| คำถาม | ตัวอย่างการควบคุม | สิ่งที่ควบคุมนี้ยังตอบไม่ได้ |
|---|---|---|
| เป็นผู้ใช้ตัวจริงหรือไม่ | PIN, Biometrics, Step-up authentication | ผู้ใช้กำลังเชื่อคำสั่งของมิจฉาชีพหรือไม่ |
| เป็นแอปและอุปกรณ์ที่เชื่อถือได้หรือไม่ | App/device attestation, hardware-backed key | ผู้รับเงินเป็น Fake Recruiter หรือไม่ |
| คำขอถูกแก้ไขหรือเล่นซ้ำหรือไม่ | TLS, nonce, request hash, idempotency key | ธุรกรรมมีบริบท Scam หรือไม่ |
| รายการมีความเสี่ยงหรือไม่ | Payee history, velocity, destination risk, transaction context | ไม่สามารถรับประกันได้ว่าจะจับ Scam ทุกกรณี |
| ควรแทรกแซงอย่างไร | Contextual warning, stronger verification, cooling-off | ต้องไม่กักเงินฉุกเฉินหรือสร้าง False Positive เกินควร |

**Authentication ไม่เท่ากับ Scam Prevention** และ **App Integrity ไม่เท่ากับ Intent Integrity** ทั้งสองชั้นต้องทำงานร่วมกัน

---

## 3. Reference architecture

```text
K PLUS Mobile App
├─ JobShield UI และ Consent
├─ Local biometric gate
├─ Hardware-backed device key
├─ App/device attestation
├─ Secure local storage
└─ แสดงผลเท่านั้น ไม่ถือ Risk Score หรือสิทธิ์ปล่อยรายการ
          │
          │ TLS + Access Token + Nonce/Expiry
          │ Content-bound Request + Idempotency Key
          ▼
Mobile BFF / API Gateway
├─ Authentication และ Session validation
├─ Device/session binding
├─ Schema validation และ Rate limiting
├─ Replay/Duplicate protection
└─ ตรวจ App/device attestation verdict
          │
          ▼
Real-time Risk Orchestrator
├─ Protected Reserve context
├─ New/known payee และ verified destination
├─ Amount, velocity, repeated/split transfers
├─ Device/session posture
├─ Destination Risk Flag
│  └─ จำลองผลจาก Fraud Analytics/Transaction Graph ใน MVP
└─ Optional ML scoring ในอนาคต ไม่ใช่ Core MVP
          │
          ▼
Policy Engine — Low / Medium / High
├─ Low    → ดำเนินการตามปกติ
├─ Medium → Contextual warning + deliberate confirmation
└─ High   → Pending/Cooling-off + Pause & Verify/Cancel & Report
          │
          ▼ เฉพาะคำสั่งที่ได้รับอนุญาตให้ Release
Payment Hub / Core Banking
          │
          ├──────────────► Audit/Event Store
          │                  └─ Tamper-evident timeline และ data minimization
          ▼
Fraud Operations / SIEM / SOAR
└─ Correlation, case management, investigation, response และ rule tuning
```

### Trust boundaries สำคัญ

- **Mobile Device → Bank Edge:** โทรศัพท์และเครือข่ายไม่ถือว่าเชื่อถือได้โดยอัตโนมัติ
- **BFF → Risk Services:** ทุก Service ต้องยืนยันสิทธิ์และตรวจ Schema; ไม่เชื่อ Risk ที่ Client คำนวณเอง
- **Risk/Policy → Payment:** Payment Hub รับเฉพาะคำสั่งที่มีสถานะและ Authorization ถูกต้องจาก Server
- **Operations/Audit:** จำกัดสิทธิ์ตามหน้าที่ บันทึกการเปลี่ยนสถานะ และไม่ใส่ข้อมูลส่วนบุคคลเกินจำเป็นใน Log

---

## 4. Deep security ฝั่งผู้ใช้และ Mobile App

### 4.1 App และ Device Integrity

ใช้ Platform Attestation ก่อนกิจกรรมสำคัญ เช่น การผูกอุปกรณ์ การตั้ง Auto-Allocation การเพิ่มผู้รับใหม่ และการปล่อยรายการ High Risk:

- **Android:** Play Integrity API ช่วยตรวจว่า Request มาจากแอปที่ระบบรู้จัก เป็น Binary ที่ไม่ถูกแก้ไข และทำงานบนอุปกรณ์ที่ผ่านเกณฑ์ของ Platform รวมถึงมี Optional verdict บางประเภท เช่น App ที่กำลัง Capture, Control หรือ Overlay หน้าจอ
- **iOS:** App Attest ใช้ Hardware-backed key และ Challenge จาก Server เพื่อช่วยยืนยันว่า Request มาจาก Instance ของแอปจริง; Assertion ควรถูกตรวจที่ Server ณ จุดสำคัญ
- Attestation เป็นเพียง Signal หนึ่ง ไม่ควรเท่ากับคำตัดสิน Scam เพราะอุปกรณ์ปกติก็อาจมีผู้ใช้ที่กำลังถูกหลอก
- เก็บ Telemetry และวัดผลก่อนบังคับใช้ เพื่อไม่ตัดผู้ใช้ที่อุปกรณ์ไม่รองรับหรือเกิด Platform Error โดยไม่จำเป็น

### 4.2 Hardware-backed key และ Biometrics

- สร้าง Private Key ใน Android Keystore หรือ Apple Secure Enclave เมื่อ Platform รองรับ
- Private Key ไม่ควรถูก Export ออกจาก Hardware-backed storage
- Biometrics/PIN ของเครื่องมีหน้าที่ **อนุญาตให้ใช้ Key** สำหรับยืนยันคำขอสำคัญ ไม่ใช่การส่งลายนิ้วมือหรือใบหน้าให้ JobShield
- Server ผูก Public Key กับ User, Device และ App Instance ที่ผ่านการลงทะเบียน
- หาก Device binding เปลี่ยน หรือ Key ถูกยกเลิก ให้บังคับ Re-enrollment และ Step-up authentication

คำที่ถูกต้องคือ **Local biometric authentication with hardware-backed key** ไม่ใช่ “Biometric Encryption”

### 4.3 Transaction Intent Signing

ก่อนยืนยันรายการ แอปสร้าง Canonical Payload ที่ครอบคลุมข้อมูลสำคัญ เช่น:

```json
{
  "transactionId": "synthetic-tx-001",
  "sourcePocketId": "protected-reserve-token",
  "destinationToken": "payee-token",
  "amount": 8000,
  "currency": "THB",
  "purposeCode": "JOB_ONBOARDING_PAYMENT",
  "policyVersion": "prototype-v1",
  "nonce": "single-use-value",
  "expiresAt": "server-issued-expiry"
}
```

แอปแสดงข้อมูลเดียวกันให้ผู้ใช้ตรวจ แล้วใช้ Hardware-backed key ลงลายมือชื่อ Payload เมื่อผ่าน Local authentication จากนั้น Server ตรวจ:

1. Signature ถูกต้องและ Key ยังผูกกับ User/Device นี้
2. Nonce ยังไม่เคยใช้และไม่หมดอายุ
3. Request hash ตรงกับรายละเอียดที่ Server ได้รับ
4. Transaction ID/Idempotency key ไม่ซ้ำ
5. Amount, destination และ source ไม่ถูกเปลี่ยนระหว่าง Warning กับ Confirmation

กลไกนี้ช่วยป้องกัน Tampering และ Replay แต่ยังไม่พิสูจน์ว่าผู้ใช้ไม่ถูกหลอก จึงต้องผ่าน Risk Orchestrator ต่อ

### 4.4 Network และ Local Data

- ใช้ TLS สำหรับ Confidentiality และ Integrity ระหว่าง Mobile กับ Server
- ไม่ควรเรียกการสื่อสารนี้ว่า End-to-End Encryption (E2EE) เพราะระบบธนาคารต้องถอดและประมวลผลข้อมูลธุรกรรมที่ Server
- เก็บ Token/Key reference ใน Keystore/Keychain และไม่ Hard-code Secret ในแอป
- ไม่เก็บ Transaction Graph, Rule weights หรือ Destination-risk database บนโทรศัพท์
- Countdown ที่ Mobile เป็นเพียงหน้าจอแสดงผล; เวลาและสถานะจริงต้องยึด Server clock
- เมื่อเปิดแอปใหม่ ต้องดึง Pending state ล่าสุดจาก Server ไม่เชื่อ Cached state บนอุปกรณ์

### 4.5 Overlay, Screen Control และ Accessibility

- หาก Platform ส่งสัญญาณว่ามีแอปอื่นกำลัง Capture, Control หรือ Overlay หน้าจอ ให้เพิ่ม Risk ไม่ใช่สรุปทันทีว่าเป็น Malware
- รายการเสี่ยงสูงอาจซ่อนข้อมูลละเอียด บังคับ Re-authentication หรือขอให้ปิด App ที่ควบคุมหน้าจอก่อนทำต่อ
- ต้องมีเส้นทางรองรับ Accessibility; การบล็อกทุก Overlay หรือ Accessibility Service อาจทำร้ายผู้ใช้จริงและเพิ่ม False Positive
- ไม่อ่านข้อความ อีเมล เสียงสนทนา หรือ Clipboard โดยปริยาย

---

## 5. Lightweight Software Control

`Lightweight` ไม่ได้หมายถึงตรวจน้อยหรือความปลอดภัยต่ำ แต่หมายถึงใช้ทรัพยากรบนโทรศัพท์ต่ำ เพิ่ม Latency เฉพาะเท่าที่จำเป็น ไม่ตรวจข้อมูลส่วนตัวเกินขอบเขต ใช้ Control ที่แรงขึ้นตามความเสี่ยง และส่งงาน Correlation ที่ซับซ้อนไปฝั่ง Server

### Cascaded detection pipeline

| ชั้น | ทำงานเมื่อใด | ตัวอย่าง Signal/Control | ต้นทุนโดยประมาณ |
|---|---|---|---|
| L0 — Always-on validation | ทุก Request | Session, schema, source pocket, payee status, nonce, idempotency | ต่ำมาก |
| L1 — Fast risk features | ทุก Eligible transfer | New payee, amount, velocity, repeated transfer, cached destination flag, device posture | ต่ำ |
| L2 — Enhanced analysis | เมื่อ L0–L1 พบความเสี่ยง | Graph query, fresh enhanced attestation, cross-account pattern, optional model | กลาง–สูง |
| L3 — Intervention/Case | เมื่อ Policy เป็น High | Server-side pending, cooling-off, independent verification, case creation | สูง แต่เกิดกับส่วนน้อย |

### Fail behavior

- **Fail closed:** Signature ผิด, Request ถูก Replay, Session หมดอายุ, Payload ถูกแก้ไข — ปฏิเสธคำขอ
- **Fail safe with step-up:** Optional Signal หายหรือ Service ชั่วคราวไม่พร้อม — ไม่กล่าวหาว่าเป็น Scam; อาจจัดเป็น Medium, ขอ Stronger verification หรือแจ้งให้ลองใหม่
- **ห้าม Fail open โดยไม่มี Policy:** ไม่ควรปล่อย High-risk Pending เพียงเพราะ Risk Service Timeout

### Performance SLO ที่ควรวัด แต่ยังไม่ควรอ้างเป็นผลจริง

- End-to-end risk decision latency: p50, p95 และ p99
- Attestation latency แยกจาก Business API latency
- Timeout/error rate ของ Risk dependency
- จำนวน Enhanced checks ต่อธุรกรรมทั้งหมด
- Mobile crash rate, battery/network overhead และ task-completion time

ตัวเลขเป้าหมายต้องกำหนดหลัง Benchmark; Prototype ไม่ควรแต่งตัวเลข Production ขึ้นมา

---

## 6. Transaction Risk Correlation

### 6.1 Signal groups

1. **Asset context:** เงินมาจาก `เงินสำรองตั้งหลัก`; ยอดหลังถอนต่ำกว่า Save Point หรือไม่
2. **Payee context:** ผู้รับใหม่หรือเคยโอนแล้ว; บัญชีบุคคล/Verified Biller/บัญชีตนเอง; Destination Risk Flag
3. **Transaction behavior:** จำนวนและสัดส่วนเทียบยอดสำรอง; โอนซ้ำ/แบ่งยอด; ความเร็วในการเพิ่มผู้รับแล้วสั่งโอน; ความเบี่ยงจาก Baseline
4. **Declared context:** วัตถุประสงค์ เช่น ค่าสมัคร ค่าอบรม ค่าอุปกรณ์ หรือมัดจำเพื่อเริ่มงาน โดยให้น้ำหนักจำกัดเพราะ Attacker อาจสอนให้ตอบผิด
5. **Device/session posture:** Attestation, อุปกรณ์/Session ใหม่, Replay/Tampering และ Optional app-access risk

### 6.2 ตัวอย่าง Policy — ไม่ใช่สูตร Production

```python
def decide_risk(event):
    if event.signature_invalid or event.replay_detected:
        return "REJECT_SECURITY"

    scam_signals = 0
    if event.source_is_protected_reserve:
        scam_signals += 1
    if event.payee_is_new_personal_account:
        scam_signals += 1
    if event.purpose_is_pay_to_get_job:
        scam_signals += 1
    if event.repeated_or_split_transfer:
        scam_signals += 1
    if event.destination_risk_is_elevated:
        scam_signals += 2
    if event.device_or_session_risk_is_elevated:
        scam_signals += 1

    if scam_signals >= 4:
        return "HIGH"
    if scam_signals >= 2:
        return "MEDIUM"
    return "LOW"
```

หลักสำคัญ:

- ไม่เตือนเพราะ Signal เดียวโดยอัตโนมัติ ยกเว้น Security invariant เช่น Signature ผิด
- แยก `security rejection` ออกจาก `scam-risk intervention`
- ไม่ส่ง Raw graph หรือ Rule weights ให้ Mobile; ส่งเฉพาะระดับและเหตุผลที่เข้าใจได้ 2–3 ข้อ
- บันทึก Policy Version ทุก Decision เพื่อ Audit และ Reproduce ผลย้อนหลัง

---

## 7. Coverage ต้องวัดหลายมิติ

ห้ามใช้คำว่า “Coverage สูง” โดยไม่มีนิยาม เพราะแต่ละ Coverage ตอบคนละคำถาม

| Coverage | นิยาม | ตัวอย่างวิธีวัด |
|---|---|---|
| Threat coverage | Threat Scenario ในขอบเขตที่มี Control | Threats ที่มี Control / Threats ทั้งหมด |
| Signal coverage | Eligible transaction ที่มี Required signals สดและครบ | รายการที่ประเมินได้ครบ / Eligible transfers |
| Platform coverage | อุปกรณ์เป้าหมายที่รองรับ Control | Supported devices / Eligible devices |
| Policy coverage | ประเภทธุรกรรมในขอบเขตที่ Policy ถูกเรียกก่อนเงินออก | Protected types / In-scope types |
| Label coverage | Decision ที่มี Ground truth ยืนยันภายหลัง | Confirmed outcomes / Decisions ทั้งหมด |
| Scenario/test coverage | Boundary/adversarial cases ที่ Prototype ทดสอบ | Passed scenarios / Planned scenarios |

- Detection coverage ของ Scam ที่ยืนยันแล้วมีความหมายใกล้กับ **Recall** จึงไม่ควรรายงานซ้ำ
- Synthetic data วัดได้เพียง Rule/test coverage และ Logic ไม่สามารถพิสูจน์ Population coverage หรือประสิทธิผลจริง

### Threat-to-control coverage matrix

| Threat | Prevent/Detect | Response | Residual risk |
|---|---|---|---|
| Fake Recruiter หลอกให้โอนเอง | Multi-signal context + destination risk | Warning/Cooling-off/Cancel & Report | ผู้ใช้อาจยังดำเนินการต่อ |
| Attacker สอนให้ตอบ Purpose ผิด | Purpose เป็นเพียง Signal; ใช้ payee/source/velocity ร่วม | Escalate เมื่อ Signal อื่นสูง | Attacker อาจลดสัญญาณได้ |
| แบ่งยอดหรือโอนซ้ำ | Velocity และ aggregate amount window | Group เป็น Detection/Case เดียว | เว้นช่วงนานอาจหลบ Rule |
| บัญชีม้าหรือเครือข่ายเสี่ยง | Destination/graph risk | High-risk intervention/case | Graph ใหม่อาจไม่มีประวัติ |
| Account takeover/session theft | Binding, attestation, step-up, revocation | Reject/revoke/recover | Social engineering บนอุปกรณ์จริงยังเกิดได้ |
| App tampering/replay | Signature, request hash, nonce, expiry, idempotency | Reject + security alert | อุปกรณ์บางรุ่นให้ Signal จำกัด |
| Overlay/remote control | App-access signal + step-up | จำกัด/ปิด control app/route review | Accessibility false positive |
| API retry ทำรายการซ้ำ | Idempotency + state machine | Return current status | Race condition ต้องทดสอบ |
| เหตุฉุกเฉินจริงถูกเตือน | Verified destination, explainability, reversible nudge | Break-glass ตาม Policy | ยังมี Friction |
| Rule/model drift | Monitor by policy version/segment | Tune/test/rollback | Ground-truth delay |

---

## 8. Precision และ Recall

กำหนด Ground truth ต่อหนึ่ง Eligible transfer หรือหนึ่ง Fraud case ให้ชัด:

- **TP:** รายการ Scam ที่ระบบ Escalate ก่อนเงินออก
- **FP:** รายการถูกต้องที่ถูก Escalate เกินระดับที่กำหนด
- **FN:** รายการ Scam ที่ระบบปล่อยผ่านหรือจัดระดับต่ำเกินไป
- **TN:** รายการถูกต้องที่ผ่าน Flow ปกติ

```text
Precision = TP / (TP + FP)
Recall    = TP / (TP + FN)
FPR       = FP / (FP + TN)
FNR       = FN / (FN + TP)
```

- **Precision สูง:** เมื่อระบบบอก High Risk มักมีเหตุจริง ช่วยลด False Positive, Alert Fatigue และต้นทุนตรวจสอบ
- **Recall สูง:** ระบบจับ Scam ในขอบเขตได้มาก ช่วยลดรายการอันตรายที่หลุดไป
- Threshold ต่ำมักเพิ่ม Recall แต่ลด Precision; Threshold สูงมักเพิ่ม Precision แต่พลาด Scam มากขึ้น
- Accuracy ไม่เหมาะเป็น Metric หลักเมื่อ Scam มีสัดส่วนน้อย

### Risk-tier strategy

- `Medium`: Threshold ต่ำกว่าเพื่อให้ Recall สูงขึ้น เพราะ Intervention เป็น Warning ที่ย้อนกลับได้
- `High`: ต้องการ Precision สูงกว่า เพราะ Cooling-off กระทบการเข้าถึงเงินและ Support cost
- รายงาน Precision/Recall แยกตาม Tier, Scam type, Platform และ Policy version

### ตัวอย่างเพื่ออธิบายเท่านั้น — ไม่ใช่ผลทดสอบ

หากมี 100 รายการ มี Scam ที่ยืนยันแล้ว 10 รายการ ระบบจับได้ 8 และ Escalate รายการปกติผิด 4:

```text
Precision = 8 / (8 + 4) = 66.7%
Recall    = 8 / (8 + 2) = 80.0%
```

ห้ามนำตัวเลขนี้ไปกล่าวว่าเป็นผลของ JobShield

### Metrics เสริม

- Amount-weighted recall
- Alert-to-case conversion rate
- Warning dismissal, pause, cancel และ report rate
- Legitimate task completion time และ abandonment rate
- Decision latency และ dependency timeout
- Label delay และ drift

---

## 9. Incident Detection และความสัมพันธ์กับ SIEM

### 9.1 Event ไม่เท่ากับ Incident

```text
Event
คำสั่งโอน, attestation verdict, destination-risk update, repeated transfer
        ↓ Correlation
Detection
Rule/Model พบรูปแบบที่ควรตรวจเพิ่ม
        ↓ Policy threshold
Alert
ผลที่ต้องมี Action เช่น High-risk pending
        ↓ Grouping + Investigation
Case
รวมธุรกรรม ผู้รับ อุปกรณ์ และ Timeline ที่เกี่ยวข้อง
        ↓ Validation
Incident
เหตุ Scam/Fraud/Security ที่ยืนยันและต้องตอบสนองอย่างเป็นระบบ
```

High-risk transfer ยังเป็น **Alert** ไม่ใช่ Incident ที่ยืนยันแล้วเสมอ

### 9.2 JobShield Risk Engine ต่างจาก SIEM

| ระบบ | หน้าที่ | เวลา | การกระทำ |
|---|---|---|---|
| Inline Transaction Risk Engine | ตัดสินคำสั่งนี้ก่อนเงินออก | Near real time | Allow, warn, pending หรือ reject |
| SIEM | รวม Event หลายระบบเพื่อค้นหารูปแบบและสอบสวน | Near real time ถึงย้อนหลัง | Alert, correlate, dashboard, case |
| SOAR/Fraud Case Management | Workflow การตอบสนอง | หลัง Alert/Incident | Enrich, assign, revoke, preserve evidence |

SIEM ไม่ควรเป็นส่วนเดียวที่ตัดสินการโอนแบบ Inline เพราะอาจมี Latency และไม่ได้เป็น Transaction State Authority แต่ JobShield ควรส่ง Events ไปให้ SIEM เพื่อเชื่อมกับ Device, IAM, API และ Fraud Operations

### 9.3 Transaction state machine

```text
RECEIVED
   ↓
EVALUATING
   ├─ LOW ───────────────► RELEASE_APPROVED ─► SENT_TO_PAYMENT
   ├─ MEDIUM ─► USER_CONFIRMED ──────────────► RELEASE_APPROVED
   └─ HIGH ──────────────► PENDING_COOLING_OFF
                              ├─ USER_CANCELLED ─► CANCELLED/REPORTED
                              ├─ VERIFIED ───────► RELEASE_APPROVED
                              ├─ POLICY_RELEASE ─► RELEASE_APPROVED
                              └─ EXPIRED ────────► CANCELLED/REVIEW
```

Security invariants:

- `SENT_TO_PAYMENT` เกิดเมื่อ Server มี `RELEASE_APPROVED` เท่านั้น
- การกดซ้ำต้องไม่สร้างคำสั่งใหม่
- Mobile เปลี่ยน Pending เป็น Released ด้วยการแก้เวลาเครื่องไม่ได้
- ทุก Transition มี Actor, timestamp, reason, policy version และ correlation ID
- Cooling-off พัก **คำสั่งโอนรายการนั้นก่อนส่งเข้าสู่ Payment Hub** ไม่ใช่ล็อก Pocket ทั้งก้อน

### 9.4 Incident-response loop

- **Detect:** รวม Transaction, Destination, Device และ Session signals
- **Respond:** พัก/ยกเลิกรายการ, รับ Report, Revoke session เมื่อสงสัย Account takeover และเปิด Case
- **Recover:** คืนการเข้าถึงอย่างปลอดภัย ช่วยตรวจรายการ และประสานกระบวนการธนาคาร
- **Improve:** วิเคราะห์ Root cause, FP/FN, ปรับ Rule และ Regression test ก่อน Deploy

---

## 10. Event schema ขั้นต่ำสำหรับ Prototype

ใช้ข้อมูลสังเคราะห์และ Tokenize identifier:

```json
{
  "eventId": "evt-uuid",
  "eventType": "TRANSFER_INTENT",
  "occurredAt": "2026-09-19T10:00:00+07:00",
  "correlationId": "case-or-flow-id",
  "transactionId": "synthetic-tx-id",
  "userToken": "synthetic-user-token",
  "deviceToken": "synthetic-device-token",
  "sourceType": "PROTECTED_RESERVE",
  "destinationType": "NEW_PERSONAL_PAYEE",
  "amountBand": "5000_10000",
  "purposeCode": "JOB_ONBOARDING_PAYMENT",
  "velocity": {"count1h": 2, "amount24h": 12000},
  "destinationRisk": "ELEVATED_SYNTHETIC",
  "devicePosture": "TRUSTED_OR_UNKNOWN",
  "policyVersion": "prototype-v1",
  "decision": "HIGH",
  "reasonCodes": [
    "PROTECTED_SOURCE",
    "NEW_PERSONAL_PAYEE",
    "PAY_TO_GET_JOB",
    "ELEVATED_DESTINATION"
  ]
}
```

Data minimization:

- ใช้ Reason code แทนข้อความอีเมลหรือบทสนทนา
- ไม่เก็บเลขบัญชีเต็มใน Analytics/Audit หาก Token ใช้งานได้
- กำหนด Retention, Access control และวัตถุประสงค์ของแต่ละ Field
- แยก Operational audit ออกจากข้อมูลสำหรับ Model training
- ไม่นำข้อมูลไปฝึกโมเดลอัตโนมัติโดยไม่มี Governance/Consent ที่เหมาะสม

---

## 11. MVP ที่ทีมสองคนพิสูจน์ได้

### Components

- Mobile clickable/functional prototype
- FastAPI mock API + OpenAPI contract
- Deterministic, versioned rule engine
- NetworkX synthetic graph หรือ precomputed destination-risk flag
- Server-side pending transaction และ authoritative countdown
- Structured audit events และ test harness

### พิสูจน์ได้

- Flow และเหตุผลที่แสดงสอดคล้องกับ Signal
- Transaction state ไม่ถูกข้ามด้วยการกดซ้ำหรือแก้เวลา Client
- Rule/test coverage สำหรับ Scenario ที่กำหนด
- Latency ของ Prototype ภายใต้ Synthetic load
- Warning comprehension และ Legitimate-task friction จาก Usability test จริง

### ยังพิสูจน์ไม่ได้

- Precision/Recall ต่อประชากรจริง
- การลดความเสียหายจริงของธนาคาร
- ความแม่นยำของ Internal Fraud Analytics/Transaction Graph
- Production scalability, Availability และ Internal API integration
- Approval ของ K Point, Benefit, ดอกเบี้ย หรือ Product terms

---

## 12. Security test plan

1. **Policy unit tests:** Low/Medium/High, Boundary และ Purpose ที่กรอกผิด
2. **Invariant/state tests:** ห้ามข้าม Pending, Cancelled ปล่อยไม่ได้, Countdown ยึด Server
3. **API security tests:** Replay, expired token, duplicate idempotency, payload tampering, unauthorized transition
4. **Mobile abuse tests:** Tampered client ส่ง Risk ปลอม, attestation unavailable, overlay/control และ accessibility exception
5. **Detection tests:** Split transfer, repeated payee, synthetic mule graph, missing/stale signal, graph timeout
6. **Performance/resilience:** p50/p95/p99, dependency timeout, retry storm, degraded mode และ duplicate prevention
7. **Human-centered security:** ความเข้าใจ Warning, contextual vs generic, fatigue, emergency access, screen reader
8. **Monitoring:** Correlation ID, Policy version, PII-safe audit, rollback และ FP review

---

## 13. ภาษาที่ควรใช้ใน Pitch และ Diagram

### ใช้ได้

> JobShield ตรวจความเสี่ยงแบบหลายสัญญาณก่อนส่งคำสั่งเข้าสู่ระบบโอน โดยเชื่อมบริบทของเงินสำรอง ผู้รับ รูปแบบธุรกรรม ความเสี่ยงปลายทาง และความน่าเชื่อถือของอุปกรณ์ เพื่อเลือกการแทรกแซงที่เหมาะสม

> ระบบใช้ Lightweight risk cascade: ตรวจสัญญาณพื้นฐานที่รวดเร็วก่อน และเรียกการวิเคราะห์ที่หนักขึ้นเฉพาะรายการที่มีความเสี่ยง

> Prototype ใช้ Rule-based policy และ Synthetic destination-risk data เพื่อพิสูจน์ Flow และ Security invariant โดยไม่อ้าง Accuracy ของระบบจริง

### ไม่ควรใช้

- “AI ตรวจจับ Scam ได้แม่นยำ” — ยังไม่มี Model และข้อมูลจริง
- “ป้องกัน Fraud ได้ 100%” — ผู้ใช้ยังอาจดำเนินการต่อและ Threat เปลี่ยนได้
- “K PLUS ใช้เทคโนโลยีนี้อยู่แล้ว” — เว้นแต่มีแหล่งทางการยืนยัน
- “เข้ารหัสแบบ E2EE” — ไม่ตรงกับ Transaction processing ที่ Server ต้องอ่านข้อมูล
- “Biometric Encryption” — ใช้ Local biometric authentication/hardware-backed key
- “Coverage/Precision/Recall สูง” — ต้องมี Dataset, Ground truth, Method และผลจริง

---

## 14. แหล่งอ้างอิงหลัก

1. OWASP, **Mobile Application Security Verification Standard (MASVS)**: <https://mas.owasp.org/MASVS/>
2. OWASP, **MASVS-NETWORK**: <https://mas.owasp.org/MASVS/08-MASVS-NETWORK/>
3. Android Developers, **Play Integrity API overview**: <https://developer.android.com/google/play/integrity/overview>
4. Android Developers, **Integrity verdicts**: <https://developer.android.com/google/play/integrity/verdicts>
5. Android Developers, **Key attestation**: <https://developer.android.com/privacy-and-security/security-key-attestation>
6. Apple Developer Documentation, **Validating apps that connect to your server**: <https://developer.apple.com/documentation/devicecheck/validating-apps-that-connect-to-your-server>
7. Apple Developer Documentation, **Establishing your app’s integrity**: <https://developer.apple.com/documentation/DeviceCheck/establishing-your-app-s-integrity>
8. Apple Developer Documentation, **Protecting keys with the Secure Enclave**: <https://developer.apple.com/documentation/Security/protecting-keys-with-the-secure-enclave>
9. NIST SP 800-61 Rev. 3, **Incident Response Recommendations and Considerations for Cybersecurity Risk Management**: <https://csrc.nist.gov/pubs/sp/800/61/r3/final>
10. scikit-learn, **precision_score**: <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html>
11. scikit-learn, **recall_score**: <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html>
12. scikit-learn, **Precision-Recall curve**: <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html>

## 15. Decision summary

JobShield ควรนำเสนอว่าเป็น **Mobile Security Module ภายใน K PLUS** ที่เสริมระบบเดิม ไม่ใช่ SIEM ใหม่หรือ AI ที่ทำงานบนมือถือทั้งหมด:

1. Mobile พิสูจน์ App/Device/Request integrity และนำเสนอ Intervention
2. Server รวมหลาย Signal และเป็นผู้ตัดสิน Policy
3. Cooling-off พักเฉพาะคำสั่งเสี่ยงก่อนส่งเข้าสู่ Payment Hub
4. SIEM/Fraud Operations รับ Event และ Case เพื่อสอบสวนและพัฒนาการตรวจจับ
5. MVP วัด Rule/test coverage และ UX ได้ แต่ห้ามอ้าง Precision/Recall จริงจนมีข้อมูลที่มี Ground truth

