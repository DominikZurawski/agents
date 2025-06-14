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

## Core Components

### 1_autogen_agentchat.ipynb
A demonstration of the basic use of AutoGen AgentChat . The notebook includes an implementation of a humorous airline assistant that uses tools to retrieve ticket prices from a SQLite database. The agent responds in a humorous way, providing prices for travel to different cities.

# 2_autogen_agentchat.ipynb
Second notebook with AgentChat examples:
1. multi-modal conversations
The notebook contains examples of multi-modal conversational implementations that allow agents to process different types of data - text, images and other media
2 Structured Outputs
The second part of the notebook demonstrates how to configure agents to generate structured responses
3 Using LangChain tools
The notebook demonstrates integration with the LangChain ecosystem, which greatly extends the capabilities of the agents . LangChain offers a rich set of tools for working with language models and allows easy integration with external APIs and databases.
4 Team systems (Teams)
The final section focuses on creating teams of agents that can work together to solve complex problems

# 3_autogen_core.ipynb
Advanced examples of the use of autogen-core . The notebook demonstrates:
Creation of simple agents with custom message handlers
Implementation of LLM agents with delegation to AssistantAgent
A "rock, paper, scissors" game system with three cooperating agents
Use of different models (OpenAI GPT-4o-mini, Ollama llama3.2)

### 4_autogen_distributed.ipynb
This notebook presents the key concepts of a distributed architecture, where agents can run in different processes and communicate using the gRPC protocol.
- GrpcWorkerAgentRuntimeHost - a central host that manages communication between different runtimes
- GrpcWorkerAgentRuntime - worker runtimes acting as clients connected to the host
- Agents - Player1Agent, Player2Agent and Judge - each running in a separate process

Definition of agents
Each agent is implemented as a class inheriting from RoutedAgent:
- Player1Agent - research agent responsible for finding arguments 'for' the use of AutoGen
- Player2Agent - research agent responsible for finding arguments 'against' the use of AutoGen
- Judge - coordinating agent who sends queries to both Players and makes the final decision

### 5_Multiagent_project - Multi-agent project
Agent.py - Template for the underlying business agent. The Agent class implements:
Business idea generation system
Random interaction with other agents (30% chance of consulting an idea)
Use of GPT-4o-mini

creator.py - Agent creator that dynamically generates new agents. Main functionalities:
Reading the agent.py template
Generation of new agent code using LLM
Automatic registration of a new agent in the runtime
Testing the created agent by sending messages

messages.py - Message handling module between agents . Includes:
Message class for communication
The find_recipient function for randomly selecting a message recipient

world.py - The main file that runs the world of agents. Implements:
Runtime configuration for agents
Agent registration Creator
Main loop to continuously generate new agents

