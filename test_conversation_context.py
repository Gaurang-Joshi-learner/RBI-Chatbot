from app.services.conversation.conversation_state import ConversationState
from app.services.conversation.topic_tracker import detect_topic, is_followup

state = ConversationState()

q1 = "What are the KYC requirements for savings accounts?"
topic1 = detect_topic(q1)

state.update_topic(topic1)
state.add_turn(q1, "KYC requirements are defined by RBI circulars.")

q2 = "What about current accounts?"

print("Is followup:", is_followup(q2))
print("Previous topic:", state.current_topic)
print("\nConversation Context:\n")
print(state.get_recent_context())
