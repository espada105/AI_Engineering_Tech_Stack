from langgraph.graph import StateGraph, MessagesState, START, END

def mock_llm(state: MessagesState) -> str:
    if state == START:
        return "Hello! How can I assist you today?"
    elif state == END:
        return "Goodbye! Have a great day!"
    else:
        return "I'm here to help with any questions you have."


print(mock_llm((START)))