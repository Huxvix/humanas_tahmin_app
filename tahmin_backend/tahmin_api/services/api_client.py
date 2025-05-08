import requests
from requests.exceptions import RequestException

API_URL = "https://case-test-api.humanas.io"

def fetch_login_rows() -> list[dict]:
    try:
        resp = requests.get(API_URL)
        resp.raise_for_status()
        payload = resp.json()
        if payload.get("status") != 0 or payload.get("message") != "Success":
            raise ValueError("Hatalı API yanıtı")
        return payload["data"]["rows"]
    except RequestException as e:
        raise RuntimeError(f"Data alınırken hata oluştu: {e}") from e