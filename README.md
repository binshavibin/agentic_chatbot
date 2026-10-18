# Agentic AI Chatbot

An end-to-end agentic AI chatbot built with **LangGraph**, **LangChain** and **Streamlit**. It uses **Groq** LLMs and the **Tavily** search API, and each use case runs as its own stateful LangGraph graph.

## Features

| Use case | What it does |
|---|---|
| **Basic Chatbot** | Simple conversational chatbot: `START → chatbot → END` |
| **Chatbot with Web** | Chatbot with Tavily web search as a tool. The LLM decides when to call it: `chatbot ⇄ tools` |
| **AI News** | Fetches the latest AI news (daily / weekly / monthly) with Tavily, summarizes it with the LLM, and saves it as Markdown: `fetch_news → summarize_news → save_result` |
| **Blog Generator** | *Planned.* It appears in the use-case list but isn't built yet. |

## Project Structure

```
agentic_chatbot/
├── app.py                         # Streamlit entry point
├── requirements.txt
└── src/
    ├── AINews/                    # Generated news summaries ({frequency}_summary.md)
    └── langgraph/
        ├── main.py                # Loads the UI, builds the graph, runs it
        ├── LLMS/groqllm.py        # Groq LLM setup
        ├── graph/graph_builder.py # Builds a LangGraph graph for each use case
        ├── nodes/                 # Graph nodes (basic chatbot, tool chatbot, AI news)
        ├── state/state.py         # Graph state definition
        ├── tools/search_tool.py   # Tavily search tool + ToolNode
        └── ui/
            ├── uiconfigfile.ini   # Page title, LLM, model and use-case options
            ├── uiconfigfile.py    # Config reader
            └── streamlitui/       # Sidebar controls and result display
```

## Prerequisites

- Python 3.10+ (developed on 3.13)
- A [Groq API key](https://console.groq.com/keys)
- A [Tavily API key](https://app.tavily.com/), needed for **Chatbot with Web** and **AI News**

## Setup

```bash
git clone <your-repo-url>
cd agentic_chatbot

python -m venv chatbotvenv
# Windows
chatbotvenv\Scripts\activate
# macOS / Linux
source chatbotvenv/bin/activate

pip install -r requirements.txt
```

## Run

Run from the project root. The config and output paths are relative to it.

```bash
streamlit run app.py
```

Then, in the sidebar:

1. Select the LLM (**Groq**) and a model.
2. Enter your **Groq API key**.
3. Pick a use case:
   - **Basic Chatbot**: type in the chat box.
   - **Chatbot with Web**: also enter your **Tavily API key**, then chat.
   - **AI News**: enter your Tavily key, choose a timeframe, and click **Fetch latest AI News**. The summary appears in the app and is saved to `src/AINews/<timeframe>_summary.md`.

API keys are entered in the UI. Keep any local `.env` file out of version control; it's already in `.gitignore`.

## Configuration

Edit [src/langgraph/ui/uiconfigfile.ini](src/langgraph/ui/uiconfigfile.ini) to change the page title, LLM providers, Groq models or use cases:

```ini
[DEFAULT]
PAGE_TITLE = Langgraph build  stateful agentic ai graph
LLM_OPTIONS = Groq
USECASE_OPTIONS = Basic Chatbot,Chatbot with Web,AI News,Blog Generator
GROQ_MODEL_OPTIONS = openai/gpt-oss-20b,gemma2-9b-it
```

## Tech Stack

- [LangGraph](https://github.com/langchain-ai/langgraph): stateful agent graphs
- [LangChain](https://python.langchain.com/) (`langchain_core`, `langchain_community`, `langchain_groq`)
- [Groq](https://groq.com/): fast LLM inference
- [Tavily](https://tavily.com/): web and news search
- [Streamlit](https://streamlit.io/): UI
