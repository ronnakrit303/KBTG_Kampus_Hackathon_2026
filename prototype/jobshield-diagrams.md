# K PLUS JobShield — System Diagrams

อัปเดตล่าสุด: 5 กันยายน 2026  
FigJam ชุดปัจจุบัน: [K PLUS JobShield — Detailed System Flow](https://www.figma.com/board/2Zucnsm9P4uPJdZ1BHVRv9)

ไฟล์นี้เป็น canonical Mermaid source ของ FigJam ชุดใหม่ มี 3 แผนภาพ:

1. End-to-End Flow — ตั้งแต่เปิด Career Mode จนรายการสำเร็จหรือถูกยกเลิก
2. Core Integrations and Risk Evaluation — แสดง 3 integrations และข้อมูลที่แต่ละส่วนรับผิดชอบ
3. High-Risk Cooling-off — แสดงว่าระบบพักคำสั่งก่อนส่งเข้าสู่ระบบโอน/PromptPay

## Diagram 1 — End-to-End Flow

```mermaid
flowchart TD
    user(["First Jobber อยู่ในช่วงสมัครงานหรือรอเงินเดือนแรก"])

    subgraph prepare["1. เตรียมเงินและเปิดการป้องกัน"]
        mode["ผู้ใช้เลือกเปิด Career Mode"]
        period["กำหนดระยะเวลาและวันหมดอายุ"]
        pockets["แยกเงินตามวัตถุประสงค์ใน K-ePocket"]
        budget["Job Search Budget<br/>เงินสำหรับค่าใช้จ่ายหางานตามแผน"]
        reserve["เงินสำรองก่อนเงินเดือนแรก<br/>ค่าเช่า อาหาร เดินทาง และเหตุจำเป็น"]
        mode --> period --> pockets
        pockets --> budget
        pockets --> reserve
    end

    request["ได้รับคำขอให้จ่ายค่าสมัคร<br/>ค่าอบรม ค่าอุปกรณ์ หรือเงินมัดจำ"]
    transfer["เริ่มทำรายการโอนใน K PLUS"]

    subgraph assess["2. ประเมินความเสี่ยงก่อนเงินออก"]
        context["บริบทจาก Career Mode และแหล่งเงิน"]
        tx["ผู้รับใหม่ ยอดเงิน และรูปแบบการโอนสะสม"]
        destination["สัญญาณความเสี่ยงปลายทาง<br/>จำลองจากระบบธนาคาร"]
        policy["Multi-signal rules / policy<br/>รวมหลายสัญญาณโดยไม่พึ่งคำตอบเดียว"]
        tier{"ระดับความเสี่ยง"}
        context --> policy
        tx --> policy
        destination --> policy
        policy --> tier
    end

    subgraph act["3. เลือกการแทรกแซงตามความเสี่ยง"]
        low["Low<br/>ตรวจสอบและโอนตามปกติ"]
        medium["Medium<br/>อธิบายเหตุผลและให้ยืนยันอย่างตั้งใจ"]
        high["High<br/>Pause & Verify + Cooling-off"]
        emergency["Limited break-glass<br/>บัญชีตนเองหรือ verified biller"]
    end

    subgraph result["4. ผลลัพธ์"]
        done(["ส่งคำสั่งเข้าสู่ระบบโอน<br/>เมื่อผ่านเงื่อนไขแล้ว"])
        cancel(["ยกเลิกรายการ<br/>เงินยังไม่ถูกส่ง"])
        report(["แจ้งข้อกังวลและเก็บ audit data ที่จำเป็น"])
        limit["เป้าหมายคือช่วยลดความเสี่ยง<br/>ไม่รับประกันว่าจะหยุด Scam ได้ทุกกรณี"]
    end

    user --> mode
    budget --> request
    reserve --> request
    request --> transfer
    transfer --> context
    transfer --> tx
    transfer -. "สัญญาณจำลอง" .-> destination
    tier -->|Low| low
    tier -->|Medium| medium
    tier -->|High| high
    tier -->|เส้นทางฉุกเฉินที่เข้าเงื่อนไข| emergency
    low --> done
    medium -->|ยืนยันต่อ| done
    medium -->|หยุด| cancel
    high -->|ผ่าน Cooling-off และตรวจสอบแล้ว| done
    high -->|ยกเลิก| cancel
    high -->|แจ้งข้อกังวล| report
    emergency --> done
    done --> limit
    cancel --> limit
    report --> limit

    style prepare fill:#C2E5FF,stroke:#3DADFF
    style assess fill:#DCCCFF,stroke:#874FFF
    style act fill:#FFECBD,stroke:#FFC943
    style result fill:#C6FAF6,stroke:#5AD8CC
    style high fill:#FFCDC2,stroke:#FF7556
    style medium fill:#FFE0C2,stroke:#FF9E42
    style low fill:#CDF4D3,stroke:#66D575
    style cancel fill:#FFCDC2,stroke:#FF7556
```

## Diagram 2 — Core Integrations and Risk Evaluation

```mermaid
flowchart LR
    user(["ผู้ใช้ทำรายการใน K PLUS"])

    subgraph core["Core — 3 Integrations"]
        pocket["1. K-ePocket<br/>ระบุว่าเงินมาจาก Job Search Budget<br/>หรือเงินสำรองก่อนเงินเดือนแรก"]
        transaction["2. K PLUS Transaction + Bank-side Fraud Risk<br/>ผู้รับใหม่ ยอด รูปแบบสะสม<br/>และสัญญาณความเสี่ยงปลายทาง"]
        response["3. K PLUS Security & Fraud Response<br/>คำเตือน การยืนยันที่เข้มขึ้น<br/>Cooling-off และ Cancel/Report"]
    end

    policy["Context-aware multi-signal policy<br/>ใช้ deterministic rules กับ synthetic data ใน Prototype"]
    decision{"Low / Medium / High / Break-glass"}

    subgraph future["Optional / Future — ไม่ใช่ Core"]
        shared["ผู้ใช้เลือกส่ง Email/Link เพื่อตรวจ<br/>ต้องขอ consent รายครั้ง"]
        specialist["Fraud Specialist workflow"]
        employer["Verified-employer / registry lookup"]
    end

    user --> pocket
    user --> transaction
    pocket --> policy
    transaction --> policy
    policy --> decision --> response
    shared -. "optional signal" .-> policy
    response -. "future escalation" .-> specialist
    employer -. "future verification" .-> response

    style core fill:#DCCCFF,stroke:#874FFF
    style future fill:#F2F2F2,stroke:#999999,stroke-dasharray:5 5
    style policy fill:#FFECBD,stroke:#FFC943
    style response fill:#C6FAF6,stroke:#5AD8CC
```

## Diagram 3 — High-Risk Cooling-off

```mermaid
sequenceDiagram
    actor U as ผู้ใช้
    participant A as K PLUS / JobShield
    participant P as Multi-signal Policy
    participant Q as Pending Instruction Queue
    participant R as ระบบโอน / PromptPay

    U->>A: ตรวจสอบรายการโอนไปผู้รับใหม่
    A->>P: ส่ง Career Mode, แหล่งเงิน, ผู้รับ, ยอด และสัญญาณปลายทาง
    P-->>A: High Risk พร้อมเหตุผลที่สังเกตได้ 2–3 ข้อ
    A-->>U: แสดง Pause & Verify และ Cancel/Report

    alt ผู้ใช้เลือก Pause & Verify
        A->>Q: พักคำสั่งเป็น Pending Instruction
        Note over Q,R: ระหว่าง Cooling-off ยังไม่ส่งคำสั่งเข้าสู่ระบบโอน/PromptPay
        A-->>U: แนะนำให้ตรวจสอบผ่านช่องทางบริษัทที่หาเอง
        U->>A: กลับมายืนยันหลังผ่านเงื่อนไข
        A->>P: ประเมินซ้ำและทำ stronger verification ตาม policy
        alt ผ่านเงื่อนไขและผู้ใช้ยืนยันต่อ
            Q->>R: ส่งคำสั่งโอน
            R-->>U: แสดงผลรายการ
        else ยังคลุมเครือหรือผู้ใช้ยกเลิก
            A->>Q: ยกเลิก Pending Instruction
            Q-->>U: เงินยังไม่ถูกส่ง
        end
    else ผู้ใช้เลือก Cancel/Report
        A->>Q: ไม่สร้างหรือยกเลิก Pending Instruction
        A-->>U: ยืนยันว่าเงินยังไม่ถูกส่ง และเปิดทางแจ้งข้อกังวล
    else Limited break-glass ที่เข้าเงื่อนไข
        Note over A,P: จำกัดเฉพาะบัญชีตนเองหรือ verified biller<br/>ไม่ใช้เป็นทางลัดสำหรับผู้รับใหม่
        A->>R: ส่งคำสั่งเมื่อผ่านการตรวจตาม policy
        R-->>U: แสดงผลรายการ
    end
```

## คำอธิบายสัญลักษณ์และขอบเขต

- เส้นทึบ = เส้นทางหลักหรือข้อมูลที่ Core ใช้จริงในแนวคิด
- เส้นประ = ข้อมูลจำลอง, Optional/Future integration หรือความเชื่อมโยงที่ยังไม่ยืนยัน
- `Destination risk` = สัญญาณจากระบบ Fraud Risk ฝั่งธนาคารที่ Prototype จำลองขึ้นด้วย synthetic flag; ทีมไม่ได้อ้างว่าเข้าถึงข้อมูลภายในจริง
- `Dynamic Time Lock` = กลไกที่ปรับระดับการพักตามความเสี่ยงภายใน Cooling-off ไม่ใช่ฟีเจอร์แยก และ Prototype ยังไม่กำหนดระยะเวลาจริง
- `Pending Instruction` = คำสั่งที่ถูกพักไว้ก่อนเข้าสู่ระบบโอน/PromptPay; จึงไม่ใช่การดึงเงินกลับหลังโอนสำเร็จ
- JobShield ไม่อ่านข้อความหรืออีเมลอัตโนมัติ Email/Link scanning จะมีได้เฉพาะส่วน Optional/Future และต้องขอ consent ทุกครั้ง
- Prototype ใช้ rules/policy และ synthetic data ไม่ได้มี ML model และไม่แสดงคะแนนที่อ้างว่าเป็นผลจากโมเดลจริง
- การทำรายการสำเร็จไม่ได้แปลว่าระบบรับรองนายจ้างหรือรับประกันว่าปลอดภัยจาก Scam
