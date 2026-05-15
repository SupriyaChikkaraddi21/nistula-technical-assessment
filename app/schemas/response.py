from pydantic import BaseModel


class WebhookResponseData(BaseModel):
    message_id: str
    query_type: str
    drafted_reply: str
    confidence_score: float
    action: str


class MessageResponse(BaseModel):
    status: str
    data: WebhookResponseData