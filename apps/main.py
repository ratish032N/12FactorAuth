"""
FastAPI application for sentiment analysis using TextBlob.
This module provides endpoints for basic health check and text sentiment analysis.
"""
from fastapi import FastAPI
import uvicorn
from textblob import TextBlob

app = FastAPI()

@app.get('/')
def root():
    """
    Root endpoint that returns a simple hello world message.
    Returns:
        dict: A dictionary containing a greeting message.
    """
    return {"message": "Hello World"}

@app.get("/analyze")
def analyze_sentiment(text: str):
    """
    Analyzes the sentiment of the provided text.
    
    Args:
        text (str): The text to analyze.
        
    Returns:
        dict: A dictionary containing the original text and its sentiment classification.
    """
    analysis = TextBlob(text)
    sentiment = (
        "positive" if analysis.sentiment.polarity > 0.1 
        else "negative" if analysis.sentiment.polarity < -0.1
        else "neutral"
    )
    return {"text": text, "sentiment": sentiment}

if __name__ == "__main__":
    uvicorn.run('server.app:app', host="0.0.0.0", port=8000, reload=True)
