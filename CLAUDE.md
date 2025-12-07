# Givago Multi-Agent System - Documentation

## Overview

This project implements a multi-agent system using the Google Agentic ADK (Agent Development Kit). The system features a hierarchical agent architecture where a root agent can delegate specialized tasks to sub-agents.

## Architecture

### Agent Hierarchy

```
Root Agent (root_agent)
    └── Model 1: Fact Checker (fact_checker_agent)
```

## Agents

### Root Agent

**Name:** `root_agent`

**Model:** `gemini-2.5-flash`

**Purpose:** Primary interface for user interactions. Handles general questions and delegates fact-checking requests to specialized sub-agents.

**Capabilities:**
- Answers general user questions
- Identifies when claims need fact-checking
- Delegates verification tasks to the fact-checker agent
- Aggregates and presents results from sub-agents

**Behavior:**
- When a user presents a factual claim, the root agent automatically delegates it to the fact-checker agent
- For non-factual queries, responds directly using its knowledge base

---

### Model 1: Fact-Checking Agent

**Name:** `fact_checker_agent`

**Model:** `gemini-2.5-flash`

**Purpose:** Specialized agent for verifying factual claims using web and academic resources.

**Tools:**
- `google_search` - Enables web search for finding reliable sources

**Key Features:**

1. **Liberal Language Interpretation**
   - Gives users the benefit of the doubt with language use
   - Accounts for colloquialisms, imprecisions, and reasonable interpretations
   - Considers context and nuance in claims

2. **Multi-Source Verification**
   - Searches web resources for current information
   - Looks for academic and scholarly sources when available
   - Cross-references multiple reputable sources

3. **Structured Output**
   - Provides clear claim restatement
   - Detailed analysis with evidence
   - Factuality rating (LOW/MEDIUM/HIGH)

**Factuality Rating Scale:**

- **HIGH**: The claim is substantially supported by reliable sources
  - Strong evidence from multiple reputable sources
  - Minimal contradictory information
  - Well-established facts

- **MEDIUM**: The claim is partially true, needs context, or evidence is mixed
  - Some supporting evidence but with important caveats
  - Claim requires additional context to be accurate
  - Mixed evidence from different sources
  - Evolving information where consensus is unclear

- **LOW**: The claim is mostly false or misleading
  - Contradicted by reliable sources
  - Based on misinformation or outdated information
  - Lacks credible supporting evidence

**Response Format:**

```
**Claim:** [Restatement of the claim being verified]

**Analysis:** [Detailed analysis including:
- Evidence found from sources
- Context and nuance
- Any important qualifications or caveats
- Citations to sources]

**Factuality Rating:** [LOW/MEDIUM/HIGH]
[Brief explanation of the rating]
```

## Usage Examples

### Example 1: Fact-Checking a Claim

**User Input:**
```
"The Eiffel Tower is the tallest building in Paris"
```

**Agent Flow:**
1. Root agent receives the claim
2. Root agent identifies this as a factual claim needing verification
3. Root agent delegates to fact_checker_agent
4. Fact checker searches for information about Paris buildings and the Eiffel Tower
5. Fact checker returns structured response with rating
6. Root agent presents the results to the user

**Expected Output:**
```
**Claim:** The Eiffel Tower is the tallest building in Paris

**Analysis:** The Eiffel Tower stands at 330 meters (1,083 feet) tall and was
the tallest structure in Paris for many years. However, as of 2011, Tour
Montparnasse (a skyscraper) at 210 meters is the tallest building, and there
are other structures taller than the Eiffel Tower. The user likely meant
"tallest structure" or "most famous tall structure," and the Eiffel Tower is
indeed the most iconic tall structure in Paris.

**Factuality Rating:** MEDIUM
The claim is partially true - the Eiffel Tower is among the tallest structures
in Paris and was historically the tallest, though technically other buildings
have surpassed it.
```

### Example 2: General Question (Not Fact-Checking)

**User Input:**
```
"How do I use this multi-agent system?"
```

**Agent Flow:**
1. Root agent receives the question
2. Root agent identifies this as a general question, not a fact-checking request
3. Root agent responds directly without delegation

## Installation & Setup

