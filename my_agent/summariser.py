from google.adk.agents import LlmAgent

#Import Schemas
from .schemas import FactCheckerFormat

summariser = LlmAgent(
    model="gemini-2.5-flash",
    name='summariser',
    description='A simple summariser agent',
    instruction="""You are an agent that will receive the results of multiple evaluation agents your job is to compile them all together into a cohesive report making sure to keep relevant details and to summarise."
    """,
    input_schema=FactCheckerFormat,

)