from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="general_faq_checker",
    model="gemini-2.5-flash",
    description=(
        "Agent to fetch details from Google Search engine"
    ),
    instruction=(
        "You a research based fact checker for any information being sent to it"
    ),
    tools=[google_search]
)
