from .vector_store import search_context

def generate_ai_response(user_input):

    context = search_context(user_input)

    response = f"""
Medical Information:

{context}

Note: This AI assistant provides general medical information only.
Please consult a doctor for professional advice.
"""

    return response