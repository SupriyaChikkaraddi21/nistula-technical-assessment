def classify_message(message: str) -> str:

    message = message.lower()

    if any(word in message for word in [
        "cancel",
        "refund",
        "complaint",
        "bad",
        "issue",
        "problem",
        "not happy",
        "worst"
    ]):
        return "complaint"

    if any(word in message for word in [
        "available",
        "availability",
        "vacant"
    ]):
        return "pre_sales_availability"

    if any(word in message for word in [
        "price",
        "rate",
        "cost",
        "charges",
        "amount"
    ]):
        return "pre_sales_pricing"

    if any(word in message for word in [
        "check in",
        "check-in",
        "wifi",
        "password"
    ]):
        return "post_sales_checkin"

    if any(word in message for word in [
        "airport transfer",
        "early check in",
        "late checkout",
        "special request",
        "chef"
    ]):
        return "special_request"

    return "general_enquiry"