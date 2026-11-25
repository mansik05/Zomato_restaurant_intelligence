import re

POSITIVE = {"good", "great", "excellent", "amazing", "delicious", "tasty", "love", "loved", "friendly", "fresh", "wonderful", "awesome", "perfect", "recommend", "best", "pleasant"}
NEGATIVE = {"bad", "poor", "terrible", "awful", "disappointing", "disappointed", "hate", "hated", "cold", "slow", "rude", "worst", "overpriced", "dirty", "unhygienic"}

def score_review(text):
    words = re.findall(r"[a-z]+", str(text).lower())
    pos = sum(w in POSITIVE for w in words)
    neg = sum(w in NEGATIVE for w in words)
    score = pos - neg
    label = "positive" if score > 0 else "negative" if score < 0 else "neutral"
    return score, label

def add_sentiment(df):
    df = df.copy()
    results = df["reviews"].map(score_review)
    df["sentiment_score"] = results.map(lambda x: x[0])
    df["sentiment"] = results.map(lambda x: x[1])
    return df
