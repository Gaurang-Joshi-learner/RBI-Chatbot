# app/services/context/context_prompt_builder.py

from app.services.conversation.conversation_state import ConversationState


def build_contextual_prompt(
    *,
    question: str,
    retrieved_context: str,
    conversation_state: ConversationState
) -> str:

    memory_block = conversation_state.get_recent_context()

    prompt = f"""
You are an expert RBI regulatory assistant.

Rules you MUST follow:
1. Answer ONLY using the provided RBI document context.
2. Do NOT use outside knowledge.
3. Cite document titles and issue dates.
4. Be precise and factual.
5. If information is missing, say so clearly.

Conversation History:
{memory_block}

Document Context:
{retrieved_context}

Question:
{question}

Answer:
"""

    return prompt.strip()
