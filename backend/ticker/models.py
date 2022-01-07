from django.db import models

class Ticker(models.Model):

    name = models.CharField( "Nombre", max_length=255)
    symbol = models.CharField( "Simbolo", max_length=20)

    def __str__(self):
        return self.name


class TimeSeries(models.Model):

    ticker = models.ForeignKey( Ticker, on_delete=models.CASCADE, null=False, blank=False)
    interval = models.CharField(max_length=10)
    last_Refreshed = models.DateTimeField()
    time_series = models.JSONField()