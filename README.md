# AI Support Assistant

AI-powered IT support assistant integrated with Zammad.

## Features

- Ticket ingestion via webhook
- Ticket analysis using LLM
- Knowledge retrieval (RAG)
- Suggested replies for support agents

## Setup

### 1. Clone repo

```bash
git clone https://github.com/mad-r0b0t/Ai-Support-Assistant.git
cd ai-support-assistant
2. Install dependencies
pip install -r requirements.txt
3. Configure environment
cp .env.example .env

Edit .env

4. Start server
uvicorn app.main:app --reload --port 8000
5. Configure Zammad webhook

URL:

http://your-server:8000/ticket

Trigger:

Ticket Created

Future roadmap

auto-reply

ticket classification

similarity search


---

# 📄 app/config.py

```python
import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL")
LLM_MODEL = os.getenv("LLM_MODEL")

ZAMMAD_URL = os.getenv("ZAMMAD_URL")
ZAMMAD_TOKEN = os.getenv("ZAMMAD_TOKEN")

VECTOR_DB_PATH = "./data/vectordb"
