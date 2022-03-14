import datetime
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


from backtest.models import BackTest

class BacktestSerializer( ModelSerializer ):
    class Meta:
        model = BackTest
        fields = '__all__'


class TimestampField(serializers.Field):
    def to_native(self, value):
        epoch = datetime.datetime(1970,1,1)
        return int((value - epoch).total_seconds())