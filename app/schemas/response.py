from typing import Any, List, Optional
from pydantic import BaseModel

class ChatResponse(BaseModel):
    answer: str

class HistoryItem(BaseModel):
    query: str
    agent_response: str
    created_at: Any

class HistoryResponse(BaseModel):
    items: List[HistoryItem]

class FundMetrics(BaseModel):
    latest_nav: Optional[float] = None
    total_return_percent: Optional[float] = None
    one_month_return_percent: Optional[float] = None
    six_month_return_percent: Optional[float] = None
    one_year_return_percent: Optional[float] = None
    three_year_return_percent: Optional[float] = None
    cagr_3y_percent: Optional[float] = None

class FundSummary(BaseModel):
    scheme_code: str
    scheme_name: str
    fund_house: Optional[str] = None
    metrics: FundMetrics

class CompareResponse(BaseModel):
    fund_1: FundSummary
    fund_2: FundSummary
    summary: str
