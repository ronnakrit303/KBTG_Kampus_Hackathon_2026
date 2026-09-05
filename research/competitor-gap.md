# JobShield — KBank Capability & Novelty Gap

สถานะ: Public-source review completed 4 กันยายน 2026  
ขอบเขต: K PLUS, K-ePocket, MAKE by KBank, KBank anti-fraud controls และมาตรการ ธปท.; การไม่พบข้อมูลในหน้าสาธารณะไม่ใช่หลักฐานยืนยันว่าไม่มีระบบภายใน

## Executive Verdict

**Research Gate 2: PASS WITH MATERIAL NARROWING**

ไม่พบแหล่งสาธารณะที่อธิบาย end-to-end flow แบบ `Career Mode + purpose-bound protected fund + recruitment-payment context + recipient/transaction risk + adaptive pre-transfer intervention` แต่ส่วนประกอบเกือบทั้งหมดมีอยู่แล้วหรือเป็นแนวปฏิบัติที่ ธปท. ผลักดัน

ดังนั้น JobShield ไม่ใช่ “ฟีเจอร์แบ่งเงิน/ล็อกเงิน/ตรวจบัญชี/เตือนก่อนโอนแบบใหม่” ความแตกต่างที่ยังพอป้องกันได้คือ **scenario-aware orchestration**: นำ context ที่ผู้ใช้เปิดเองและแหล่งเงินที่ผู้ใช้กำหนดไว้ มาเพิ่มน้ำหนักให้ risk policy ณ จุดก่อน authorized transfer

## Capability Matrix

| Existing capability | หลักฐานสาธารณะ | สิ่งที่ซ้ำกับ JobShield | ช่องว่างที่ยังเสนอได้ | Design response |
|---|---|---|---|---|
| K PLUS My Budget | ตั้งงบรายจ่ายและกำหนดหมวดหมู่ได้ | Job Search Budget | ไม่มีเหตุผลสร้าง budget engine ใหม่ | ให้ Job Search Budget เป็น Career Mode template/category บน My Budget |
| K-ePocket | แบ่งกระเป๋าเก็บ/ใช้/เป้าหมาย และโอน-จ่ายจากกระเป๋าโดยตรง | เงินสำรองก่อนเงินเดือนแรก และ source-of-funds context | หน้าสาธารณะไม่ได้อธิบาย adaptive fraud policy แยกตาม pocket | ให้เงินสำรองก่อนเงินเดือนแรกเป็น user-designated K-ePocket/sub-pocket ไม่ใช่ผลิตภัณฑ์เงินฝากใหม่ |
| MAKE Cloud Pocket | แบ่งเงินจริงเป็นกระเป๋าย่อย ใช้จ่าย/ออมตามเป้าหมาย | การจัดเงินเป็นก้อน | Pocket concept ไม่ใหม่ | อ้าง MAKE เป็นหลักฐาน duplication และตัดการขาย “สองกระเป๋า” เป็นนวัตกรรม |
| MAKE Lock Cloud Pocket | ล็อก Cloud Pocket เพื่อกันนำเงินเก็บออกมาใช้ และปลดล็อกได้ | protected savings | Static/self-control lock มีแล้ว | JobShield ต้องต่างด้วย recipient/context risk และ adaptive intervention |
| K PLUS Lock Account | ล็อกบัญชีแล้วห้ามโอน เติม จ่าย ถอนแบบไม่ใช้บัตรผ่าน K PLUS; ปลดล็อกที่สาขา | hard protection ของเงินฝาก | เป็น account-wide control ไม่ใช่ scenario-specific decision support | ไม่เสนอ hard lock เป็น core; อธิบาย JobShield เป็น selective pre-transfer layer |
| KBank anti-fraud controls | วงเงินตามความเสี่ยง, face verification, suspicious destination detection, call/alert และ hotline | detection, stronger verification, warning, response | แหล่งสาธารณะไม่อธิบาย recruitment context + protected-fund source policy | เชื่อม controls เดิมเป็น recruitment-aware policy; ห้ามอ้างว่าตรวจปลายทางหรือ face scan เป็นของใหม่ |
| KBank job-scam education | อธิบายค่าประกัน/ค่าสมัคร/ค่าเริ่มงาน การตรวจทะเบียนและช่องทางบริษัทจริง พร้อมช่องทางรายงาน | threat knowledge, verification guidance, reporting | เป็นคำแนะนำ/knowledge flow; ไม่พบการผูกเข้ากับ pre-transfer context ในหน้าที่ตรวจ | เปลี่ยน advice ให้เป็น contextual action ณ payment moment โดยไม่อ้างว่า knowledge ใหม่ |
| Share to K PLUS | แชร์ภาพ QR จากแชตเข้า K PLUS เพื่อโอน/จ่าย/ตรวจสลิป | cross-app entry point | รับ QR image แต่ไม่ได้ยืนยันว่าอ่านข้อความหรืออีเมล | ใช้เป็น optional future entry signal; ห้ามอ้าง inbox access |
| มาตรการ ธปท. | money lock, risk-based limits, biometric verification และตัวอย่าง allowlist/double authorisation | lock, limit, verification, trusted recipients | ไม่ได้กำหนด recruitment-specific orchestration | ยอมรับ controls เหล่านี้เป็น baseline และวาง JobShield เหนือ baseline |

