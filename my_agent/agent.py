from google.adk.agents import SequentialAgent
from .fact_checker_1.agent import fact_checker_agent
from .summariser import summariser

# Root Agent - Sequential workflow: fact_checker -> summariser
# The fact_checker runs first, stores its output in 'fact_check_result',
# then the summariser reads that output and produces the final summary.
root_agent = SequentialAgent(
    name='fact_check_pipeline',
    description='A fact-checking pipeline that verifies claims and summarizes the results.',
    sub_agents=[fact_checker_agent, summariser],
)
