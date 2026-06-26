import requests
from app.config import MF_API_BASE_URL, MF_SEARCH_URL
from app.core.exceptions import MFAPIError

def search_funds(query: str):
    try:
        url = f"{MF_SEARCH_URL}?q={query}"
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        if not isinstance(data, list):
            raise MFAPIError("Unexpected MF search response format")
        return data
    except requests.RequestException as e:
        raise MFAPIError(f"MFAPI search failed: {str(e)}") from e

def get_nav_history(scheme_code: str):
    try:
        url = f"{MF_API_BASE_URL}/{scheme_code}"
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        if not isinstance(data, dict):
            raise MFAPIError("Unexpected NAV response format")
        return data
    except requests.RequestException as e:
        raise MFAPIError(f"MFAPI NAV fetch failed: {str(e)}") from e
