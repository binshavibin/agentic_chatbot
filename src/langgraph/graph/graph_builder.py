from langgraph.graph import StateGraph,START,END
from src.langgraph.state.state import State
from src.langgraph.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraph.tools.search_tool import get_tools,create_tools_node
from langgraph.prebuilt import tools_condition,ToolNode
from src.langgraph.nodes.chatbot_with_tools_node import ChatbotToolNode



class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder= StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Build basic chatbot using langgraph.
        """
        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def chatbot_with_tools_with_graph(self):
        """
        Build an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both chatbot and tool.
        """
        #Define the tools and tool node
        tools = get_tools()
        tool_node =create_tools_node(tools)

        #Defins LLM
        llm = self.llm

        obj_chat = ChatbotToolNode(llm)
        chatbot_node = obj_chat.create_chatbot(tools)

        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)

        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def ai_news_builder_graph(self):
        self.graph_builder.add_node("fetch_news","")
        self.graph_builder.add_node("summarize_news","")
        self.graph_builder.add_node("save_result","")

        self.graph_builder.set_entry_point("fetch_news")
        self.graph_builder.add_edge("fetch_news","summarize_news")
        self.graph_builder.add_edge("summarize_news","save_result")
        self.graph_builder.add_edge("save_result",END)





    def setup_graph(self,usecase:str):
        """
        Setup graph for specific usecase
        """
        if usecase =="Basic Chatbot":
            self.basic_chatbot_build_graph()
        if usecase =="Chatbot with Web":
            self.chatbot_with_tools_with_graph()

        return self.graph_builder.compile()

        