## Refined Product Boundary

### Reuse — ไม่สร้างใหม่

- `Job Search Budget` ใช้ My Budget เป็นฐาน
- `เงินสำรองก่อนเงินเดือนแรก` ใช้ K-ePocket/sub-pocket ที่ผู้ใช้กำหนด
- suspicious-destination flag, facial verification, notification และ fraud reporting ใช้เป็น existing capability/integration point
- Lock Account เป็น existing hard-stop option ไม่ใช่ JobShield novelty

### Proposed layer

- `Career Mode` แบบ opt-in และหมดอายุได้
- policy รวม Career Mode, source pocket, first-seen payee/repetition และ destination-risk signal
- contextual reason ที่อธิบายได้โดยไม่เปิด threshold
- adaptive action: normal → deliberate confirmation → pre-transfer cooling-off/independent verification
- limited break-glass สำหรับ own account/verified biller

### Future/optional — ห้ามวางเป็น core claim

- verified-employer/payment network
- registry/contact lookup อัตโนมัติ
- fraud-specialist workflow เฉพาะ recruitment case
- Optional/Future user-shared Email/Link analysis

## Novelty Statement ที่ใช้ได้หลัง review

> JobShield เสนอให้ K PLUS ประสานเครื่องมือจัดงบ กระเป๋าเงิน และ fraud controls ที่มีอยู่แล้ว เข้ากับ Career Mode เพื่อปรับการแทรกแซงก่อนโอนตามทั้งบริบทการหางาน แหล่งเงินที่กำลังถูกแตะ และความเสี่ยงของธุรกรรม

ข้อความนี้เป็น `proposed differentiation based on reviewed public information` ไม่ใช่คำกล่าวว่าเป็นสิ่งแรกของตลาดหรือไม่มีระบบภายในที่คล้ายกัน

## Claims ที่ต้องตัด

- “K PLUS ยังไม่มีฟีเจอร์ล็อกเงิน” — ไม่จริงตาม 1Q25 MD&A
- “KBank ยังตรวจบัญชีปลายทางไม่ได้” — ขัดกับข่าวทางการปี 2569
- “K-ePocket/MAKE ทำได้แค่เก็บเงิน” — ไม่จริง; มีการโอน/จ่าย และ MAKE มี lock
- “การสแกนหน้าแก้ social engineering ได้” — การยืนยันเจ้าของรายการไม่พิสูจน์ว่าไม่ได้ถูกหลอก
- “JobShield เป็นโมเดลตรวจจับ Fraud ใหม่” — Core ที่ตกลงคือ policy/rules + existing/simulated signals ไม่ใช่โมเดลใหม่

## Residual Novelty Risks

- ระบบภายใน KBank อาจมี contextual controls ที่ไม่เปิดเผยสู่สาธารณะ
- “Career Mode” อาจถูกมองเป็น campaign skin หาก source-of-funds ไม่เปลี่ยน policy จริง
- adaptive cooling-off อาจซ้ำ controls ภายในหรือขัด operational/legal requirements ที่ยังไม่ทราบ
- หาก one-page ใช้พื้นที่อธิบาย pockets มากกว่า risk policy กรรมการจะมองว่าเป็น budgeting concept

## Sources

- K PLUS product page: https://www.kasikornbank.com/th/kplus/
- K-ePocket: https://www.kasikornbank.com/th/personal/Digital-banking/Pages/k-epocket.aspx
- MAKE by KBank: https://makebykbank.kbtg.tech/
- MAKE, “Lock Cloud Pocket”: https://makebykbank.kbtg.tech/articles/Lock-Cloud-Pocket-to-prevent-overspending?id=Lock-Cloud-Pocket-to-prevent-overspending
- KBank 1Q25 MD&A (Lock Account, หน้า 31): https://www.kasikornbank.com/th/IR/FinanInfoReports/financialReports/1Q25_MDxA_Th.pdf
- KBank, “หลอกรับสมัครงานออนไลน์”: https://www.kasikornbank.com/th/personal/digital-banking/kbankcyberrisk/pages/jobscam.aspx
- KBank, “สติไฟต์เตอร์,” 22 พ.ค. 2569: https://www.kasikornbank.com/th/news/pages/sati_fighter.aspx
- K PLUS, “Share to K PLUS”: https://www.kasikornbank.com/th/kplus/instruction/share-to-kplus
- ธปท., “ยกระดับมาตรการจัดการภัยทุจริตทางการเงิน,” 13 มิ.ย. 2567: https://www.bot.or.th/th/news-and-media/news/news-20240613.html

ทุกแหล่งเข้าถึง 4 กันยายน 2569
