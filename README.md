# AI Agents

## Quick Setup

1. **Install UV package manager** (requires PowerShell):
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

2. **Clone and initialize project**:
git clone https://github.com/DominikZurawski/agents.git
cd agents

3. **Install dependencies**:
uv sync

## Environment Configuration
Create `.env` file with required API credentials:
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
GROQ_API_KEY=groq_cloud_key
