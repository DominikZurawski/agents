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
- **Jupyter Notebook Tutorials**
  Four foundational guides demonstrating agent orchestration:
  - `intro.ipynb`: SDK fundamentals and execution tracing
  - `EmailAgent.ipynb`: Multi-agent email workflow system
  - `Guardrail.ipynb`: Security validation patterns
  - `Deep Research.ipynb`: Automated research pipeline with structured outputs

## Deep Research Application (`/deep_research`)
```
uv run app.py
```
Modular production-grade system for autonomous research operations:
- **ResearchManager**: Core orchestration
- **PlannerAgent**: Web search strategy formulation
- **WriterAgent**: Report generation with Pydantic validation
- **RateLimiter**: API usage optimization
- **Email_agent**: SendGrid integration for result distribution

Check on HuggingFace: https://huggingface.co/spaces/Domino675/Deep_Research_and_send_email