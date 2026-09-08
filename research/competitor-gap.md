# JobShield — KBank Capability & Novelty Gap

สถานะ: Public-source review updated 6 กันยายน 2026
ขอบเขต: K PLUS, K-ePocket, MAKE by KBank, KBank anti-fraud controls และมาตรการ ธปท.; การไม่พบข้อมูลในหน้าสาธารณะไม่ใช่หลักฐานยืนยันว่าไม่มีระบบภายใน

## Executive Verdict

**Research Gate 2: PASS WITH MATERIAL NARROWING**

ไม่พบแหล่งสาธารณะที่อธิบาย end-to-end flow แบบ `protected reserve + goal-aware scheduled saving + benefit continuity + recipient/transaction context + adaptive pre-transfer intervention` แต่ส่วนประกอบเกือบทั้งหมดมีอยู่แล้วหรือเป็นแนวปฏิบัติที่ ธปท. ผลักดัน

ดังนั้น JobShield ไม่ใช่ “ฟีเจอร์แบ่งเงิน/ล็อกเงิน/ตรวจบัญชี/เตือนก่อนโอนแบบใหม่” ความแตกต่างที่ยังพอป้องกันได้คือ **scenario-aware orchestration**: นำ protected fund source และ transaction context มาเพิ่มน้ำหนักให้ risk policy ณ จุดก่อน authorized transfer

## Capability Matrix

| Existing capability | หลักฐานสาธารณะ | สิ่งที่ซ้ำกับ JobShield | ช่องว่างที่ยังเสนอได้ | Design response |
|---|---|---|---|---|
| K PLUS My Budget | ตั้งงบรายจ่ายและกำหนดหมวดหมู่ได้ | การวางแผนรายจ่ายทั่วไป | ไม่มีเหตุผลสร้าง budget engine ใหม่ | ไม่สร้าง Job Search Budget ใน current scope; ใช้ Reserve Dashboard เท่าที่จำเป็น |
| K-ePocket | แบ่งกระเป๋าเก็บ/ใช้/เป้าหมาย และโอน-จ่ายจากกระเป๋าโดยตรง | เงินสำรองตั้งหลักและ source-of-funds context | หน้าสาธารณะไม่ได้อธิบาย adaptive fraud policy แยกตาม pocket | ใช้ protected reserve ก้อนเดียวบน K-ePocket ไม่ใช่ผลิตภัณฑ์เงินฝากใหม่ |
| K PLUS Schedule Transfer | ระบุบัญชีปลายทาง จำนวนเงิน วัน/เวลา และตั้งรายการล่วงหน้า | Auto-Routing แบบจำนวนคงที่ตามวัน | หน้าสาธารณะไม่ยืนยัน salary-event trigger, direct sub-pocket destination หรือ stop-at-cap | MVP คำนวณจำนวนคงที่จากค่าที่ผู้ใช้กรอกแล้วใช้ scheduled mechanism เป็นฐาน |
| K Point ecosystem | มีระบบคะแนน ภารกิจ การแลก และสิทธิประโยชน์ใน K PLUS ภายใต้เงื่อนไขธนาคาร | Benefit/reward concept | ไม่ยืนยันว่าออมผ่าน JobShield แล้วมีสิทธิได้คะแนนหรือคูปอง | แสดง Benefit Tier และตัวอย่างสิทธิแบบ Business-dependent โดยไม่ระบุจำนวน/มูลค่า |
| MAKE Cloud Pocket | แบ่งเงินจริงเป็นกระเป๋าย่อย ใช้จ่าย/ออมตามเป้าหมาย | การจัดเงินเป็นก้อน | Pocket concept ไม่ใหม่ | อ้าง MAKE เป็นหลักฐาน duplication และตัดการขาย “สองกระเป๋า” เป็นนวัตกรรม |
| MAKE Lock Cloud Pocket | ล็อก Cloud Pocket เพื่อกันนำเงินเก็บออกมาใช้ และปลดล็อกได้ | protected savings | Static/self-control lock มีแล้ว | JobShield ต้องต่างด้วย recipient/context risk และ adaptive intervention |
| K PLUS Lock Account | ล็อกบัญชีแล้วห้ามโอน เติม จ่าย ถอนแบบไม่ใช้บัตรผ่าน K PLUS; ปลดล็อกที่สาขา | hard protection ของเงินฝาก | เป็น account-wide control ไม่ใช่ scenario-specific decision support | ไม่เสนอ hard lock เป็น core; อธิบาย JobShield เป็น selective pre-transfer layer |
| KBank anti-fraud controls | วงเงินตามความเสี่ยง, face verification, suspicious destination detection, call/alert และ hotline | detection, stronger verification, warning, response | แหล่งสาธารณะไม่อธิบาย recruitment context + protected-fund source policy | เชื่อม controls เดิมเป็น recruitment-aware policy; ห้ามอ้างว่าตรวจปลายทางหรือ face scan เป็นของใหม่ |
| KBank job-scam education | อธิบายค่าประกัน/ค่าสมัคร/ค่าเริ่มงาน การตรวจทะเบียนและช่องทางบริษัทจริง พร้อมช่องทางรายงาน | threat knowledge, verification guidance, reporting | เป็นคำแนะนำ/knowledge flow; ไม่พบการผูกเข้ากับ pre-transfer context ในหน้าที่ตรวจ | เปลี่ยน advice ให้เป็น contextual action ณ payment moment โดยไม่อ้างว่า knowledge ใหม่ |
| Share to K PLUS | แชร์ภาพ QR จากแชตเข้า K PLUS เพื่อโอน/จ่าย/ตรวจสลิป | cross-app entry point | รับ QR image แต่ไม่ได้ยืนยันว่าอ่านข้อความหรืออีเมล | ใช้เป็น optional future entry signal; ห้ามอ้าง inbox access |
| มาตรการ ธปท. | money lock, risk-based limits, biometric verification และตัวอย่าง allowlist/double authorisation | lock, limit, verification, trusted recipients | ไม่ได้กำหนด recruitment-specific orchestration | ยอมรับ controls เหล่านี้เป็น baseline และวาง JobShield เหนือ baseline |

