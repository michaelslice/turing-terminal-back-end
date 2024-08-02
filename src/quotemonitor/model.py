from django.db import models
from userbiography.model import UserBio

'''


'''
class Ticker(models.Model):
    user = models.ForeignKey(UserBio, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=4)
    last = models.DecimalField(decimal_places=2)
    open = models.DecimalField(decimal_places=2)
    high = models.DecimalField(decimal_places=2)
    low = models.DecimalField(decimal_places=2)
    change_percent = models.DecimalField(decimal_places=2)
    volume = models.DecimalField(decimal_places=1)
    
    def __str__(self) -> str:
        return self.symbol