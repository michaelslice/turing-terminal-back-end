from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.http import HttpResponse
from django.http import JsonResponse
from userbiography.model import UserAccount
import requests
import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from userbiography.model import UserAccount
from accountmanagement.serializer import UserAccountSerializer

'''

'''
@api_view(["GET"])
def get_account_info(request):
    if request.method == "GET":

        email = request.GET.get("userEmail")

        data = UserAccount.objects.all().filter(user_email=email)
        serializer = UserAccountSerializer(data, many=True)
        
        return JsonResponse({"Success": serializer.data}, status=200)
    else:
        return Response({"Error": "Wrong Request Method"}, status=400)