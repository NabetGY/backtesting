from rest_framework.routers import DefaultRouter

from backtest.views import BacktestViewSet

router = DefaultRouter()

router.register( r'', BacktestViewSet)

urlpatterns = router.urls