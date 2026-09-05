# AGENTS.md — KBTG Kampus Hackathon 2026

## 1. Purpose of this repository

This repository is the working space for preparing an application and, if selected, subsequent work for **KBTG Kampus Hackathon 2026 — Intern Edition**.

Codex must act as a careful product, cybersecurity, research, writing, and prototyping partner. The immediate objective is to create a strong **one-page pitch proposal in PDF format**. Later work may include idea validation, judge-question rehearsal, presentation preparation, security architecture, a clickable prototype, a proof of concept, and technical documentation.

Do not treat the current idea as final merely because it appears in this file. Treat it as a working hypothesis that must survive research and adversarial review.

## 2. Applicant context

Tailor recommendations to the applicant's actual background:

- Computer Science student at Thammasat University.
- Primary interest and strongest fit: cybersecurity, threat detection, network security, endpoint security, fraud detection, and digital trust.
- Hands-on experience includes Wazuh SIEM, phishing investigation, SSH brute-force investigation, IOC extraction, incident reporting, MITRE ATT&CK mapping, Wireshark, Linux, Python, Bash, Docker, and security labs.
- Prior fraud-related experience includes an AI-assisted mule-account detection concept using transaction behavior, graph relationships, transfer frequency, network connectivity, and suspicious fund-flow indicators.
- The applicant wants the hackathon work to support an application for a **Cyber Security internship position at KBTG**.
- Explain unfamiliar concepts in clear Thai. Preserve useful English technical terms in parentheses when they are standard in the industry.
- The applicant may be working alone or in a team of up to three people. Team size and member skills are not yet confirmed. Ask before assigning roles or assuming capabilities.

Use this background to create a coherent story across the proposal, resume, pitch, and interview. Do not exaggerate experience or claim production banking experience.

## 3. Official challenge context

All applicants receive the same main challenge:

> Design a new K PLUS feature, function, service, solution, or digital experience that helps First Jobbers manage their finances and savings more effectively while reducing the risk of becoming victims of Scam or Fraud.

Target users are **First Jobbers aged 22–30**.

Applicants may participate individually or in a team of no more than three people. The application deadline shown in the supplied announcement is **21 September 2026**. Verify time-sensitive details against the current official announcement or form before final submission.

Application materials:

- Resume or CV.
- One-page pitch proposal in PDF format.

Application form supplied by the organizer:

- <https://forms.gle/PU2YCUCGLe6Ei7do6>

Organizer contacts supplied in the announcement:

- supornphan.p@kbtg.tech
- ketsarin.t@kbtg.tech

Do not submit the form, send email, or contact anyone unless the user explicitly asks and approves the exact action.

## 4. Track information

### Track 1 — Software Engineering & Quality

Positions:

- Software Engineer
- AI and Software Testing (Test Automation Engineer)
- Test Engineer

This track must show what will be developed, how it will be developed, and how quality, reliability, testing, and performance will be ensured.

### Track 2 — Data Science & Intelligence

Position:

- Data Science

This track must show how data, analytics, or intelligence helps First Jobbers make better financial decisions.

### Track 3 — Cyber Security & Digital Trust

Position:

- Cyber Security

This is the selected and recommended track for the applicant. The proposal should show how K PLUS can:

- prevent risk;
- detect suspicious behavior or transactions;
- warn users before damage occurs;
- reduce the likelihood that First Jobbers become Scam or Fraud victims; and
- strengthen trust in digital banking.

The core technical perspective must be cybersecurity and digital trust. Machine learning, analytics, and graph analysis may support the solution, but do not let the proposal read primarily like a Track 2 data-science project.

## 5. Submission requirement

The first-round deliverable is exactly **one page in PDF format** and must include all five required sections:

1. **Problem Statement** — What problem is being solved?
2. **Proposed Solution** — What feature, service, solution, or digital experience is proposed?
3. **Target Users** — Who benefits from it?
4. **Value Proposition** — What value does it create for users and K PLUS?
5. **Track Perspective** — How does it relate to the selected technical track and position?

Teams will be selected for Pitching Day based on proposal quality. The proposal will become the foundation for later presentation development.

