from decimal import Decimal
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.http import HttpResponse
from django.http import JsonResponse
import yfinance as yf
import requests
import os
from dotenv import load_dotenv
import json
import pandas as pd
from userbiography.model import UserAccount
from quotemonitor.model import Ticker
load_dotenv()
MY_ENV_VAR = os.getenv("ALPHA_VANTAGE_API_KEY")


'''
The function upload_ticker(request) is used to 

@param request: Is a HTTP object which contains data about the request

@return JsonResponse: Represents a object of data that is sent back to the client

@note: This function uses the Alpha Vantage API, found at https://www.alphavantage.co/documentation/
'''
@api_view(['GET'])
def upload_ticker(request):
    
    if request.method == "GET":
        
        ticker = request.GET.get("ticker")
        email = request.GET.get("userEmail")
        
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={MY_ENV_VAR}'
        r = requests.get(url)
        data = r.json()
        data = pd.DataFrame(data)
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
                
        try:
            current_user = UserAccount.objects.get(user_email=email)
        except UserAccount.DoesNotExist:
            return JsonResponse({"Error": "User not found"}, status=404)
        
        # Check if the ticker already exists for the user
        if Ticker.objects.filter(user_id=current_user.pk, symbol=ticker).exists():
            return JsonResponse({"Error": "This ticker is already in your list, remove it first"}, status=400)
        
        # Save the new ticker data
        try:
            data = Ticker(
                symbol=df['symbol'].iloc[0],
                last=Decimal(str(df['price'].iloc[0])),
                open=Decimal(str(df['open'].iloc[0])),
                high=Decimal(str(df['high'].iloc[0])),
                low=Decimal(str(df['low'].iloc[0])),
                change_percent=Decimal(str(df['changePercent'].iloc[0].strip('%'))),
                volume=int(df['volume'].iloc[0]),
                user_id=current_user.pk,
            )
            data.save()
        except Exception as e:
            return JsonResponse({"Error": str(e)}, status=500)
        
        return JsonResponse(df.to_dict(orient="records"), status=200, safe=False)
    
    else:
        return JsonResponse({"Error": "Invalid Request Method"}, status=400)
    
    
'''
Get all the currently logged in users tickers
'''
@api_view(['GET'])
def get_tickers(request):
    if request.method == "GET":
        email = request.GET.get("userEmail")

        # Get the primary key for the logged in user, based on email
        current_user_pk = UserAccount.objects.get(user_email=email).pk
        
        if Ticker.objects.filter(id=current_user_pk).exists():
            ticker_list = Ticker.objects.all() 
            
            data = [{
                'symbol': ticker.symbol, 
                'previousClose': ticker.last, 
                'open': ticker.open, 
                'high': ticker.high, 
                'low': ticker.low, 
                'changePercent': ticker.change_percent, 
                'volume': ticker.volume
            } for ticker in ticker_list]
            
            return JsonResponse({"Tickers" : data}, status=200)
        else:
            return JsonResponse({"Error!": "User does not have any tickers"}, status=200)
        
    else:
        return JsonResponse({"Error": "Wrong Method"}, status=400)

'''
Delete the user requested ticker from the database 
'''
def delete_ticker(request):
    
    if request.method == "DELETE":
        print("test")
        return JsonResponse({"Test": "works"}, status=200)
    
    else:
        return json({"Error": "Wrong HTTP Method Requested"}, status=400)