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
def get_balance_sheet(request):
    
    if request.method == "GET":

        ticker = request.GET.get("ticker")

        url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={ticker}&apikey={MY_ENV_VAR}'

        r = requests.get(url)
        data = r.json()        
        data = pd.DataFrame(data['annualReports'])
        
        return JsonResponse(data.to_dict(orient="records"), safe=False)

    else:
        return JsonResponse({"Error": "Invalid Request Method"}, status=400)


@api_view(['GET'])
def get_cash_flow(request):
    
    if request.method == "GET":

        ticker = request.GET.get("ticker")

        url = f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={ticker}&apikey={MY_ENV_VAR}'

        r = requests.get(url)
        data = r.json()        
        data = pd.DataFrame(data['annualReports'])
        
        return JsonResponse(data.to_dict(orient="records"), safe=False)

    else:
        return JsonResponse({"Error": "Invalid Request Method"}, status=400)


@api_view(['GET'])
def get_income_statement(request):
    
    if request.method == "GET":

        ticker = request.GET.get("ticker")

        url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={ticker}&apikey={MY_ENV_VAR}'

        r = requests.get(url)
        data = r.json()        
        data = pd.DataFrame(data['annualReports'])
        
        return JsonResponse(data.to_dict(orient="records"), safe=False)

    else:
        return JsonResponse({"Error": "Invalid Request Method"}, status=400)
