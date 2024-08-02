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

'''
Create a User object in the db for the first time or update the users email, user_name, first_name, last_name, and company 

@param: 
    request: Takes a request object which contains data sent from the front end

@Notes: 
    User.objects.get_or_create(): Used to retrive existing users, or update the db if one all ready exists
    update_or_create(): Ensures no duplicate entries are added into the db,

@Relavant Resources: 
    https://docs.djangoproject.com/en/5.0/topics/db/queries/
    https://docs.djangoproject.com/en/5.0/ref/models/querysets/
'''
@api_view(["POST"])
def post_user_bio(request):
    if request.method == "POST":
        params = request.data.get('params', {})

        user_email = params.get("userEmail")
        user_name = params.get("userName")
        first_name = params.get("firstName")
        last_name = params.get("lastName")
        company = params.get("company")

        # Try to upload user data to database
        try:
            # Check if user with the given email exists, if not create it 
            user, created = User.objects.get_or_create(
                # Set the email that should be searched for in the User instance 
                email=user_email,
                # Create or, update these fields
                defaults={
                    'username': user_name,
                    'first_name': first_name,
                    'last_name': last_name,                    
                }
            ) 
            
            # Create or update the UserAccount
            UserAccount.objects.update_or_create(
                # Search for a user, matching in the User instance
                user=user,
                # Create or, update these fields
                defaults={
                    'user_email': user_email, 
                    'user_name': user_name,
                    'first_name': first_name,
                    'last_name': last_name,
                    'company': company
                }
            )
            
        except Exception as e:
            return JsonResponse({"Error": str(e)}, status=400)
          
        return Response({"SUCCESS": "User Data Saved Successfully"}, status=200)
    else:
        return Response({"Error": "Wrong Request Method"}, status=400)