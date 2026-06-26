from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.request import ChatRequest, CompareRequest
from app.schemas.response import ChatResponse, CompareResponse, HistoryResponse, HistoryItem, FundSummary
from app.services.agent_service import run_agent
from app.services.compare_service import compare_two_funds
from app.tools.db_tools import save_chat, fetch_history
from app.core.exceptions import FundNotFoundError, MFAPIError

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, db: Session = Depends(get_db)):
    try:
        answer = await run_agent(request.message)
        save_chat(db, request.user_id, request.message, answer)
        return ChatResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/compare", response_model=CompareResponse)
def compare(request: CompareRequest):
    try:
        result = compare_two_funds(request.fund_1, request.fund_2)
        return CompareResponse(**result)
    except FundNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except MFAPIError as e:
        raise HTTPException(status_code=502, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history/{user_id}", response_model=HistoryResponse)
def history(user_id: str, db: Session = Depends(get_db)):
    records = fetch_history(db, user_id)
    items = [HistoryItem(query=r.query, agent_response=r.agent_response, created_at=r.created_at) for r in records]
    return HistoryResponse(items=items)
