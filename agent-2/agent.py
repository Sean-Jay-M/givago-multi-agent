from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    name="general_faq_checker",
    model="gemini-2.5-flash",
    # model=LiteLlm(model="openai/gpt-4o"),
    description=(
        "Agent to fact check in"
    ),
    instruction=(
        "You a research based fact checker for any information being sent to it"
    ),
    tools=[google_search]
)