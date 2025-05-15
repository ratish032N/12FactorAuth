from fastapi import FastAPI, APIRouter
import uvicorn
from textblob import TextBlob

app = FastAPI()

@app.get('/')
def root():
    return {"message": "Hello World"}

@app.get("/analyze")
def analyze_sentiment(text: str):
    analysis = TextBlob(text)
    sentiment = "positive" if analysis.sentiment.polarity > 0.1 else "negative" if analysis.sentiment.polarity < -0.1 else "neutral"
    return {"text": text, "sentiment": sentiment}

if __name__ == "__main__":
    uvicorn.run('server.app:app', host="0.0.0.0", port=8000, reload=True)