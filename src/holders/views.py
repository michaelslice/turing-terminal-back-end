from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.http import HttpResponse
from django.http import JsonResponse
import yfinance as yf

'''

The function get_holders(request) is used to handle a GET request and 
retrieve the current holders for a specific ticker

@param request: Is a HTTP object which contains data about the request

@return JsonResponse: Represents a object of data that is sent back to the client

@note: This function uses the yfinance API, found at https://python-yahoofinance.readthedocs.io/en/latest/api.html

'''
@api_view(["GET"])
def get_holders(request):
    if request.method == "GET":
        stock_ticker = request.GET.get("ticker")

        if not stock_ticker:
            return JsonResponse({"Error": "No Stock Ticker Provided"}, status=400)

        try:
            stock = yf.Ticker(stock_ticker)
            stock_news = stock.institutional_holders

            if stock_news is None:
                return JsonResponse({"Error": "No Institutional Holders Data Available"}, status=404)

            limit = int(request.GET.get("limit", 10))
            
            # Convert to a List of Dictionaries
            news_data = stock_news.head(limit).to_dict(orient="records")

            return JsonResponse(news_data, safe=False)

        except Exception as e:
            return JsonResponse({"Error": str(e)}, status=500)

    return JsonResponse({"Error": "Method Not Allowed"}, status=405)