from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.http import HttpResponse
from django.http import JsonResponse
import yfinance as yf
from quotemonitor.model import Ticker
import requests
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv()
MY_ENV_VAR = os.getenv("ALPHA_VANTAGE_API_KEY")

'''

The function upload_ticker(request) is used to 

@param request: Is a HTTP object which contains data about the request

@return JsonResponse: Represents a object of data that is sent back to the client

@note: This function uses the Alpha Vantage API, found at https://www.alphavantage.co/documentation/

'''
def upload_ticker(request):
    
    if request.method == "GET":
        
        ticker = request.GET.get("ticker")
        
        url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=demo'
        # url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={MY_ENV_VAR}'
        r = requests.get(url)
        data = r.json()
        data = pd.DataFrame(data)
        
        #new_ticker = Ticker(symbol="AAPL", last="12", bid="12", ask="12", change_percent="12", volume="12")
        #new_ticker.save()     
        
        quote_data = data['Global Quote']
        df = pd.DataFrame([quote_data])  

        # Change names
        columns = {
        '01. symbol': 'symbol',
        '02. open': 'open',
        '03. high': 'high',
        '04. low': 'low',
        '05. price': 'price',
        '06. volume': 'volume',
        '07. latest trading day': 'latestTradingDay',
        '08. previous close': 'previousClose',
        '09. change': 'change',
        '10. change percent': 'changePercent'
        }

        df = df.rename(columns=columns)

        return JsonResponse(df.to_dict(orient="records"), status=200, safe=False) 

    else:
        return JsonResponse({"Error": "Invalid Request Method"}, status=400)