The organizer has not yet been shown specifying whether the PDF body must be Thai or English. Preserve the required English section headings unless the user chooses otherwise, and ask before making a final language decision. The event itself is stated to be conducted in Thai.

## 6. Current working concept — not yet final

Working name:

**K PLUS SafeStart — จัดเงินเป็น ปลอดภัยก่อนโอน**

Alternative working name previously considered:

**K PLUS Salary Shield — เงินเดือนก้อนแรก ออมมั่นใจ ปลอดภัยก่อนโอน**

Working concept:

Create a security-aware money-management experience for First Jobbers. It helps users understand what they can safely spend, protect important savings, and receive contextual interventions before a high-risk transfer is completed.

Possible components:

1. **Safe-to-Spend**
   - Shows an amount that can be spent after accounting for planned bills, emergency reserves, and savings goals.
   - This is the financial-management layer, not the main cybersecurity novelty.

2. **Protected Savings**
   - Lets the user mark emergency or goal-based funds as requiring stronger protection before withdrawal or transfer.
   - Protection must not imply that legitimate funds are permanently inaccessible.

3. **Smart Scam Intervention**
   - Assesses contextual transaction risk before money is sent.
   - Potential signals include a new payee, unusual amount, unusual time, rapid withdrawal from protected savings, device or session changes, behavioral anomalies, and risk relationships around the recipient account.

4. **Explainable Warning**
   - Tells the user why the transaction appears risky in plain language.
   - Avoid generic warnings that users will habitually dismiss.

5. **Risk-based Action**
   - Low risk: allow the normal flow.
   - Medium risk: show a contextual warning and require deliberate confirmation.
   - High risk: use stronger verification, a carefully designed cooling-off step, or another justified control.
   - Always consider emergency access, accessibility, false positives, and user autonomy.

6. **Rapid Response**
   - Offer a clear path to pause outgoing transactions, preserve incident details, and reach the bank's fraud-reporting process when the user suspects deception.

The differentiating hypothesis is not merely “budgeting plus fraud detection.” It is a **security layer protecting goal and emergency money at the exact moment a user is pressured into a risky transaction**. Codex must test whether this distinction is genuinely novel, understandable, feasible, and valuable.

## 7. Existing-product landscape and duplication risk

Do not propose common features as if KBank has never implemented them. Current public information indicates that:

- K PLUS already supports income/expense summaries, saving support, and K-ePocket.
- K-ePocket already allows users to separate money into spending, saving, and goal pockets.
- MAKE by KBank already provides Cloud Pocket, budgeting, saving goals, and transaction organization.
- KBank publicly describes controls such as risk-aligned daily transaction limits, facial verification for important transactions, suspicious destination detection, alerts, and fraud-reporting support.

Starting official sources:

- K PLUS: <https://www.kasikornbank.com/th/kplus/>
- K-ePocket: <https://www.kasikornbank.com/th/personal/Digital-banking/Pages/k-epocket.aspx>
- MAKE by KBank: <https://makebykbank.kbtg.tech/>
- KBank cyber-risk information: <https://www.kasikornbank.com/th/personal/digital-banking/kbankcyberrisk/pages/index.aspx>
- KBank anti-fraud announcement: <https://www.kasikornbank.com/th/news/pages/sati_fighter.aspx>

These pages can change. Recheck current official information before making competitive or novelty claims. Clearly label inferences. Cite the exact supporting page near each externally verifiable claim.

Avoid submitting any of the following without a clearly defensible innovation:

- a generic expense tracker;
- ordinary saving pockets or saving goals;
- a generic suspicious-account checker;
- a warning that only says “this transaction may be risky”;
- a generic financial-advice chatbot;
- a feature that reads personal messages, calls, or other sensitive data by default;
- a solution that depends on unavailable KBank internal APIs or data without stating assumptions; or
- a claim that AI can guarantee prevention of all fraud.

## 8. Required working process

### Phase A — Understand and research

Before drafting the final proposal:

