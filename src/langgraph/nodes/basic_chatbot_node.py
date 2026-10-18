from src.langgraph.state.state import State

class BasicChatbotNode:
    """
    Basic chatbot node implementation
    """
    def __init__(self,model):
        self.model = model

    def process(self,state:State)->dict:
        """
        Process the input and generate chat response
        """
        return {"messages":self.llm.invoke(state['messages'])}
