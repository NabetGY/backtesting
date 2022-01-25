from rest_framework.serializers import ModelSerializer

from ticker.models import Ticker, TimeSeries

class TickerSerializer( ModelSerializer ):
    
    class Meta:
        model = Ticker
        fields = '__all__'


class TimeSeriesSerializer( ModelSerializer ):
    
    class Meta:
        model = TimeSeries
        fields = '__all__'