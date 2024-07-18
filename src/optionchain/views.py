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


@api_view(['GET'])
def get_option_chain(request):
    
    if request.method == "GET":

        ticker = request.GET.get("ticker")

        url = f'https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&symbol={ticker}&apikey={MY_ENV_VAR}'

        r = requests.get(url)
        data = r.json()        
        data = pd.DataFrame(data['data'])
        
        return JsonResponse(data.to_dict(orient="records"), safe=False)

    else:
        return JsonResponse({"Error": "Invalid Request Method"}, status=400)


@api_view(['GET'])
def get_calls(request):
    
    if request.method == "GET":

        ticker = request.GET.get("ticker")

        url = f'https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&symbol={ticker}&apikey={MY_ENV_VAR}'

        r = requests.get(url)
        data = r.json()        
        data = pd.DataFrame(data['data'])
        data.drop(data.loc[data['type']=='put'].index, inplace=True) # Remove all put options from data
        
        return JsonResponse(data.to_dict(orient="records"), safe=False)

    else:
        return JsonResponse({"Error": "Invalid Request Method"}, status=400)


@api_view(['GET'])
def get_puts(request):
    
    if request.method == "GET":

        ticker = request.GET.get("ticker")

        url = f'https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&symbol={ticker}&apikey={MY_ENV_VAR}'

        r = requests.get(url)
        data = r.json()        
        data = pd.DataFrame(data['data'])
        data.drop(data.loc[data['type']=='call'].index, inplace=True) # Remove all call options from data
        
        return JsonResponse(data.to_dict(orient="records"), safe=False)

    else:
        return JsonResponse({"Error": "Invalid Request Method"}, status=400)
