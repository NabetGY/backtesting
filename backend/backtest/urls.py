from django.urls import path

from backtest.views import BackTestAPIView

urlpatterns = [
    path('', BackTestAPIView.as_view(), name='backtest')
]