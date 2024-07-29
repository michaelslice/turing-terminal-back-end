from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.http import HttpResponse
from django.http import JsonResponse
import yahoo_fin.stock_info as si
import os
from dotenv import load_dotenv
import pandas as pd
import yahoo_fin.stock_info as si
load_dotenv()
MY_ENV_VAR = os.getenv("POLYGON_API_KEY")
import requests


@api_view(['GET'])
def get_screener(request):
    
    if request.method == "GET":
               
        # ticker = request.GET.get("ticker")
        operand = request.GET.get("operand")
        value = request.GET.get("value")

        if not operand and not value:
            return JsonResponse({"Error", "Operand and Value are Required"}, status=400)

        # Dictionary to map passed in operands to, a lambda expression for evaluation
        # Can be called using valid_operations[operand](arg1, arg2)
        valid_operations = {
            "=": lambda x, y: x == y,
            ">": lambda x, y: x > y, 
            "<": lambda x, y: x < y,
            ">=": lambda x, y: x >= y,
            "<=": lambda x, y: x <= y,
        }
        
        try:
            value = float(value)
        except Exception as e:
            return JsonResponse({"Error": e}, status=400)

        # Get S&P 500 companies
        sp500_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
        sp500_data = pd.read_html(sp500_url)[0]
        ticker_list = sp500_data['Symbol'].tolist()
        results = []

        for ticker in ticker_list:
            url = f"https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={MY_ENV_VAR}"
            r = requests.get(url)
            data = r.json()
            
            if 'results' in data:
                ticker_data = data['results']
                market_cap = ticker_data.get("market_cap", None)
                
                # valid_operations[operand](market_cap, value): 
                # [operand]: The passed in operand from the front-end is used as the key for the dictionary
                # (market_cap, value): Calls the lambda function with market_cap, and value as arguements for x, and y
                if market_cap is not None and valid_operations[operand](market_cap, value):
                    row = {
                        "ticker": ticker_data.get("ticker", None),
                        "name": ticker_data.get("name", None),
                        "market_cap": round(ticker_data.get("market_cap", None), 2)
                    }
        
                    print(row)      
                    results.append(row)
                    
        results = pd.DataFrame(results)

        return JsonResponse(results.to_dict(orient="records"), safe=False, status=200)
    
    else:
        return JsonResponse({"Error": "Invalid Request Method"}, status=400)