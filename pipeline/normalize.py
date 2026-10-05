def normalize_input(message):
    return {
        "raw": message["raw"],
        "normalized": message["raw"].strip(),
        "status": "normalized"
    }
