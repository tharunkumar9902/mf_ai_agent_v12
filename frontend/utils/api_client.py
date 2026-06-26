import os
import requests

API_BASE = os.getenv("API_BASE_URL", "http://localhost:8000")


def chat(user_id: str, message: str):
    return requests.post(
        f"{API_BASE}/chat",
        json={"user_id": user_id, "message": message},
        timeout=60
    ).json()


def compare(fund_1: str, fund_2: str):
    return requests.post(
        f"{API_BASE}/compare",
        json={"fund_1": fund_1, "fund_2": fund_2},
        timeout=60
    ).json()


def fund_lookup(query: str):
    return requests.get(
        f"{API_BASE}/fund/{query}",
        timeout=60
    ).json()


# ⭐ NEW
def search_funds(query: str):
    return requests.get(
        f"{API_BASE}/fund/search/{query}",
        timeout=60
    ).json()


def history(user_id: str):
    return requests.get(
        f"{API_BASE}/history/{user_id}",
        timeout=60
    ).json()


def report_compare(fund_1: str, fund_2: str):
    return requests.post(
        f"{API_BASE}/report/compare",
        json={"fund_1": fund_1, "fund_2": fund_2},
        timeout=60
    ).json()