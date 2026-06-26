from fastapi import APIRouter, HTTPException

from app.services.fund_service import (
    get_fund_detail,
    resolve_fund
)

from app.core.exceptions import (
    FundNotFoundError,
    MFAPIError
)

router = APIRouter(prefix="/fund", tags=["Funds"])


@router.get("/search/{query}")
def search_fund(query: str):
    """
    Returns the top matching mutual funds.
    """

    try:

        result = resolve_fund(query)

        return result["candidates"]

    except FundNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

    except MFAPIError as e:
        raise HTTPException(status_code=502, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{query}")
def fund_detail(query: str):

    try:

        return get_fund_detail(query)

    except FundNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

    except MFAPIError as e:
        raise HTTPException(status_code=502, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))