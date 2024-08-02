from django.db import models
from userbiography.model import UserBio

'''
Relationships: Linked to UserBio through a foreign key,
so each ticker is associated with a specific user

Relevant Sources: https://docs.djangoproject.com/en/5.0/topics/db/models/#automatic-primary-key-fields
'''
class Ticker(models.Model):
    user = models.ForeignKey(UserBio, on_delete=models.CASCADE) # Foreign key to UserBio, to link each unique user
    symbol = models.CharField(max_length=4, unique=True) # Prevent users from storing duplicate tickers
    last = models.DecimalField(decimal_places=2)
    open = models.DecimalField(decimal_places=2)
    high = models.DecimalField(decimal_places=2)
    low = models.DecimalField(decimal_places=2)
    change_percent = models.DecimalField(decimal_places=2)
    volume = models.DecimalField(decimal_places=1)
    
    def __str__(self) -> str:
        return self.symbol