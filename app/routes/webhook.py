from fastapi import APIRouter

from app.schemas.message import IncomingMessage
from app.schemas.response import MessageResponse

from app.utils.normalization import normalize_message
from app.utils.logger import logger
from app.utils.confidence import calculate_confidence

from app.services.claude_service import generate_ai_reply
from app.utils.action import determine_action

router = APIRouter(
    prefix="/webhook",
    tags=["Webhook"]
)




@router.post("/message", response_model=MessageResponse)
async def receive_message(payload: IncomingMessage):

    logger.info(f"Message received from {payload.guest_name}")

    normalized_message = normalize_message(payload)

    logger.info(
        f"Message classified as {normalized_message.query_type}"
    )

    drafted_reply = generate_ai_reply(
        normalized_message.message_text,
        normalized_message.query_type
    )

    confidence_score = calculate_confidence(
        normalized_message.query_type
    )

    action = determine_action(
        confidence_score,
        normalized_message.query_type
    )

    return {
        "status": "success",
        "data": {
            "message_id": normalized_message.message_id,
            "query_type": normalized_message.query_type,
            "drafted_reply": drafted_reply,
            "confidence_score": confidence_score,
            "action": action
        }
    }