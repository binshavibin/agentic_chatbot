from src.langgraph.state.state import State

class ChatbotToolNode:
    """
    Chatbot tool integration
    """
    def __init__(self,model):
        self.llm = model
    def process(self,state:State)->dict:
        """
        Process the input and generate chat response with tool integration
        """
        user_input = state['messages'][-1] if state['messages'] else ""
        llm_response = self.llm.invoke([{'role':"user","content":user_input}])

        tools_response = f"Tool integration for {user_input}"
        return {"messages":[llm_response,tools_response]}

    def create_chatbot(self,tools):
        """
        Returns chatbot node function
        """
        llm_witt_tools = self.llm.bind_tools(tools)
        def chatbot_node(state:State):
            """
            Chatbot logic for processing input state and returns response
            """
            return {"messages":[llm_witt_tools.invoke(state['messages'])]}
        return chatbot_node
