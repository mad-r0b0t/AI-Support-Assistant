import requests
from config import OLLAMA_URL, LLM_MODEL

def llm_complete(prompt):

    payload = {
        "model": LLM_MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    return response.json()["response"]


def generate_reply(ticket_text, analysis, context_docs):

    context = "\n".join(context_docs)

    prompt = f"""
You are an IT support assistant.

Ticket:
{ticket_text}

Analysis:
{analysis}

Relevant documentation:
{context}

Generate a helpful support reply.
"""

    return llm_complete(prompt)