def detect(context):
    if context.get("scheduled"):
        return False

    if context.get("requested"):
        return False

    if not context.get("anomaly"):
        return False

    if context.get("anomaly").get("repeatable"):
        return False

    return True
