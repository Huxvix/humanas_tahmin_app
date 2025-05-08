from datetime import datetime

def parse_iso(ts: str) -> datetime:
    """Parse an ISO-8601 timestamp (with or without fractional seconds)."""
    # strip Z if present, then fromisoformat
    if ts.endswith('Z'):
        ts = ts[:-1]
    return datetime.fromisoformat(ts)