def interpret(message):
    return {
        "input": message["normalized"],
        "intent": None,
        "context": {},
        "constraints": [],
        "confidence": None,
        "status": "awaiting_interpretation"
    }
