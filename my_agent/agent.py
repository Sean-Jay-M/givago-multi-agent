from google.adk.agents import SequentialAgent, ParallelAgent
from .retriever.agent import retriever_agent
from .fact_checker_1.agent import fact_checker_agent
from .fact_checker_2.agent import fact_checker_agent_2
from .Summariser.agent import summariser_agent

# Parallel Agent - Runs both fact checkers simultaneously
# Each fact checker stores its output with a unique key:
# - fact_checker_agent -> 'fact_check_result'
# - fact_checker_agent_2 -> 'fact_check_result_2'
parallel_fact_checkers = ParallelAgent(
    name='parallel_fact_checkers',
    description='Runs multiple fact-checking agents in parallel for comprehensive verification.',
    sub_agents=[fact_checker_agent, fact_checker_agent_2],
)

# Root Agent - Sequential workflow:
# 1. retriever_agent: Gathers initial information (stores in 'retriever_result')
# 2. parallel_fact_checkers: Runs both fact checkers in parallel
#    - fact_checker_agent stores output in 'fact_check_result'
#    - fact_checker_agent_2 stores output in 'fact_check_result_2'
# 3. summariser_agent: Combines all results into a final report
root_agent = SequentialAgent(
    name='fact_check_pipeline',
    description='A comprehensive fact-checking pipeline that retrieves information, verifies claims using parallel fact-checkers, and summarizes the results.',
    sub_agents=[retriever_agent, parallel_fact_checkers, summariser_agent],
)
