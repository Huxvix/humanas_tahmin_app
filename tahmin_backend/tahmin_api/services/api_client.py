import requests
from requests.exceptions import RequestException

API_URL = "https://case-test-api.humanas.io"

def fetch_login_rows() -> list[dict]:
    """Call external API and return its 'rows' list, or raise."""
    try:
        resp = requests.get(API_URL)
        resp.raise_for_status()
        payload = resp.json()
        if payload.get("status") != 0 or payload.get("message") != "Success":
            raise ValueError("Bad payload status")
        return payload["data"]["rows"]
    except RequestException as e:
        # you might want to log here instead
        raise RuntimeError(f"Error fetching data: {e}") from e