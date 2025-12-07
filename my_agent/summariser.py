from google.adk.agents import LlmAgent

from .schemas import SummariserInput

summariser = LlmAgent(
    model="gemini-2.5-flash",
    name='summariser',
    description='A summariser agent that compiles fact-check results into a final report',
    instruction="""You are a summariser agent. You will receive the output from the fact-checker agent stored in the session state under the key 'fact_check_result'.
    
    Your job is to:
    1. Read the fact-check analysis from the state
    2. Compile the findings into a clear, concise summary report
    3. Highlight the key findings, confidence levels, and any important caveats
    4. Present the information in an easy-to-understand format for the user
    
    Your output should be the final response that the user sees, so make it comprehensive yet accessible.""",
    input_schema=SummariserInput
)