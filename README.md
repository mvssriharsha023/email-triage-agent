# email-triage-agent
AI Email Triage &amp; Task Agent

### Problem Statement
People receive too many emails/messages/tasks

The agent should:
1. Read incoming email text
2. Check if email is spam or legitimate
3. Classify urgency
4. Extract action items
5. Decide who should handle it
6. Generate a response draft
7. Save task state
8. Ask human approval if confidence is low

                     ┌────────────────────┐
                     │ Incoming Email     │
                     └─────────┬──────────┘
                               │
                               ▼
                  ┌────────────────────────┐
                  │ Spam Detection Node    │
                  └─────────┬──────────────┘
                            │
                 ┌──────────┴──────────┐
                 │                     │
                 ▼                     ▼
        ┌────────────────┐    ┌──────────────────┐
        │ Spam Email     │    │ Valid Email      │
        │ End Workflow   │    │ Continue Flow    │
        └────────────────┘    └────────┬─────────┘
                                       │
                                       ▼
                     ┌────────────────────────┐
                     │ Classification Node    │
                     │ (billing/tech/hr/etc) │
                     └─────────┬──────────────┘
                               │
                               ▼
                     ┌────────────────────────┐
                     │ Urgency Detection      │
                     │ (high/medium/low)      │
                     └─────────┬──────────────┘
                               │
                               ▼
                     ┌────────────────────────┐
                     │ Task Extraction Node   │
                     └─────────┬──────────────┘
                               │
                               ▼
                     ┌────────────────────────┐
                     │ Owner Assignment Node  │
                     └─────────┬──────────────┘
                               │
                               ▼
                     ┌────────────────────────┐
                     │ Response Draft Node    │
                     └─────────┬──────────────┘
                               │
                               ▼
                     ┌────────────────────────┐
                     │ Human Approval Check   │
                     └─────────┬──────────────┘
                               │
                  ┌────────────┴────────────┐
                  │                         │
                  ▼                         ▼
         ┌────────────────┐      ┌──────────────────┐
         │ Auto Approve   │      │ Needs Human      │
         │ Save Result    │      │ Review           │
         └────────────────┘      └──────────────────┘