### Prerequisites

- Python 3.8+
- Google API Key (for Gemini models)

### Environment Variables

Create a `.env` file in the `my_agent` directory:

```env
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=your_api_key_here
```

### Installation

```bash
# Install Google ADK
pip install google-adk

# Install dependencies
pip install python-dotenv
```

### Running the Agent

```python
from my_agent.agent import root_agent

# The root agent will automatically handle delegation to sub-agents
response = root_agent.run("Your query here")
```

## File Structure

```
givago-multi-agent/
├── my_agent/
│   ├── __init__.py          # Package initialization
│   ├── agent.py             # Root agent definition
│   ├── .env                 # Environment variables
│   └── fact_checker_1/
│       ├── __init__.py      # Package initialization
│       └── agent.py         # Fact-checker agent (Model 1)
├── CLAUDE.md                # This documentation file
└── README.md                # Project README
```

## Design Principles

### 1. Specialization
Each agent has a specific role and expertise. The fact-checker focuses solely on verification, allowing it to be highly optimized for that task.

### 2. Delegation Pattern
The root agent acts as an orchestrator, intelligently routing requests to specialized sub-agents rather than trying to handle everything itself.

### 3. Liberal Interpretation
The fact-checker is designed to be charitable in interpretation, acknowledging that users may not use perfectly precise language while still providing accurate verification.

### 4. Transparency
All fact-checking responses include sources, reasoning, and clear rating scales so users understand the basis for assessments.

### 5. Structured Output
Consistent response formatting makes it easy to parse and understand fact-checking results.

## Extending the System

### Adding New Sub-Agents

To add a new specialized agent:

1. Create a new subdirectory for the agent within `my_agent/`:
```bash
mkdir my_agent/new_agent_name
```

2. Create the agent module structure:
```
my_agent/new_agent_name/
├── __init__.py
└── agent.py
```

3. Define the agent in `my_agent/new_agent_name/agent.py`:
```python
from google.adk.agents.llm_agent import Agent

new_specialist_agent = Agent(
    model='gemini-2.5-flash',
    name='specialist_name',
    description='What this agent does',
    instruction='Detailed instructions for the agent',
    tools=['relevant_tools'],
)
```

4. Import and add it to the root agent's sub_agents in `my_agent/agent.py`:
```python
from google.adk.agents.llm_agent import Agent
from .fact_checker_1.agent import fact_checker_agent
from .new_agent_name.agent import new_specialist_agent

root_agent = Agent(
    # ... other config ...
    sub_agents=[fact_checker_agent, new_specialist_agent],
)
```

### Modifying Fact-Checker Behavior

Edit the `instruction` parameter in the `fact_checker_agent` definition in [my_agent/fact_checker_1/agent.py](my_agent/fact_checker_1/agent.py) to adjust:
- How liberally claims are interpreted
- What sources are prioritized
- Rating criteria
- Output format

## Best Practices

1. **Clear Claims**: While the fact-checker is liberal with interpretation, clearer claims yield better results
2. **Specific Questions**: For best results, ask specific factual questions rather than vague statements
3. **Source Awareness**: The fact-checker relies on web search, so very recent events may have limited sources
4. **Context Matters**: Providing context with claims helps the agent make better assessments

## Troubleshooting

### Agent Not Delegating

If the root agent isn't delegating to the fact-checker:
- Ensure the claim is phrased as a factual statement
- Try being more explicit: "Can you fact-check this claim: ..."

### Search Not Working

If the fact-checker can't search:
- Verify your Google API key is set correctly in `.env`
- Ensure `google_search` tool is available in your ADK installation
- Check API quota and usage limits

### Low-Quality Results

If fact-checking results are poor:
- Try rephrasing the claim more clearly
- Provide additional context
- Check if the topic is too recent or obscure for available sources

## Future Enhancements

Potential improvements to consider:

- Add citation formatting options (APA, MLA, Chicago)
- Implement confidence scores beyond LOW/MEDIUM/HIGH
- Add academic database search capabilities
- Create specialized sub-agents for different domains (science, history, etc.)
- Add claim complexity detection to adjust search strategies
- Implement claim decomposition for complex multi-part statements

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
