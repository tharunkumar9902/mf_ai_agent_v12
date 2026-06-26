from app.tools.mf_api import search_funds, get_nav_history
from app.tools.calculators import calculate_returns
from app.services.ollama_service import ask_ollama


class FundNotFound(Exception):
    pass


def get_fund_data(query: str):
    """
    Search a mutual fund, fetch NAV history and calculate returns.
    """

    results = search_funds(query)

    if not results:
        raise FundNotFound(f"Fund '{query}' not found.")

    fund = results[0]

    scheme_code = str(fund.get("schemeCode"))
    scheme_name = fund.get("schemeName")

    nav_payload = get_nav_history(scheme_code)

    nav_data = nav_payload.get("data", [])
    meta = nav_payload.get("meta", {})

    metrics = calculate_returns(nav_data)

    return {
        "scheme_code": scheme_code,
        "scheme_name": scheme_name,
        "fund_house": meta.get("fund_house"),
        "metrics": metrics,
    }


def compare_two_funds(fund1: str, fund2: str):

    first = get_fund_data(fund1)
    second = get_fund_data(fund2)

    first_return = first["metrics"].get("one_year_return_percent", 0)
    second_return = second["metrics"].get("one_year_return_percent", 0)

    if first_return > second_return:
        winner = first["scheme_name"]
    elif second_return > first_return:
        winner = second["scheme_name"]
    else:
        winner = "Both funds performed equally"

    difference = round(abs(first_return - second_return), 2)

    summary = (
        f"{winner} performed better over the last one year "
        f"with a difference of {difference}%."
    )

    prompt = f"""
You are an experienced Mutual Fund Investment Advisor.

Fund 1
Name: {first["scheme_name"]}
Fund House: {first["fund_house"]}
Metrics: {first["metrics"]}

Fund 2
Name: {second["scheme_name"]}
Fund House: {second["fund_house"]}
Metrics: {second["metrics"]}

Explain:

1. Which fund is better?
2. Why?
3. Risk level.
4. Long-term recommendation.
5. Explain in simple English.

Keep the answer under 150 words.
"""

    ai_analysis = ask_ollama(prompt)

    return {
        "fund_1": first,
        "fund_2": second,
        "summary": summary,
        "ai_analysis": ai_analysis,
    }