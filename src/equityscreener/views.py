from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.http import HttpResponse
from django.http import JsonResponse
import yfinance as yf
import yahoo_fin.stock_info as si
import requests
import os
from dotenv import load_dotenv

load_dotenv()
MY_ENV_VAR = os.getenv("ALPHA_VANTAGE_API_KEY")

@api_view(['GET'])
def get_screener(request):
    
    if request.method == "GET":
               
        symbol = request.GET.get("ticker")
        interval = "5min"
                
        if not symbol:
            return JsonResponse({"Error": "Invalid Symbol"}, status=400)
                
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={MY_ENV_VAR}'
        try:
            r = requests.get(url)
            r.raise_for_status() # If Bad HTTP Response 
            data = r.json()

            return JsonResponse(data, safe=False)
 
        except Exception as e:
            return JsonResponse({"Error": str(e)}, status=400)
    else:
        return JsonResponse({"Error": "Invalid Request Method"}, status=400)