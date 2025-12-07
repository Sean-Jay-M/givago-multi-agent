from typing import List
from pydantic import BaseModel, Field

# 1. The output of a single Checker Agent
class FactCheckerFormat(BaseModel):
    agent_name: str = Field(description="Name of the agent performing the check.")
    modelConfidence: str = Field(description="Confidence level (Low, Medium, High).")
    statementConfidence: str = Field(description="Confidence in the specific statement.")
    reasoning: str = Field(description="Detailed reasoning backed up with facts.")

# 2. The input for the Summariser (The Container)
class SummariserInput(BaseModel):
    reports: List[FactCheckerFormat] = Field(
        description="A list containing the analysis reports from all three fact-checker agents."
    )