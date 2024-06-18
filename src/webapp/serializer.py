# Convert Complex Data Into Python Data Types, To Then Render Into JSON on The React Client Side
from rest_framework import serializers
from . models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = [ 'test1', 'test2'] 