## Refined Product Boundary

### Reuse — ไม่สร้างใหม่

- เงินสำรองตั้งหลักใช้ K-ePocket/sub-pocket เดียวตลอด Flow โดยไม่เปลี่ยนตามสถานะงาน
- การตั้งเป้าหมายการออมและการทำธุรกรรมจาก Pocket เป็นความสามารถเดิม
- กลไก Schedule Transfer เป็นฐานสำหรับแผนออมจำนวนคงที่/วันที่กำหนดใน MVP
- K Point เป็น reward ecosystem เดิม แต่ JobShield ไม่มีสิทธิให้คะแนนจนกว่าจะผ่าน Business/Product approval
- suspicious-destination flag, facial verification, notification และ fraud reporting ใช้เป็น existing capability/integration point
- Lock Account เป็น existing hard-stop option ไม่ใช่ JobShield novelty

### Proposed layer

- JobShield แบบ opt-in โดยไม่ถามหรืออนุมานสถานะงาน
- ตัวช่วยคำนวณเป้าหมาย 3/6 เดือน และ Benefit Tier จาก qualified Auto-Routing rounds ที่ 1/3/6 เดือน
- Grace/Pause 1–2 รอบ, checkpoint และ progress hold เพื่อไม่ลงโทษเหตุจำเป็นและลด reward farming
- policy รวม protected-reserve source, first-seen payee, job-payment context/repetition และ destination-risk signal
- contextual reason ที่อธิบายได้โดยไม่เปิด threshold
- two-route action: Mascot Savings Nudge ที่กดข้ามได้เมื่อไม่เข้า High-Risk combination หรือ serious warning → pre-transfer cooling-off/independent verification เมื่อเข้า High Risk

### Future/optional — ห้ามวางเป็น core claim

- verified-employer/payment network
- registry/contact lookup อัตโนมัติ
- fraud-specialist workflow เฉพาะ recruitment case
- Optional/Future user-shared Email/Link analysis

## Novelty Statement ที่ใช้ได้หลัง review

> JobShield เสนอให้ K PLUS เชื่อมเงินสำรองตั้งหลักและ Auto-Routing บน K-ePocket เข้ากับ fraud controls เพื่อปรับการแทรกแซงก่อนโอนตามแหล่งเงิน ผู้รับ บริบทธุรกรรม และความเสี่ยงปลายทาง
>
> Benefit Tier เป็น supporting engagement loop; security novelty ยังคงอยู่ที่การใช้ protected fund context ปรับ pre-transfer policy

