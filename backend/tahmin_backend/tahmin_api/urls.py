from django.urls import path
from .views import LoginPredictionView

urlpatterns = [
    path('data/', LoginPredictionView.as_view(), name='api_data'),
]