1. Read this file and inspect all relevant project files.
2. Identify which facts come from the organizer, which come from official public sources, and which are hypotheses.
3. Verify current K PLUS, K-ePocket, MAKE by KBank, Scam, and Fraud capabilities using authoritative sources.
4. Research First Jobber financial behavior and relevant Scam/Fraud patterns. Prefer Thai primary or authoritative sources such as regulators, banks, police, official statistics, and original research.
5. Do not invent statistics, user interviews, market size, model accuracy, loss reduction, or adoption rates.
6. Record sources and access dates in a research note before using factual claims in the proposal.

### Phase B — Plan

Use Plan mode or a Plan skill when available. Otherwise perform the same workflow manually.

The plan must:

- clarify team size, member skills, submission language, available time, and whether a prototype is expected;
- define the user and a specific high-risk scenario;
- compare at least three plausible solution directions before locking the concept;
- identify why each direction belongs to Track 3;
- compare each direction against existing K PLUS and KBank capabilities;
- choose a narrow, demonstrable core rather than a collection of unrelated features;
- list assumptions that require evidence;
- define success criteria and failure conditions; and
- produce a timeline with a buffer before 21 September 2026.

Do not start coding or designing the final PDF while major product assumptions remain unresolved.

### Phase C — Grill the idea

Use a Grill Me skill when available. Otherwise conduct an adversarial judge interview manually.

Ask one important question at a time. Wait for the user's answer, critique it honestly, identify unsupported assumptions, and only then continue. Cover at least:

- Why First Jobbers specifically?
- What exact moment or behavior creates the risk?
- What is new compared with K-ePocket, MAKE by KBank, and current fraud controls?
- Why is this Track 3 rather than Track 2?
- What data and signals are required, and are they realistically available?
- How could attackers evade or manipulate the system?
- How will false positives, warning fatigue, and legitimate emergencies be handled?
- What happens if a victim trusts the scammer and intentionally confirms every step?
- How are privacy, consent, explainability, accessibility, and user autonomy protected?
- What can be demonstrated without real bank data or internal infrastructure?
- What outcome can be measured credibly?
- Why should K PLUS build this instead of using an existing control?

Do not praise weak answers. Help the user strengthen them with evidence and clear reasoning.

### Phase D — Draft the one-page proposal

Only after the concept passes the review:

1. Write a single-sentence value proposition.
2. Draft the five required sections with concise, concrete language.
3. Make the user journey understandable within seconds.
4. Keep the cybersecurity mechanism credible but brief.
5. Show value for both users and K PLUS.
6. Separate facts from assumptions and future possibilities.
7. Use a clean hierarchy and no dense wall of text.
8. Keep technical terms understandable to mixed technical and business judges.
9. Ensure the applicant's experience supports the chosen technical story without turning the proposal into a CV.

Recommended page hierarchy:

- Title and one-line value proposition.
- Problem Statement and Target Users.
- A simple three-step user flow for the Proposed Solution.
- Value Proposition for user and K PLUS.
- Track 3 technical perspective.
- Optional compact evidence or source footer if space permits.

### Phase E — Verify the PDF

When asked to create the final PDF:

- Produce exactly one page.
- Render the PDF to an image and inspect it visually.
- Check for overflow, clipping, tiny text, broken Thai fonts, missing glyphs, low contrast, and inconsistent spacing.
- Confirm all five required sections are present.
- Confirm the title, track, age range, and deadline-related statements are correct.
- Confirm every statistic and factual claim has a reliable source.
- Confirm the PDF opens correctly and remains readable at normal zoom.
- Do not mark the file final until visual verification passes.

## 9. Security and technical design principles

When expanding the concept, consider the following without pretending that every item must be implemented:

- Threat modeling: identify victim, attacker, asset, attack path, trust boundary, and control.
- Defense in depth: do not rely on one model score or one warning.
- Risk-based controls: intervention strength should match risk.
- Explainability: communicate observable reasons without revealing rules that make evasion easy.
- Data minimization: collect only necessary data.
- Consent: optional scanning of a suspicious link or message must be explicit; do not silently inspect personal communications.
- Secure defaults with user control.
- Fail-safe behavior that does not trap users or create financial harm.
- Model and rule monitoring for drift and changing scam tactics.
- Human escalation and incident-response paths.
- Fairness and accessibility across users with different behavior patterns or technical literacy.
- Auditability without exposing sensitive customer data.

