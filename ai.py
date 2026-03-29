import os
from openai import OpenAI

# Initialize client (make sure you set OPENAI_API_KEY in env)
client = OpenAI(api_key=os.getenv(""))


# ----------- Generate AI Briefing -----------

def generate_briefing(articles):
    """
    Takes list of news articles and generates a personalized briefing
    """

    content = "\n\n".join([f"Title: {a['title']}\nDescription: {a['description']}" for a in articles])

    prompt = f"""
You are an intelligent financial and business news analyst.

Given the following news articles, generate a clear, concise, and insightful daily briefing.

Instructions:
- Summarize key events
- Highlight important trends
- Explain why it matters
- Keep it easy to understand
- Avoid generic summaries

News Articles:
{content}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a sharp news analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    return response.choices[0].message.content


# ----------- Q&A on News -----------

def answer_question(question, context):
    """
    Answer user questions based on generated news briefing
    """

    prompt = f"""
You are a news assistant.

Use the context below to answer the question clearly and accurately.

Context:
{context}

Question:
{question}

Instructions:
- Be precise
- Do not hallucinate
- If answer not found, say "Not enough information"
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You answer based on provided context only."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
