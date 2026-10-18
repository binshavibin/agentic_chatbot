from langgraph.graph import StateGraph,START,END
from src.langgraph.state.state import State

class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder= StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Build basic chatbot using langgraph.
        """
        self.graph_builder.add_node("chatbot","")
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)
        