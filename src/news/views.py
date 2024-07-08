from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.http import HttpResponse
from django.http import JsonResponse
import yfinance as yf


@api_view(['GET'])
def get_news(request):
    if request.method == "GET":
        stock_ticker = request.GET.get("ticker")

        if not stock_ticker:
            return JsonResponse({"Error": 'No Stock Ticker Provided'}, status=400)

        try:
            stock = yf.Ticker(stock_ticker)
            stock_news = stock.news

            limit = int(request.GET.get("limit", 10))
            news_data = [{
                "title": news_item['title'],
                "publisher": news_item['publisher'],
                "link": news_item['link']
            } for news_item in stock_news[:limit]]

            return JsonResponse(news_data, safe=False)

        except Exception as e:
            return JsonResponse({"Error": str(e)}, status=500)

    return JsonResponse({"Error": 'Method Not Allowed'}, status=405)