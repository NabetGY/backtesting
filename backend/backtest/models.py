from django.db import models

from core import settings

class BackTest( models.Model ):

    operations = models.IntegerField("Numero de operaciones")
    win_rate = models.DecimalField("Win rate", max_digits=3, decimal_places=2 )
    total_profit_loss = models.DecimalField("Total Profit/Loss", max_digits=10, decimal_places=2 )
    profit_loss = models.DecimalField("Profit/Loss", max_digits=3, decimal_places=2 )
    max_profit = models.DecimalField("Max Profit", max_digits=10, decimal_places=2 )
    max_loss = models.DecimalField("Max Loss", max_digits=10, decimal_places=2 )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete = models.CASCADE
    )
    
    



