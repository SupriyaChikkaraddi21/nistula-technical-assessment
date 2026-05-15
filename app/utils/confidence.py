def calculate_confidence(query_type: str) -> float:

    confidence_map = {
        "pre_sales_availability": 0.93,
        "pre_sales_pricing": 0.91,
        "post_sales_checkin": 0.89,
        "special_request": 0.78,
        "general_enquiry": 0.74,
        "complaint": 0.42
    }

    return confidence_map.get(query_type, 0.60)