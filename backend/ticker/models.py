from django.db import models
from django.contrib.postgres.fields import JSONField

class Ticker(models.Model):

    symbol = models.CharField( "Ticker", max_length=7)
    last_Refreshed = models.DateTimeField()
    interval = models.CharField(max_length=10)
    time_series = JSONField()