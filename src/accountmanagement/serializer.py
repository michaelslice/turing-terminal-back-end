from rest_framework import serializers
from userbiography.model import UserAccount

class UserAccountSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField(max_length=50)
    user_name = serializers.CharField(max_length=30)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    company = serializers.CharField(max_length=30)
    
    class Meta:
        model = UserAccount
        fields = '__all__'
