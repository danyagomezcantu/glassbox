def classify_sentiment(text):
    if "good" in text.lower() or "great" in text.lower():
        return "positive"
    elif "bad" in text.lower() or "hate" in text.lower():
        return "negative"
    else:
        return "neutral"

