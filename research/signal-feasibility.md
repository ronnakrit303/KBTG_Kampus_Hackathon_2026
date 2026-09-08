# JobShield — Signal & Control Feasibility

สถานะ: Public-evidence feasibility review completed 4 กันยายน 2026; V5 continuous-reserve scope synced 6 กันยายน 2026

วัตถุประสงค์: แยกสิ่งที่ K PLUS เห็นตามธรรมชาติของ flow, สิ่งที่เป็น reasonable bank-side assumption และสิ่งที่ต้องตัดจาก core

## Research Gate 3

**ผล: PASS FOR CONCEPT/PROTOTYPE, NOT PRODUCTION VALIDATION**

Transaction-based core สามารถสาธิตได้โดยไม่อ่านข้อความส่วนตัวและไม่ใช้ข้อมูลลูกค้าจริง เพราะสัญญาณขั้นต่ำมาจาก JobShield state, protected fund source และข้อมูลธุรกรรมใน flow อย่างไรก็ตาม recipient legal type, fraud-network graph, verified-employer network และอำนาจ operational ในการ cooling-off ยังไม่ได้รับการยืนยันจาก public sources จึงต้องจำลองหรือระบุเป็น future integration

Core มี 3 integrations เท่านั้น: `K-ePocket`, `K PLUS Transaction + Bank-side Fraud Risk` และ `K PLUS Security & Fraud Response` ส่วน Email/Link scanning และ Fraud Specialist เป็น Optional/Future integration

## Signal Matrix

| Signal | สถานะ | เหตุผล/หลักฐาน | ใช้ใน prototype |
|---|---|---|---|
| JobShield on/off | Proposed app state | ผู้ใช้ opt-in เอง; ไม่ต้องอนุมานสถานะงานจากอายุ/อีเมล | ใช้จริงใน synthetic policy |
| Source = เงินสำรองตั้งหลัก | Publicly plausible | K-ePocket โอน/จ่ายจากกระเป๋าโดยตรง | ใช้เป็น protected fund source เดียวตลอด Flow |
| Amount, timestamp, destination identifier | Bank-visible in transfer flow | เป็นข้อมูลที่ต้องใช้สร้างและบันทึกธุรกรรม | ใช้จริง |
| First-seen/new payee | Reasonable derived signal | K PLUS มี transaction history/favorites; ไม่พบหลักฐานสาธารณะว่า fraud engine ใช้ feature นี้โดยตรง | ใช้เป็น derived feature assumption |
| Repeated/cumulative transfers | Reasonable derived signal | ประวัติธุรกรรมทำให้คำนวณการโอนสะสมได้ | ใช้จริงบน synthetic history |
| Destination suspicious-risk flag | Existing capability at high level | KBank ระบุว่ามีระบบตรวจบัญชีหรือปลายทางน่าสงสัย แต่ไม่เปิด interface/rules | ใช้ simulated bank-side flag |
| Device binding / important-transaction face verification | Existing capability | K PLUS และมาตรการ ธปท. รองรับ device binding/biometric control | ใช้เป็น secondary control; ไม่ใช้พิสูจน์ว่าไม่ถูก social engineering |
| User-declared job-payment purpose | Proposed, user-provided | ถามเฉพาะเมื่อเสี่ยงและผู้ใช้ตอบได้ | ใช้เป็นหนึ่ง signal ห้ามเป็น bypass switch |
| Recipient = individual vs registered business | Unconfirmed detail | หน้าสาธารณะไม่ยืนยัน availability/reliability ข้ามธนาคาร | ใช้เฉพาะเมื่อระบุ assumption; core ใช้ `new account transfer vs verified biller` แทน |
| Verified employer/payment channel | Future integration | ไม่พบ public KBank product ที่เป็น employer-payment directory | ไม่ใช้เป็น dependency; ใช้ใน future vision เท่านั้น |
| Shared Email/Link indicators | Optional/Future, consent-based | K PLUS มี Share-to-K PLUS สำหรับ QR image แต่ไม่ได้แปลว่ามี inbox access | ไม่อยู่ใน Core scenario |
| Fraud graph/network connectivity | Internal/unavailable | ต้องพึ่งข้อมูล CFR/ธนาคารและระบบภายใน | simulated destination-risk flag เท่านั้น |

## Minimum Viable Policy

Prototype core ไม่ต้องใช้ ML:

1. รับ JobShield state, protected-reserve source, payee history, amount/repetition, optional job-payment purpose และ destination-risk flag
2. ใช้ explainable rules จัดระดับ Low/Medium/High
3. แสดงเฉพาะ observable reasons เช่น “ผู้รับนี้ยังไม่เคยได้รับเงินจากคุณ”, “รายการนี้แตะเงินสำรองตั้งหลัก”, “มีการโอนสะสมหลายครั้งในช่วงสั้น”
4. Low ทำรายการปกติ; Medium deliberate confirmation; High พัก Pending Instruction ก่อนระบบโอน/PromptPay แล้วใช้ risk-based Cooling-off + verification path
5. Own account/verified biller ใช้ limited break-glass; user-created trusted payee ต้องผ่าน first-time control

## Control Feasibility Boundaries

