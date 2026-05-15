from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class IncomingMessage(BaseModel):
    source: str
    guest_name: str
    message: str
    timestamp: Optional[datetime] = None
    booking_ref: str
    property_id: str


class NormalizedMessage(BaseModel):
    message_id: str
    source: str
    guest_name: str
    message_text: str
    timestamp: datetime
    booking_ref: str
    property_id: str
    query_type: str