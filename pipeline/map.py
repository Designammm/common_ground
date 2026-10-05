def map_to_common_ground(interpreted):
    return {
        "intent": interpreted["intent"],
        "context": interpreted["context"],
        "constraints": interpreted["constraints"],
        "confidence": interpreted["confidence"],
        "status": "mapped"
    }
