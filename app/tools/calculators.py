from datetime import datetime
from math import pow
from typing import Dict, List, Optional


def parse_nav_data(nav_data):
    parsed = []

    for item in nav_data:
        try:
            if isinstance(item, dict):
                date = item["date"]
                nav = item["nav"]
            else:
                date = item.date
                nav = item.nav

            parsed.append({
                "date": datetime.strptime(date, "%d-%m-%Y"),
                "nav": float(nav)
            })
        except Exception as e:
            print("Skipping NAV:", item, e)

    parsed.sort(key=lambda x: x["date"])
    return parsed


def calculate_absolute_return(start_nav: float, end_nav: float) -> float:
    if start_nav <= 0:
        return 0.0
    return round(((end_nav - start_nav) / start_nav) * 100, 2)


def calculate_cagr(start_nav: float, end_nav: float, years: float) -> Optional[float]:
    if start_nav <= 0 or years <= 0:
        return None
    return round((pow(end_nav / start_nav, 1 / years) - 1) * 100, 2)


def find_closest_nav(parsed_data: List[Dict], days_back: int) -> Optional[float]:
    if not parsed_data:
        return None

    latest_date = parsed_data[-1]["date"]
    target_ts = latest_date.timestamp() - (days_back * 86400)

    closest = None
    min_diff = float("inf")

    for item in parsed_data:
        diff = abs(item["date"].timestamp() - target_ts)

        if diff < min_diff:
            min_diff = diff
            closest = item["nav"]

    return closest


def calculate_returns(nav_data) -> Dict:
    parsed = parse_nav_data(nav_data)

    if len(parsed) < 2:
        return {"error": "Not enough NAV data"}

    latest_nav = parsed[-1]["nav"]
    oldest_nav = parsed[0]["nav"]

    result = {
        "latest_nav": latest_nav,
        "total_return_percent": calculate_absolute_return(oldest_nav, latest_nav),
    }

    one_month_nav = find_closest_nav(parsed, 30)
    six_month_nav = find_closest_nav(parsed, 180)
    one_year_nav = find_closest_nav(parsed, 365)
    three_year_nav = find_closest_nav(parsed, 365 * 3)

    if one_month_nav is not None:
        result["one_month_return_percent"] = calculate_absolute_return(one_month_nav, latest_nav)

    if six_month_nav is not None:
        result["six_month_return_percent"] = calculate_absolute_return(six_month_nav, latest_nav)

    if one_year_nav is not None:
        result["one_year_return_percent"] = calculate_absolute_return(one_year_nav, latest_nav)

    if three_year_nav is not None:
        result["three_year_return_percent"] = calculate_absolute_return(three_year_nav, latest_nav)
        result["cagr_3y_percent"] = calculate_cagr(three_year_nav, latest_nav, 3)

    return result