ข้อความนี้เป็น `proposed differentiation based on reviewed public information` ไม่ใช่คำกล่าวว่าเป็นสิ่งแรกของตลาดหรือไม่มีระบบภายในที่คล้ายกัน

## Claims ที่ต้องตัด

- “K PLUS ยังไม่มีฟีเจอร์ล็อกเงิน” — ไม่จริงตาม 1Q25 MD&A
- “KBank ยังตรวจบัญชีปลายทางไม่ได้” — ขัดกับข่าวทางการปี 2569
- “K-ePocket/MAKE ทำได้แค่เก็บเงิน” — ไม่จริง; มีการโอน/จ่าย และ MAKE มี lock
- “การสแกนหน้าแก้ social engineering ได้” — การยืนยันเจ้าของรายการไม่พิสูจน์ว่าไม่ได้ถูกหลอก
- “JobShield เป็นโมเดลตรวจจับ Fraud ใหม่” — Core ที่ตกลงคือ policy/rules + existing/simulated signals ไม่ใช่โมเดลใหม่
- “Auto-Routing เป็นฟังก์ชันใหม่ทั้งหมด” — K PLUS มี Schedule Transfer แล้ว; สิ่งที่เสนอเพิ่มคือ goal/checkpoint/tier orchestration
- “ออมมากขึ้นจึงทำให้ KBank ปล่อยกู้และกำไรเพิ่มโดยตรง” — เป็น causal claim ที่กว้างเกินหลักฐาน; ใช้ได้เพียงสมมติฐานเรื่อง stable deposit/engagement แบบมีเงื่อนไข
- “ผู้ใช้ออมแล้วได้รับ K Point แน่นอน” — สิทธิและต้นทุนยังต้องผ่าน Business/Product approval

## Residual Novelty Risks

- ระบบภายใน KBank อาจมี contextual controls ที่ไม่เปิดเผยสู่สาธารณะ
- เมื่อเอา career stage ออก First Jobber specificity อาจอ่อนลง จึงต้องรักษา Target Users และ Fake Recruiter hero scenario ให้ชัด
- adaptive cooling-off อาจซ้ำ controls ภายในหรือขัด operational/legal requirements ที่ยังไม่ทราบ
- หาก one-page ใช้พื้นที่อธิบาย pockets มากกว่า risk policy กรรมการจะมองว่าเป็น budgeting concept
- หาก Benefit Tier กลายเป็น Hero Feature แทน Fake Recruiter/pre-transfer protection แนวคิดจะอ่อนลงใน Track 3
- หาก reward นับจากการโอนเข้าอย่างเดียว ผู้ใช้อาจวนเงินเข้า–ออกเพื่อเก็บสิทธิ; checkpoint/net-balance rule ต้องได้รับการทดสอบ

## Sources

- K PLUS product page: https://www.kasikornbank.com/th/kplus/
- K-ePocket: https://www.kasikornbank.com/th/personal/Digital-banking/Pages/k-epocket.aspx
- K PLUS Schedule Transfer: https://www.kasikornbank.com/th/kplus/instruction/forward-transfers
- K Point: https://www.kasikornbank.com/th/personal/Digital-banking/kplus-kpoint
- MAKE by KBank: https://makebykbank.kbtg.tech/
- MAKE, “Lock Cloud Pocket”: https://makebykbank.kbtg.tech/articles/Lock-Cloud-Pocket-to-prevent-overspending?id=Lock-Cloud-Pocket-to-prevent-overspending
- KBank 1Q25 MD&A (Lock Account, หน้า 31): https://www.kasikornbank.com/th/IR/FinanInfoReports/financialReports/1Q25_MDxA_Th.pdf
- KBank, “หลอกรับสมัครงานออนไลน์”: https://www.kasikornbank.com/th/personal/digital-banking/kbankcyberrisk/pages/jobscam.aspx
- KBank, “สติไฟต์เตอร์,” 22 พ.ค. 2569: https://www.kasikornbank.com/th/news/pages/sati_fighter.aspx
- K PLUS, “Share to K PLUS”: https://www.kasikornbank.com/th/kplus/instruction/share-to-kplus
- ธปท., “ยกระดับมาตรการจัดการภัยทุจริตทางการเงิน,” 13 มิ.ย. 2567: https://www.bot.or.th/th/news-and-media/news/news-20240613.html

แหล่งเดิมเข้าถึง 4 กันยายน 2569; Schedule Transfer และ K Point ตรวจซ้ำ 6 กันยายน 2569
