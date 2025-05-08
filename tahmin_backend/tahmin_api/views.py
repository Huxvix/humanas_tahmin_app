from django.views import View
from django.http import JsonResponse
from tahmin_api.services.api_client import fetch_login_rows
from tahmin_api.services.prediction_service import predict_for_user
from rest_framework.exceptions import ValidationError

class LoginPredictionView(View):
    def get(self, request, *args, **kwargs):
        try:
            rows = fetch_login_rows()
        except Exception as e:
            return JsonResponse(
                {"error": str(e)},
                status=502
            )

        # her kullanıcı için algoritmaları çalıştır
        results = [predict_for_user(u) for u in rows]

        return JsonResponse(results, safe=False, status=200)
