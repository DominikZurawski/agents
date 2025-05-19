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

## New Features Overview

### Core Modules
- **`app.py`**
  Main application file implementing a Gradio web interface for interacting with AI agents. Features include:
  - PDF processing of LinkedIn profiles (`me/linkedin.pdf`)
  - Push notification integration via Pushover API
  - User interaction tracking system

### Evaluation Notebooks
- **`evaluate_other_model.ipynb`**
  Implements quality assurance workflows for LLM responses, featuring:
  - Automatic answer validation against predefined criteria
  - Retry mechanisms for failed evaluations
  - Comparative analysis between different model outputs

- **`orchestration_and_evaluate_models.ipynb`**
  Demonstrates hybrid AI workflows combining:
  - Local model execution via Ollama (Llama3.2)
  - Cloud-based model comparisons (OpenAI/Anthropic)
  - Performance benchmarking metrics

### Tool Integrations
- **`tools_and_push_notification.ipynb`**
  Step-by-step guide for configuring real-time alerts:
  - Pushover service setup
  - API key management
  - Notification routing logic

### Configuration
- **`openAI.ipynb`**
  Environment setup notebook for:
  - OpenAI API key validation
  - Basic chat completion patterns
  - Error handling best practices

## Data Assets
- **`me/` Directory**
  Contains sample inputs for testing:
  - `linkedin.pdf`: Example LinkedIn profile PDF
  - `summary.txt`: Structured personal profile template

---

**Usage Note**: Requires API keys for OpenAI, Anthropic, and Pushover in `.env` file. See individual notebooks for implementation details.
