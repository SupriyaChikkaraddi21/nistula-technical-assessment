import os

from anthropic import Anthropic
from dotenv import load_dotenv


load_dotenv()



client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)


PROPERTY_CONTEXT = """
Property: Villa B1, Assagao, North Goa
Bedrooms: 3 | Max guests: 6 | Private pool: Yes
Check-in: 2pm | Check-out: 11am
Base rate: INR 18,000 per night (up to 4 guests)
Extra guest: INR 2,000 per night per person
WiFi password: Nistula@2024
Caretaker: Available 8am to 10pm
Chef on call: Yes, pre-booking required
Availability April 20-24: Available
Cancellation: Free up to 7 days before check-in
"""


def generate_ai_reply(message_text: str, query_type: str):

    prompt = f"""
    You are a hospitality support assistant for Nistula.

    Guest Message:
    {message_text}

    Query Type:
    {query_type}

    Property Context:
    {PROPERTY_CONTEXT}

    Instructions:
    - Reply professionally and warmly
    - Be concise
    - Answer only using provided context
    - If complaint, show empathy
    - Do not invent unavailable information
    """

    try:

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=300,
            temperature=0.3,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.content[0].text

    except Exception as e:

        print("Claude API Error:", e)

        return """
Hi! Thank you for contacting Nistula.

Our support team has received your message and will assist you shortly.
"""