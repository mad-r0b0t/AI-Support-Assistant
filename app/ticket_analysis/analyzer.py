from llm.ollama_client import llm_complete

def analyze_ticket(text):

    prompt = f"""
    Analyze the IT support ticket.

    Ticket:
    {text}

    Extract:
    - category
    - problem_type
    - priority
    - summary

    Respond as JSON.
    """

    result = llm_complete(prompt)

    return result