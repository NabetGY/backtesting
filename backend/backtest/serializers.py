from rest_framework.serializers import ModelSerializer

from backtest.models import BackTest

class BacktestSerializer( ModelSerializer ):
    class Meta:
        model = BackTest
        fields = '__all__'