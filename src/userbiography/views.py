from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.http import HttpResponse
from django.http import JsonResponse
from userbiography.model import UserBio
import requests
import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def post_user_bio(request):
    if request.method == "POST":
        params = request.data.get('params', {})

        user_email = params.get("userEmail")
        user_name = params.get("userName")
        first_name = params.get("firstName")
        last_name = params.get("lastName")
        company = params.get("company")

        user = UserBio(
            user_email=user_email, 
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            company=company
        )
        user.save() # Update database with current data
        
        return Response({"SUCCESS!", user}, status=200)
    else:
        return Response({"Error": "Wrong Request Method"}, status=400)
