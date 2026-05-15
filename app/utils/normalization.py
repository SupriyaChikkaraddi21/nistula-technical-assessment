import uuid

from datetime import datetime, timezone

from app.schemas.message import (
    IncomingMessage,
    NormalizedMessage
)

from app.services.classifier import classify_message


def normalize_message(payload: IncomingMessage) -> NormalizedMessage:

    timestamp = payload.timestamp or datetime.now(timezone.utc)

    return NormalizedMessage(
        message_id=str(uuid.uuid4()),
        source=payload.source,
        guest_name=payload.guest_name,
        message_text=payload.message,
        timestamp=timestamp,
        booking_ref=payload.booking_ref,
        property_id=payload.property_id,
        query_type=classify_message(payload.message)
    )