from django.db import models

class Ticker(models.Model):
    symbol = models.CharField(max_length=4)
    last = models.DecimalField(decimal_places=2)
    bid = models.DecimalField(decimal_places=2)
    ask = models.DecimalField(decimal_places=2)
    change_percent = models.DecimalField(decimal_places=2)
    volume = models.DecimalField(decimal_places=1)
    
    def __str__(self):
        return self.symbol