import streamlit as st

from src.langgraph.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraph.LLMS.groqllm import GroqLLM
from src.langgraph.graph.graph_builder import GraphBuilder
from src.langgraph.ui.streamlitui.display_result import DisplayResult

def load_langgraph_app():
    """
    Loads and runs agentic ai apps wit streamlit ui
    """
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Failed to load user input from ui")
        return


    user_meesage = st.chat_input("Enter your message")
    if user_meesage:
        try:
            obj_llm_config =GroqLLM(user_controls_input=user_input)
            model =obj_llm_config.get_llm_model()

            if not model:
                st.error("Please select model")
                return

            usecase = user_input.get('selected_usecase')
            if not usecase:
                st.error("Please select usecase")
                return
            graph_builder = GraphBuilder(model)

            try:
                graph = graph_builder.setup_graph(usecase)
                display_result = DisplayResult(usecase,graph,user_meesage)
                display_result.display_result_on_ui()
            except Exception as e:
                st.error(f"Graph set up failed: {e}")

        except Exception as e:
            st.error(f"Error: {e}")