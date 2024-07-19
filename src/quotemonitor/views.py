from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.http import HttpResponse
from django.http import JsonResponse
import yfinance as yf
from quotemonitor.model import Ticker

def upload_ticker(request):
    
    ticker = request.GET.get("ticker")
    print(ticker)
    
    if request.method == "POST":
        
        #new_ticker = Ticker(symbol="AAPL", last="12", bid="12", ask="12", change_percent="12", volume="12")
        #new_ticker.save()
        
        return JsonResponse({"TEST": "test"}, status=200)

    else:
        return JsonResponse({"Error": "Invalid Request Method"}, status=400)
