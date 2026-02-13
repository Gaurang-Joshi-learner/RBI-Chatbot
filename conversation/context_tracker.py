# app/services/conversation/context_tracker.py

class ConversationContext:
    def __init__(self):
        self.current_topic = None
        self.last_question = None

    def update(self, question: str, topic: str | None):
        self.last_question = question
        if topic:
            self.current_topic = topic

    def get_topic(self) -> str | None:
        return self.current_topic


# Global (simple in-memory store)
conversation_context = ConversationContext()
