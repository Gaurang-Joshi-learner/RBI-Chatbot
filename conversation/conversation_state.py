# app/services/context/conversation_state.py

from typing import List, Dict


class ConversationState:
    def __init__(self, max_turns: int = 5):
        self.max_turns = max_turns
        self.turns: List[Dict] = []
        self.current_topic: str | None = None

    def add_turn(self, user: str, assistant: str | None = None):
        self.turns.append({
            "user": user,
            "assistant": assistant
        })

        if len(self.turns) > self.max_turns:
            self.turns.pop(0)

    def update_topic(self, topic: str):
        self.current_topic = topic

    def clear(self):
        self.turns = []
        self.current_topic = None

    def get_recent_context(self) -> str:
        """
        Returns last N conversation turns as text
        """
        context = []
        for turn in self.turns:
            context.append(f"User: {turn['user']}")
            if turn["assistant"]:
                context.append(f"Assistant: {turn['assistant']}")
        return "\n".join(context)
