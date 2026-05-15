# Nistula Technical Assessment — Thinking Questions

---
# Question A — Immediate Response

## AI Reply

Hi, and I sincerely apologize for the inconvenience caused.

I understand how stressful this is, especially with guests arriving in a few hours. I have marked this as an urgent maintenance issue and alerted the on-call support team immediately.

A team member will contact you shortly with an update and next steps. We will do our best to resolve this as quickly as possible and assist you further regarding your refund request after the issue is reviewed.

## Why I Chose This Response

The response prioritizes empathy, urgency, and accountability without making unrealistic promises. Since this is a high-stress operational issue happening late at night, the guest needs reassurance that the problem has already been escalated to humans and is actively being handled.
---

# Question B — System Design

When the complaint is received, the platform should:

1. Classify the message as a high-priority complaint.
2. Automatically escalate the issue instead of auto-sending a fully AI-generated resolution.
3. Notify the on-call operations manager and maintenance contact immediately through SMS, WhatsApp, or push notification.
4. Create an incident log linked to the reservation and property.
5. Start a response timer and monitor whether a human agent responds within 30 minutes.

If no human responds within 30 minutes:
- escalate to a secondary manager,
- notify senior operations staff,
- and continue sending reminders until acknowledged.

The system should also store:
- timestamps,
- escalation history,
- AI confidence score,
- and final resolution outcome for future analysis.

---

# Question C — Learning

If the same hot water complaint occurs multiple times at Villa B1, the platform should identify it as a recurring operational issue instead of isolated incidents.

I would build:
- complaint trend monitoring,
- recurring issue detection,
- and automated maintenance recommendations.

For example:
- if similar complaints cross a threshold,
- automatically create a maintenance task,
- notify property managers,
- and temporarily lower AI auto-send confidence for that property.

The goal is to move from reactive support to proactive prevention by identifying operational patterns early.