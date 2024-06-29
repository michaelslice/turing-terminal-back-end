from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.http import HttpResponse
from django.http import JsonResponse
import yfinance as yf

def get_msft(request):
    msft = yf.Ticker("MSFT")
    stock_info = msft.info
    data = {
        'name': stock_info.get('shortName', 'N/A'),
        'symbol': stock_info.get('symbol', 'N/A'),
        'currentPrice': stock_info.get('regularMarketPrice', 'N/A'),
        'marketCap': stock_info.get('marketCap', 'N/A'),
    }
    return JsonResponse(data)


