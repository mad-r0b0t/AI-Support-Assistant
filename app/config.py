import os

OLLAMA_URL = "http://localhost:11434/api/generate"
LLM_MODEL = "llama3"

ZAMMAD_URL = "https://your-zammad-instance/api/v1"
ZAMMAD_TOKEN = os.getenv("ZAMMAD_TOKEN")

VECTOR_DB_PATH = "./vectordb"
EMBEDDING_MODEL = "nomic-embed-text"