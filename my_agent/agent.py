from google.adk.agents.llm_agent import Agent
from .fact_checker_1.agent import fact_checker_agent

# Root Agent
root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant that can verify facts and answer user questions.',
    instruction="""You are a helpful assistant that answers user questions.

When a user presents a factual claim or statement that should be verified, delegate it to the fact_checker agent for verification. The fact checker will research the claim using web and academic resources and provide a factuality assessment.

For general questions and non-factual requests, respond directly based on your knowledge.

When delegating to the fact checker, simply pass the claim or statement that needs verification.""",
    sub_agents=[fact_checker_agent],  # Root agent can delegate to fact checker
)
