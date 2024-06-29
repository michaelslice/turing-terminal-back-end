from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.http import HttpResponse
from django.http import JsonResponse
import yfinance as yf

@api_view(['GET'])  
def test_view(request): 
    return Response("THIS IS A TEST", status=status.HTTP_200_OK)


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
                "price" : current_price,
                "price_change" : day_change,
                "percent_change" : day_percent_change,
            }          
        return JsonResponse(data)
        
    else:
        return JsonResponse({"error": 'No stock ticker provided'}, status=400)  
    