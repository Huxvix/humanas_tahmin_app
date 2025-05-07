from datetime import datetime, timedelta
from statistics import mean
from django.http import JsonResponse
from django.views import View
import requests

class LoginPredictionMixin:
    """Provides two next-login prediction algorithms."""

    @staticmethod
    def parse_iso(ts: str) -> datetime.date:
        # Accepts '2025-04-01T04:47:00Z'
        return datetime.fromisoformat(ts)
    

    def predict_next_mean_interval(self, logins: list[str]) -> datetime.date:
        """Algorithm 1: Add the average inter-login interval to last login."""
        times = [self.parse_iso(ts) for ts in logins]
        intervals = [(t2 - t1).total_seconds()
                     for t1, t2 in zip(times, times[1:])]
        avg_interval = mean(intervals) if intervals else 0
        return times[-1] + timedelta(seconds=avg_interval)

    def predict_next_exponential_smoothing(
        self,
        logins: list[str],
        alpha: float = 0.5
    ) -> datetime.date:
        """Algorithm 2: EWMA of intervals, then project forward."""
        times = [self.parse_iso(ts) for ts in logins]
        intervals = [(t2 - t1).total_seconds()
                     for t1, t2 in zip(times, times[1:])]
        s = intervals[0] if intervals else 0
        for interval in intervals[1:]:
            s = alpha * interval + (1 - alpha) * s
        return times[-1] + timedelta(seconds=s)

class LoginPredictionView(LoginPredictionMixin, View):
    """
    A class to fetch and analyze user login data and predict future logins
    using two different algorithms:
    1. Recent Frequency Algorithm - Based on recent login frequency
    2. Time Pattern Algorithm - Based on common login time patterns
    """
    
    def get(self, request, *args, **kwargs):
        
        data = self.get_login_data(request, *args, **kwargs)
        results = []
        
        for user in data:
            logins = user.get("logins", [])
            if not logins:
                continue
            
            last_login = datetime.fromisoformat(logins[-1]).strftime("%d.%m.%Y %H:%M:%S")
            pred_mean = datetime.fromisoformat(str(self.predict_next_mean_interval(logins))).strftime("%d.%m.%Y %H:%M:%S")
            pred_exsm = datetime.fromisoformat(str(self.predict_next_exponential_smoothing(logins))).strftime("%d.%m.%Y %H:%M:%S")
            
            results.append({
                "user_id": self.only_numerics(user["id"]),
                "user_name": user["name"],
                "last_login": last_login,
                "predicted_next_mean": pred_mean,
                "predicted_next_exsm": pred_exsm
            })
        
        return JsonResponse(results, safe=False, status=200)
        
    def only_numerics(self , s: str) -> str:
        # Remove non-numeric characters from a string.
        return ''.join(filter(str.isdigit, s))
    
    def get_login_data(self, request, *args, **kwargs):
        """Fetch and process login data from API"""
        try:
            api_url = "https://case-test-api.humanas.io"
            
            response = requests.get(f"{api_url}")
            response.raise_for_status()
            
            data = response.json()["data"]["rows"]
            return data

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from API: {e}")
            return None


