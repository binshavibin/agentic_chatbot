from src.langgraph.state.state import State
from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate

class AINewsNode:
    def __init__(self,llm):
        """
        Initialize the AINewsNode with APIKeys for Tavily and Groq
        """
        self.tavily = TavilyClient()
        self.llm = llm
        self.state = {}

    def fetch_news(self,state:dict) ->dict:
        """
        Fetch AI news based on specific frequency
        Args:
            state(dict): State dictionary containing 'frequency'
        Returns: 
            dict:Updated news with 'news_data' key containing fetched news
        """

        frequency = state['messages'][0].content.lower()
        self.state['frequency'] = frequency
        time_range_map = {'daily':'d','weekly':'w','monthly':'m','yearly':'y'}
        days_map = {'daily':1,'weekly':7,'monthly':30,'yearly':365}

        response = self.tavily.search(
            query = "Top AI(Artificial Intelligence) technology news india and globally",
            topic="news",
            time_range=time_range_map[frequency],
            include_answer='advanced',
            max_result = 10,
            days= days_map[frequency]
        )

        state['news_data'] = response.get('result',[])
        self.state['news_data'] = state['news_data']
        return state

