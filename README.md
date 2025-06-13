# AI Agents

## Quick Setup

1. **Install UV package manager**:
https://docs.astral.sh/uv/getting-started/installation/

2. **Clone and initialize project**:
```
git clone https://github.com/DominikZurawski/agents.git
cd agents
```

4. **Install dependencies**:
```uv sync```

## Environment Configuration
Create `.env` file with required API credentials:
```
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
GROQ_API_KEY=groq_cloud_key
PUSHOVER_TOKEN=your_pushover_token
PUSHOVER_USER=your_pushover_user
```

# AI Agents Framework (Evaluate_models Branch)

This branch introduces experimental features for evaluating LLM performance and integrating external tools. Below are the key components:


## Core Components
1. 1_simple_LangGraph.ipynb
A basic educational project introducing the capabilities of the LangGraph framework. The project demonstrates:
The creation of simple chatbots using StateGraph
Implementation of conversational interfaces with Gradio
Basic concepts of state management in LangGraph
Integration with ChatOpenAI models
The main objective is to learn the fundamental concepts of building AI agents using add_messages and BaseModel.

2. 2_LangSmith_Tools_memory_SQL.ipynb - Chatbot with Memory and Tools
An advanced chatbot using the full LangChain ecosystem . The project implements:
Integration with LangSmith for monitoring and debugging
External tool system (ToolNode)
Persistent conversation memory using MemorySaver and SqliteSaver
SQLite database management (memory.db, memory.db-shm, memory.db-wal)
This project shows how to create chatbots with long-term memory that can use external tools to perform tasks.

3. 3_News_scrapper.ipynb - News Scraping Agent
A specialised AI agent for automatically reviewing and analysing web content. Functionality includes:
Automatic news scraping using Playwright
Asynchronous web scraping operations (nest_asyncio)
Push notification system via Pushover API
Automatic analysis and processing of news content
The agent is designed to monitor news sources and deliver personalised notifications.

4. 4_Personal_Co-worker.ipynb - Personal Collaborator (Sidekick)
The most advanced project implementing the multi-agent system 'Sidekick' . The system consists of:
Worker Agent: Performs tasks using the available tools
Evaluator Agent: Evaluates the quality of the work performed and compliance with success criteria
Structured outputs using Pydantic
Integration with Playwright's browser automation tools
Project demonstrates advanced multi-agent architecture concepts with structured outputs

5. app.py - Sidekick application
Web application implementing the Sidekick system with additional functionalities :
Web interface (Gradio)
Integration with the sidekick.py module

sidekick.py - The Sidekick Core Module
The central module implementing the logic of the Sidekick system . Includes:
Complete implementation of multi-agent architecture
Asynchronous operations for better performance
Task evaluation system
State and workflow management between agents
