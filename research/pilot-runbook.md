# K PLUS JobShield — Pilot Runbook

วันที่เตรียม: 4 กันยายน 2026  
สถานะ: `0 pilot sessions conducted`; `0 participant sessions conducted`

## Gate

ทำ pilot กับคนจริง 1 คนก่อนเริ่ม formative sessions 5–8 คน Automated QA, expert review หรือการคลิกเองของทีมไม่นับเป็น pilot participant

Precondition: human visual owner ต้องกรอก `prototype/visual-owner-review.md` และตัดสิน `READY FOR PILOT` โดยไม่มี Critical/High visual or flow defect ค้างอยู่

## Pilot Participant

- เลือกคนที่อายุ/พฤติกรรมใกล้ First Jobbers และไม่ได้ร่วมออกแบบ flow
- ใช้ Participant ID `PILOT-01`; ไม่เก็บชื่อ เลขบัญชี Resume อีเมล หรือข้อมูลธนาคารจริงใน repository
- อ่าน consent script จาก `research/formative-usability-test-plan.md`
- ขอ recording consent แยกต่างหาก; หากไม่ได้ consent ให้จดเฉพาะ observation ที่ไม่ระบุตัวตน

## Pilot Route

1. เริ่มที่ `START-SETUP` และไปถึง Scenario Dashboard
2. ใช้ `START-S1-CONTEXTUAL` หรือ `START-S1-GENERIC` ตามลำดับที่กำหนด
3. ตรวจ legitimate path จาก `START-LEGIT-LOW`
4. ตรวจ emergency path จาก `START-EMERGENCY`
5. จบแต่ละภารกิจที่ `T00` และใช้ neutral prompts เท่านั้น

## Pass/Revise Gate

ต้องแก้ก่อนเริ่ม 5–8 sessions หากพบข้อใดข้อหนึ่ง:

- ปุ่มหรือ start point ใช้งานไม่ได้ หรือมี dead end
- ผู้ใช้คิดว่ารายการถูกส่งแล้วใน `H05/H06`
- `Pause & Verify`, `Cancel` หรือ `Report` ให้ผลไม่ตรงกับที่คาด
- verified payment channel ถูกเข้าใจว่า KBank รับรอง employer
- legitimate/emergency task ถูก High-Risk flow ขัดขวาง
- `เงินสำรองก่อนเงินเดือนแรก` ถูกเข้าใจว่าเงินถูกล็อกถาวร
- ข้อความล้น ถูกตัด อ่านยาก หรือ action หลักหาไม่เจอ

## Blank Pilot Record — Fill Only After A Real Session

```text
Participant ID: PILOT-01
Date/time:
Format: remote / in-person
Consent: yes/no
Recording consent: yes/no/not recorded
Routes completed:
Broken links/dead ends:
Critical findings:
High findings:
Medium/Low findings:
Timing issue:
Changes required before participant sessions:
Decision: pass / revise and re-pilot
```

ห้ามเติมช่องนี้ด้วยข้อมูลสมมติ และห้ามนับ pilot เป็นหนึ่งในผล 5–8 คนโดยอัตโนมัติหาก protocol หรือ screen content เปลี่ยนอย่างมีนัยสำคัญหลัง pilot
