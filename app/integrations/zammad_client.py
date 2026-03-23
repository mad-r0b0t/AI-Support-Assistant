import requests
from config import ZAMMAD_URL, ZAMMAD_TOKEN

headers = {
    "Authorization": f"Token token={ZAMMAD_TOKEN}",
    "Content-Type": "application/json"
}

def add_ticket_note(ticket_id, text):

    url = f"{ZAMMAD_URL}/ticket_articles"

    payload = {
        "ticket_id": ticket_id,
        "body": text,
        "type": "note",
        "internal": True
    }

    requests.post(url, json=payload, headers=headers)