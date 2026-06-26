from app.tools.mf_api import search_funds, get_nav_history
from app.tools.calculators import calculate_returns


class FundNotFound(Exception):
    pass


def get_fund_data(query: str):
    """
    Search a fund, fetch NAV history, calculate returns,
    and return a structured response.
    """

    results = search_funds(query)

    if not results:
        raise FundNotFound(f"Fund '{query}' not found.")

    # Best matching fund
    fund = results[0]

    # MFAPI search response keys
    scheme_code = str(fund.get("schemeCode"))
    scheme_name = fund.get("schemeName")

    # Fetch NAV history
    nav_payload = get_nav_history(scheme_code)

    nav_data = nav_payload.get("data", [])
    meta = nav_payload.get("meta", {})

    # Calculate returns
    metrics = calculate_returns(nav_data)

    return {
        "scheme_code": scheme_code,
        "scheme_name": scheme_name,
        "fund_house": meta.get("fund_house", ""),
        "metrics": metrics,
        "nav_data": nav_data,
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

    return {
        "fund_1": {
            "scheme_code": first["scheme_code"],
            "scheme_name": first["scheme_name"],
            "fund_house": first["fund_house"],
            "metrics": first["metrics"],
        },
        "fund_2": {
            "scheme_code": second["scheme_code"],
            "scheme_name": second["scheme_name"],
            "fund_house": second["fund_house"],
            "metrics": second["metrics"],
        },
        "summary": summary,
    }