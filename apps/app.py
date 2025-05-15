from fastapi import FastAPI, APIRouter
from textblob import TextBlob

router = APIRouter()

@router.get("/analyze")
def analyze_sentiment(text: str):
    analysis = TextBlob(text)
    sentiment = "positive" if analysis.sentiment.polarity > 0.1 else "negative" if analysis.sentiment.polarity < -0.1 else "neutral"
    return {"text": text, "sentiment": sentiment}