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


def get_intraday(request):
    if request.method == "GET":

        ticker = request.GET.get("ticker")
        
        # url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={MY_ENV_VAR}'
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=IBM&apikey=demo'
        r = requests.get(url)
        data = r.json()
        
        return JsonResponse(data, safe=False, status=200)
    
    else:
        return JsonResponse({"Failure": "Server Error"}, status=400)