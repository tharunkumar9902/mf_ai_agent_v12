from typing import Dict, List
from app.core.exceptions import FundNotFoundError
from app.tools.mf_api import search_funds, get_nav_history
from app.tools.calculators import calculate_returns

def _score_result(query: str, scheme_name: str) -> int:
    q = query.lower().strip()
    s = scheme_name.lower().strip()
    score = 0
    if q == s:
        score += 100
    if q in s:
        score += 50
    for token in q.split():
        if token in s:
            score += 5
    return score

def resolve_fund(query: str) -> Dict:
    results = search_funds(query)
    if not results:
        raise FundNotFoundError(f"No fund found for query: {query}")
    ranked = sorted(
        results,
        key=lambda x: _score_result(query, x.get("schemeName", "")),
        reverse=True
    )
    best = ranked[0]
    return {
        "scheme_code": str(best.get("schemeCode")),
        "scheme_name": best.get("schemeName"),
        "candidates": ranked[:5]
    }

def get_fund_detail(query: str) -> Dict:
    resolved = resolve_fund(query)
    scheme_code = resolved["scheme_code"]
    scheme_name = resolved["scheme_name"]
    nav_payload = get_nav_history(scheme_code)
    nav_data = nav_payload.get("data", [])
    meta = nav_payload.get("meta", {})
    metrics = calculate_returns(nav_data)
    return {
        "scheme_code": scheme_code,
        "scheme_name": scheme_name,
        "fund_house": meta.get("fund_house"),
        "metrics": metrics,
        "nav_data": nav_data,
        "candidates": resolved.get("candidates", [])
    }
