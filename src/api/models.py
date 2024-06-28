from django.db import models

# Inherit from models Model to get database models
'''
@class StockList: Is a model class that inherits from models.Model
meaning Django will treat this class as a table in the database
each attribute will be a field in the table   

'''
class StockList(models.Model):
    ticker = models.CharField(max_length=4)
    last = models.IntegerField()
    bid = models.IntegerField()
    ask = models.IntegerField()
    change = models.IntegerField()
    change_percent = models.IntegerField()
    volume = models.IntegerField()

    def __str__(self):
        return self.ticker