- `Cooling-off` ต้องพัก Pending Instruction ก่อนส่งเข้าสู่ระบบโอน/PromptPay; ห้ามสื่อว่าสามารถดึง transfer ที่เสร็จแล้วกลับมาได้
- `Dynamic Time Lock` เป็นกลไกภายใน risk-based Cooling-off ไม่ใช่ฟีเจอร์แยก
- ระยะ cooling-off เป็น usability/policy hypothesis ไม่กำหนดตัวเลขจนทดสอบและหารือข้อกำกับ
- Lock Account ของ K PLUS เป็น existing account-wide hard stop; JobShield ไม่ควรจำลองว่าแก้หรือแทนที่ระบบนี้
- Cancel/Report หมายถึงยกเลิกรายการที่ยังไม่ execute และนำผู้ใช้เข้าสู่ช่องทางรายงานที่มีอยู่ ไม่รับประกัน freeze/recovery
- Independent verification ด้วยทะเบียน/เว็บไซต์ทางการเป็นแนวทางที่ KBank แนะนำ แต่ automated lookup และ fraud-specialist SLA เป็น future integration

## Prototype Data Boundary

- ใช้ชื่อบริษัท บัญชี เลขอ้างอิง และเหตุการณ์สมมติทั้งหมด
- ห้ามใช้เลขบัญชีจริง Resume จริง อีเมลจริง credential หรือข้อมูลลูกค้า
- synthetic risk table ต้องแสดง input → rule reason → risk tier → action โดยไม่อ้าง precision/recall จากข้อมูลจริง
- coded demo ถ้าทำทันต้องเป็น deterministic rules demo และติดป้ายว่า simulation

## เงินสำรองตั้งหลัก And Auto-Routing

**ผล: FEASIBLE FOR CLICKABLE PROTOTYPE; PRODUCTION DEPENDENCIES UNCONFIRMED**

| Capability | Prototype approach | Production boundary |
|---|---|---|
| Emergency-reserve target | deterministic formula: essential monthly expense × selected months | financial-education wording and product suitability review required |
| Auto-Routing | synthetic incoming-fund event or user-configured scheduled transfer; เปิดภายหลังได้ | K-ePocket/internal scheduling APIs and automatic income classification not confirmed publicly |
| Recommended percentage | transparent rule/example, editable by user | do not call AI; recommendation methodology needs product review |
| Stop at cap | simulated rule state | requires reliable balance/event handling and idempotency |
| Reward | milestone badge; K Point shown only as unconfirmed concept | campaign cost, eligibility and Business approval required |
| Withdrawal protection | own/verified path, dismissible spending nudge, or reuse H05/H06 for multi-signal High Risk | cooling-off authority and payment-operations design remain unconfirmed |

Security requirements for a production implementation include encryption in transit/at rest, bank-approved key management, least-privilege access, minimal audit logging and an idempotency key that prevents repeated taps from creating duplicate Auto-Routing or transfer instructions. These are architecture requirements only; the Figma prototype does not prove they are implemented.

PDPA boundary: collect only target/rule/transaction indicators needed for the declared purpose, do not read email or messages, provide explicit opt-in and controls to pause/disable, state retention, and send any changed-purpose processing through legal/DPO review. Consent is not automatically the only lawful basis; production counsel must determine the applicable basis.

Alert fatigue/false positives: normal internal Auto-Routing should be quiet, ordinary spending receives a dismissible nudge, own-account/verified emergency use must remain accessible, and only multi-signal High Risk enters Cooling-off. A reserve withdrawal alone is not a fraud finding.

## Sources

- K PLUS product/features: https://www.kasikornbank.com/th/kplus/
- K PLUS transfer flow: https://www.kasikornbank.com/th/kplus/instruction/transfer
- K PLUS Share to K PLUS: https://www.kasikornbank.com/th/kplus/instruction/share-to-kplus
- K-ePocket product/FAQ: https://www.kasikornbank.com/th/personal/Digital-banking/Pages/k-epocket.aspx
- KBank 1Q25 MD&A (Lock Account): https://www.kasikornbank.com/th/IR/FinanInfoReports/financialReports/1Q25_MDxA_Th.pdf
- KBank “สติไฟต์เตอร์” anti-fraud controls: https://www.kasikornbank.com/th/news/pages/sati_fighter.aspx
- ธปท. mobile-banking anti-fraud measures: https://www.bot.or.th/th/news-and-media/news/news-20230713.html
- ธปท. enhanced fraud measures: https://www.bot.or.th/th/news-and-media/news/news-20240613.html
- FCA APP-fraud control review: https://www.fca.org.uk/publications/multi-firm-reviews/anti-fraud-controls-complaint-handling-firms-focus-app-fraud
- SET emergency-reserve guidance: https://www.set.or.th/th/about/mediacenter/insights/video/1253-ruthunpakthong-emergency-reserve
- AEA randomized field experiment on saving by default: https://www.aeaweb.org/articles?id=10.1257/app.20160547
- Security-warning habituation research: https://www.jmis-web.org/articles/1304
- KBank K Point: https://www.kasikornbank.com/th/personal/Digital-banking/kplus-kpoint
- GPPC/PDPC privacy policy: https://gppc.pdpc.or.th/privacy-policy/
- OWASP MASVS storage/cryptography/privacy: https://mas.owasp.org/MASVS/05-MASVS-STORAGE/ , https://mas.owasp.org/MASVS/06-MASVS-CRYPTO/ , https://mas.owasp.org/MASVS/controls/MASVS-PRIVACY-1/

แหล่งเดิมเข้าถึง 4 กันยายน 2569; แหล่งส่วนขยายเข้าถึง 5 กันยายน 2569
