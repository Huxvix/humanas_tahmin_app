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
    """
    mean interval algoritmasındaki bütün loginler arasındaki sürelerin ortalamasını alıyoruz ve son login zamanına bunu ekleyerek tahmin edilen
    sonraki login zamanını elde ediyoruz.
    """
    avg = mean(intervals) # loginler arasındaki ortalama süreyi hesapla
    next_mean = times[-1] + timedelta(seconds=avg) # son login zamanına ortalama süreyi ekle

    # 2) median interval algoritması
    """
    median interval algoritmasında ise, loginler arasındaki sürelerin medyanını yani tam ortadaki değeri alıyoruz.
    mean interval yöntemine göre çok büyük dalgalanmalara karşı daha dayanıklı olan bu yöntemde örneğin kullanıcı her gün girdikten sonra 3 gün boyunca girmezse,
    yine 1 gün sonra girecek gibi bir tahmin yapılır.
    """
    avg = np.median(intervals) # loginler arasındaki ortalama süreyi hesapla
    next_median = times[-1] + timedelta(seconds=avg) # son login zamanına ortalama süreyi ekle

    return {
        "user_id": only_numerics(user["id"]),
        "user_name": user["name"],
        "last_login": times[-1].strftime("%d.%m.%Y %H:%M:%S"),
        "predicted_next_mean": next_mean.strftime("%d.%m.%Y %H:%M:%S"),
        "predicted_next_median": next_median.strftime("%d.%m.%Y %H:%M:%S"),
    }

# sadece sayılardan oluşan bir string döndürür
def only_numerics(s: str) -> str:
    return "".join(filter(str.isdigit, s))