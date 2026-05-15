# Nistula Technical Assessment

AI-powered guest messaging backend system built using FastAPI.

The system receives guest messages from multiple channels, normalizes them into a unified schema, classifies the query type, generates AI-assisted replies using Claude integration, and returns a confidence score with automated action routing.

---

# Features

- FastAPI webhook backend
- Unified message normalization
- Query classification engine
- Claude API integration layer
- Graceful AI failure fallback handling
- Confidence scoring system
- Action routing (`auto_send` / `agent_review` / `escalate`)
- Structured logging
- Swagger API documentation
- PostgreSQL schema design
- Clean modular project structure

---

# Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- Anthropic SDK
- PostgreSQL (schema design)

---

# Project Structure

```bash
app/
│
├── main.py
│
├── routes/
│   └── webhook.py
│
├── schemas/
│   ├── message.py
│   └── response.py
│
├── services/
│   ├── classifier.py
│   └── claude_service.py
│
├── utils/
│   ├── normalization.py
│   ├── confidence.py
│   ├── action.py
│   └── logger.py
│
├── tests/
│
schema.sql
thinking.md
README.md
requirements.txt
.env.example
```

---

# Webhook Endpoint

## POST `/webhook/message`

Receives inbound guest messages from supported channels.

Supported sources:

- whatsapp
- booking_com
- airbnb
- instagram
- direct

---

# Sample Request

```json
{
  "source": "whatsapp",
  "guest_name": "Rahul Sharma",
  "message": "Is the villa available from April 20 to 24?",
  "booking_ref": "REF001",
  "property_id": "villa-b1"
}
```

---

# Sample Response

```json
{
  "status": "success",
  "data": {
    "message_id": "uuid",
    "query_type": "pre_sales_availability",
    "drafted_reply": "Hi! Thank you for contacting Nistula...",
    "confidence_score": 0.93,
    "action": "auto_send"
  }
}
```

---

# Query Types

The system classifies messages into:

- pre_sales_availability
- pre_sales_pricing
- post_sales_checkin
- special_request
- complaint
- general_enquiry

---

# Confidence Scoring Logic

Confidence scores are rule-based and represent how safe it is for the platform to auto-send an AI-generated response.

Examples:

- Availability and pricing queries → high confidence
- Special requests → medium confidence
- Complaints → low confidence

Routing logic:

- Above 0.85 → `auto_send`
- Between 0.60 and 0.85 → `agent_review`
- Below 0.60 or complaints → `escalate`

---

# Claude Integration

The system integrates with the Claude API using the Anthropic SDK.

If the external AI provider fails or authentication is unavailable, the system gracefully falls back to a safe default response instead of crashing.

Note: The provided assessment Claude API key returned authentication errors during testing. Graceful fallback handling was implemented to ensure API reliability and prevent endpoint failures.

---

# Run Locally

## Install dependencies

```bash
pip install -r requirements.txt
```

## Start FastAPI server

```bash
uvicorn app.main:app --reload
```

## Open Swagger Docs

```text
http://127.0.0.1:8000/docs
```

---

# Environment Variables

Create a `.env` file:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

---

# Testing

Tested with:

- availability queries
- pricing queries
- WiFi/check-in questions
- special requests
- complaints

---

# Author

Supriya Chikkaraddi