Possible prototype architecture, only if later required:

1. Mobile user-flow prototype.
2. Synthetic transaction-event generator.
3. Rules or mock risk-scoring service.
4. Optional synthetic transaction graph for mule-account risk demonstration.
5. Policy engine mapping risk levels to warnings and verification steps.
6. Explainable result returned to the interface.
7. Tests covering normal transfers, suspicious transfers, false positives, bypass attempts, and emergency cases.

Use synthetic data only. Never use real account numbers, credentials, customer data, or private banking information.

## 10. Metrics and evaluation

Do not claim target improvements without evidence. Potential metrics to discuss or simulate include:

- scam or suspicious transactions identified before completion;
- warning precision and false-positive rate;
- user cancellation or pause rate after a contextual warning;
- percentage of protected emergency or goal funds retained;
- warning-dismissal rate and warning fatigue;
- time from suspicion to transaction pause or incident report;
- task-completion time for legitimate transactions;
- user comprehension of the warning reason; and
- perceived trust in K PLUS.

Distinguish clearly among product metrics, security metrics, user-experience metrics, and unvalidated hypotheses.

## 11. Writing and communication rules

- Communicate with the user primarily in Thai unless asked otherwise.
- Use plain language first, then explain technical terms.
- Lead with the conclusion and evidence.
- Be direct when an idea is duplicated, infeasible, too broad, unsupported, or misaligned with Track 3.
- Ask only questions that materially affect the result, preferably one at a time during idea grilling.
- Do not silently choose team composition, proposal language, visual style, implementation stack, or unverified data sources.
- When several choices are viable, recommend one and explain the tradeoff.
- Keep final proposal wording concise even though research notes may be detailed.
- Preserve exact organizer terminology: First Jobbers, K PLUS, Scam, Fraud, Cyber Security & Digital Trust, and one-page pitch proposal.

## 12. Repository and artifact guidance

If the project grows, prefer this structure:

```text
.
├── AGENTS.md
├── README.md
├── research/
│   ├── sources.md
│   ├── competitor-gap.md
│   └── user-problem.md
├── proposal/
│   ├── proposal-draft.md
│   ├── proposal-final.pdf
│   └── assets/
├── pitch/
│   ├── judge-questions.md
│   └── presentation-outline.md
└── prototype/
```

Do not create every folder preemptively. Create only what the current task needs. Preserve user files and unrelated changes. Do not overwrite a final proposal without retaining or clearly identifying the prior version.

## 13. Definition of done for the application proposal

The proposal is ready only when all of the following are true:

- It is exactly one readable PDF page.
- It includes all five required submission sections.
- It targets First Jobbers aged 22–30.
- It addresses both daily financial management and financial-risk protection.
- Its main technical perspective is Track 3: Cyber Security & Digital Trust.
- It explains a specific user problem and a coherent end-to-end solution.
- It clearly differs from existing K PLUS, K-ePocket, MAKE by KBank, and generic fraud warnings.
- It does not depend on fabricated evidence or unstated access to internal banking data.
- It addresses privacy, false positives, warning fatigue, and legitimate-use friction at an appropriate level.
- It states value for both users and K PLUS.
- It can serve as a credible foundation for Pitching Day and later prototype work.
- The user has reviewed and approved the final wording and visual design before submission.

## 14. First actions for a new Codex session

When beginning work in this repository:

1. Summarize the objective, selected track, submission requirement, current concept, and unresolved decisions in no more than ten bullets.
2. Inspect the available files and report what evidence or deliverables already exist.
3. Ask for the single most important missing detail if it blocks progress.
4. If the concept has not passed adversarial review, begin with Plan and Grill rather than drafting the final PDF.
5. If the user asks for a deliverable, complete and verify it rather than returning only general advice.

Known unresolved decisions at the time this file was created:

- Solo applicant or team, and member roles.
- Final product name.
- Final proposal language.
- Evidence supporting the First Jobber problem statement.
- Exact novelty gap compared with current KBank controls.
- Which controls belong in the one-page proposal versus later presentation.
- Whether a prototype will be required before or only after selection.
