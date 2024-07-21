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
import yahoo_fin.stock_info as si
load_dotenv()
MY_ENV_VAR = os.getenv("POLYGON_API_KEY")


@api_view(['GET'])
def get_description(request):
    
    if request.method == "GET":

        ticker = request.GET.get("ticker")

        ticker = yf.Ticker("AAPL")
        current_price = ticker.history(period='1d')['Close'][0]

        market_data = si.get_stats_valuation("aapl")
        market_cap = market_data['Current'][0]

        url = f'https://api.polygon.io/v3/reference/tickers/AAPL?apiKey={MY_ENV_VAR}'
        r = requests.get(url)
        data = r.json()
        
        # Flatten the JSON data, and convert nested objects to now have dot notation, ex: results.ticker
        df = pd.json_normalize(data)

        data = [{ 
                "ticker": df['results.ticker'][0],
                "phonenumber": df['results.phone_number'][0],
                "address": df['results.address.address1'][0],
                "city": df['results.address.city'][0],
                "state": df['results.address.state'][0],
                "description": df['results.description'][0],
                "website": df['results.homepage_url'][0],
                "zipcode": df['results.address.postal_code'][0],
                "price": round(current_price, 2),
                "marketcap": market_cap,
        }]
        
        return JsonResponse(data, safe=False, status=200)

    else:
        return JsonResponse({"Error": "Invalid Request Method"}, status=400)
