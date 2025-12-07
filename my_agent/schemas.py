from pydantic import BaseModel, Field

# Input schema used by both agents
class FactCheckerFormat(BaseModel):
    modelConfidence: str = Field(description="The confidence level of the facts provided. (Low,Medium,High)")
    statementConfidence: str = Field(description="The confidence level for the given fact to evaluate. (Low,Medium,High)")
    reasoning: str = Field(description="The reasoning for the confidence level given backed up with facts.")