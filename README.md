# 12FactorAuth Sentiment Analysis Service

This project provides a simple sentiment analysis API built with FastAPI. It analyzes the sentiment of text provided by the user and classifies it as positive, negative, or neutral.

## Features

- RESTful API for sentiment analysis
- Docker support for easy deployment
- FastAPI framework for high performance

## Prerequisites

- Docker
- Docker Compose (optional)

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/ratish032N/12FactorAuth.git
cd 12FactorAuth
```

### Build and Run with Docker

1. Build the Docker image:

```bash
docker build -t sentiment-analysis-app .
```

2. Run the container:

```bash
docker run -p 8000:8000 sentiment-analysis-app
```

The API will be available at http://localhost:8000

### Using Docker Compose (Alternative)

If you prefer using Docker Compose:

1. Run with Docker Compose:

```bash
docker compose up
```

## API Usage

### Analyze Sentiment

Endpoint: `/analyze`

Method: GET

Parameters:
- `text`: The text to analyze

Example:

```bash
curl "http://localhost:8000/analyze?text=I%20love%20this%20application"
```

Response:
```json
{
  "text": "I love this application",
  "sentiment": "positive"
}
```

## Development

### Project Structure

```
12FactorAuth/
├── first_assignment/
│   └── apps/
│       └── main.py       # Main application code
├── Dockerfile            # Docker configuration
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

### Dependencies

- FastAPI: Web framework
- TextBlob: Natural language processing library for sentiment analysis
- Uvicorn: ASGI server