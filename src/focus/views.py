from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.http import HttpResponse
from django.http import JsonResponse
import yfinance as yf


@api_view(['GET'])
def get_ticker(request):
    
    if request.method == "GET":

        stock_ticker = request.GET.get('ticker')
        
        if stock_ticker:
            stock = yf.Ticker(stock_ticker)

            stock_data = stock.history(period='1d')
            
            open_price = stock_data['Open'][0]
            close_price = stock_data['Close'][0]
            day_change = close_price - open_price
            
            day_percent_change = (day_change / open_price) * 100
            current_price = stock.history(period='1d')['Close'][0]

            data = {
                "price" : round(current_price, 2),
                "price_change" : round(day_change, 2),
                "percent_change" : round(day_percent_change, 2),
            }          
        return JsonResponse(data)
        
    else:
        return JsonResponse({"Error": 'No Stock Ticker Provided'}, status=400)  
    