from statistics import mean
from datetime import datetime, timedelta
from tahmin_api.utils.parsing import parse_iso
import numpy as np

def predict_for_user(user: dict) -> dict:

    logins = user.get("logins", []) # kullanıcının logins'ı yoksa boş bir dict döndür, varsa loginlerini al
    if not logins:
        return {}

    # tüm logins'ı datetime nesnelerine çevir
    times = [parse_iso(ts) for ts in logins]
    # iki login arasındaki süreleri hesapla
    intervals = [(t2 - t1).total_seconds()
                 for t1, t2 in zip(times, times[1:])]

    # 1) mean interval algoritması
    avg = mean(intervals) # loginler arasındaki ortalama süreyi hesapla
    next_mean = times[-1] + timedelta(seconds=avg) # son login zamanına ortalama süreyi ekle

    # 2) median interval algoritması
    avg = np.median(intervals) # loginler arasındaki ortalama süreyi hesapla
    next_median = times[-1] + timedelta(seconds=avg) # son login zamanına ortalama süreyi ekle

    return {
        "user_id": only_numerics(user["id"]),
        "user_name": user["name"],
        "last_login": times[-1].strftime("%d.%m.%Y %H:%M:%S"),
        "predicted_next_mean": next_mean.strftime("%d.%m.%Y %H:%M:%S"),
        "predicted_next_median": next_median.strftime("%d.%m.%Y %H:%M:%S"),
    }

def only_numerics(s: str) -> str:
    return "".join(filter(str.isdigit, s))

def predict_next_volatility(intervals, alpha_min=0.1, alpha_max=0.9, window=5):
    if not intervals:
        return 0
    s = intervals[0]
    for i, interval in enumerate(intervals[1:], start=1):
        # 
        recent = intervals[max(0, i-window):i]
        volatility = np.std(recent) if recent else 0
        # Normalize et (örneğin max volatility’yi öngör)
        norm_vol = min(1, volatility / (np.mean(intervals) + 1e-6))
        alpha = alpha_min + (alpha_max - alpha_min) * norm_vol
        s = alpha * interval + (1 - alpha) * s
    return s