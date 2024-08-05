from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.http import HttpResponse
from django.http import JsonResponse
import yfinance as yf
import requests
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv()
MY_ENV_VAR = os.getenv("ALPHA_VANTAGE_API_KEY")


'''
The function get_intraday(request) is used to handle a GET request and 
retrieve intraday sales data for a specific ticker

@param request: Is a HTTP object which contains data about the request

@return JsonResponse: Represents a object of data that is sent back to the client

@note: This function uses the Alpha Vantage API (Time Series Stock Data), found at https://www.alphavantage.co/documentation/
'''
def get_intraday(request):
    if request.method == "GET":

        ticker = request.GET.get("ticker")
        
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={MY_ENV_VAR}'
        r = requests.get(url)
        data = r.json()
        
        return JsonResponse(data, safe=False, status=200)
    
    else:
        return JsonResponse({"Failure": "Server Error"}, status=400)