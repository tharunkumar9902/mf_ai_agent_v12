from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    user_id: str = Field(..., description="User identifier")
    message: str = Field(..., description="User prompt to the agent")

class CompareRequest(BaseModel):
    fund_1: str
    fund_2: str
