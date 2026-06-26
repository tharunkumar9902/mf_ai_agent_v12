from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.schemas.request import CompareRequest
from app.services.report_service import build_compare_report_files
from app.core.exceptions import FundNotFoundError, MFAPIError

router = APIRouter(prefix="/report")

@router.post("/compare")
def report_compare(request: CompareRequest):
    try:
        files = build_compare_report_files(request.fund_1, request.fund_2)
        return files
    except FundNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except MFAPIError as e:
        raise HTTPException(status_code=502, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
