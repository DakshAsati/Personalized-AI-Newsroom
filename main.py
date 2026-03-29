from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from news import fetch_news
from ai import generate_briefing, answer_question

app = FastAPI()

# ----------- Request Models -----------

class UserInput(BaseModel):
    interests: List[str]

class QuestionInput(BaseModel):
    question: str
    context: str


# ----------- Routes -----------

@app.get("/")
def home():
    return {"message": "AI Newsroom Backend Running"}


@app.post("/get-news")
def get_news(data: UserInput):
    """
    Step 1: Fetch news based on user interests
    """
    news_articles = fetch_news(data.interests)
    return {"articles": news_articles}


@app.post("/generate-briefing")
def briefing(data: UserInput):
    """
    Step 2: Generate AI summary / briefing
    """
    news_articles = fetch_news(data.interests)
    briefing = generate_briefing(news_articles)
    return {"briefing": briefing}


@app.post("/ask")
def ask_question(data: QuestionInput):
    """
    Step 3: Ask questions on news
    """
    answer = answer_question(data.question, data.context)
    return {"answer": answer}
