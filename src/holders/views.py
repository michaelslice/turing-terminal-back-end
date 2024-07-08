from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.http import HttpResponse
from django.http import JsonResponse
import yfinance as yf


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