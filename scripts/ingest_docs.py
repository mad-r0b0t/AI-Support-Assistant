from app.retrieval.vector_store import add_document

docs = [
    "Outlook login issues are often caused by expired passwords.",
    "VPN issues can be solved by reconnecting or resetting credentials."
]

for d in docs:
    add_document(d)

print("Documents ingested.")
