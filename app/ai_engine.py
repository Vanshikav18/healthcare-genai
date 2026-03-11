from .vector_store import search_context

def generate_ai_response(user_input):

    context = search_context(user_input)

    response = f"""
Based on medical knowledge:

{context}

This information is for educational purposes only.
Please consult a healthcare professional for diagnosis.
"""

    return response