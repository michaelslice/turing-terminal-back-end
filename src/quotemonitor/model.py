from django.db import models
from userbiography.model import UserAccount

'''
Relationships: Linked to UserAccount through a foreign key,
so each ticker is associated with a specific user

@Type: Foreign key to UserAccount

@Relevant Sources: https://docs.djangoproject.com/en/5.0/topics/db/models/#automatic-primary-key-fields
'''
class Ticker(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE) # Foreign key to UserAccount, to link each unique user
    symbol = models.CharField(max_length=4, null=False)
    last = models.DecimalField(max_digits=10, decimal_places=2) 
    open = models.DecimalField(max_digits=10, decimal_places=2) 
    high = models.DecimalField(max_digits=10, decimal_places=2) 
    low = models.DecimalField(max_digits=10, decimal_places=2) 
    change_percent = models.DecimalField(max_digits=10, decimal_places=2) 
    volume = models.DecimalField(max_digits=20, decimal_places=1) 
    
    def __str__(self) -> str:
        return self.symbol
