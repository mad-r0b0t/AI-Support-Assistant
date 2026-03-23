from fastapi import APIRouter, Request
from ticket_analysis.analyzer import analyze_ticket
from llm.ollama_client import generate_reply
from retrieval.vector_store import search_documents
from integrations.zammad_client import add_ticket_note

router = APIRouter()

@router.post("/ticket")
async def ticket_webhook(request: Request):

    data = await request.json()

    ticket_id = data["id"]
    ticket_text = data["article"]["body"]

    analysis = analyze_ticket(ticket_text)

    context_docs = search_documents(ticket_text)

    reply = generate_reply(ticket_text, analysis, context_docs)

    add_ticket_note(ticket_id, reply)

    return {"status": "processed"}