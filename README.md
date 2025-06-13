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
```

# AI Agents Framework (Evaluate_models Branch)

This branch introduces experimental features for evaluating LLM performance and integrating external tools. Below are the key components:


## Core Components
### 1. coder/ - Programming Agent
A directory containing code or modules related to programming agents and automation of coding tasks . The project focuses on creating AI agents capable of performing programming and application development tasks.

### 2. debate/ - LLM Debate System
Advanced multi-agent system for debating between different language models . The project implements:
A knowledge directory structure for storing knowledge resources
Output directory for saving the results of debates
Source code in src/debate with configuration of agents and tasks
Design template for easy creation of a multi-agent system using crewAI
The system is designed to compare and analyse different perspectives by having AI agents collaborate in the debate process .

### 3. engineering_team/
A comprehensive project to simulate an engineering team using AI agents . Functionalities include:
Collaboration of multiple agents to build an application
Configurable team structure via agents.yaml and tasks.yaml
Customisable logic and tools in crew.py and main.py
Generation of team progress reports
The project demonstrates how AI agents can collaborate on complex engineering projects, maximising team effectiveness .

### 4. financial_researcher/ - Financial Analyst
Specialised AI agent system dedicated to financial research and market analysis . The system consists of:
Multi-agent architecture for financial data analysis
Configurable agents in src/financial_researcher/config/agents.yaml
Definable tasks in config/tasks.yaml for different aspects of financial research
Ability to generate detailed financial reports
The project enables the creation of advanced systems for financial analysis using the collective intelligence of AI agents .

### 5. stock_picker/ - Share selector
Advanced AI agent system for analysing and selecting stocks in the financial market . The project offers:
Multi-agent architecture for the analysis of financial instruments
Memory catalogue for storing historical data and context
LLM memory system for better management of long-term analysis
Collaboration between agents to make investment decisions
The system is designed to analyse the stock market and support investment decisions through collective AI intelligence of agents
