from rest_framework import serializers
from .models import StockList

'''
@class StockListSerializer: Represents a serializer class that 
inherits from "serializers.ModelSerializer", which is a shortcut
that automatically creates a serializer class with fields that
correspond to the model fields

@class Meta: Is a nested class that represents metadeta for the 
serializer regarding which model it should use and what fields
should be included in the serialization

@note This class handles the conversion for StockList to be converted
into JSON, and will onyl include the specified fields 

'''
class StockListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockList
        # Fields that should be included in the serialized output
        fields = ["ticker", "last", "bid", "ask", "change", "change_percent", "volume" ]
        