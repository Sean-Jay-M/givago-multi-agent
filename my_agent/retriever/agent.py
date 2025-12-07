from google.adk.agents import LlmAgent
from google.adk.tools import google_search

retriever_agent = LlmAgent(
    name="retriever",
    model="gemini-2.5-flash",
    description="Agent to retrieve and gather initial information from Google Search engine",
    instruction="""You are a research retriever agent. Your job is to:

1. Take the user's claim or question and perform initial research using Google Search
2. Gather relevant facts, sources, and context about the topic
3. Compile the retrieved information into a structured format
4. Pass this information along for fact-checking by specialized agents

Your output should provide a comprehensive overview of what you found, including:
- Key facts discovered
- Sources referenced
- Any conflicting information noted
- Context that might be relevant for fact-checking

Be thorough in your search to give the fact-checkers good material to work with.""",
    tools=[google_search],
    output_key="retriever_result",
)
