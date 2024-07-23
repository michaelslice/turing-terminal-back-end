from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.http import HttpResponse
from django.http import JsonResponse
import yahoo_fin.stock_info as si

'''

The function num_to_numeric(market_cap_str) is used to convert
a string to a numeric value

@param market_cap_str: Represents a market cap (3.14T)

@return: This function will return the numeric conversion of the string

@notes: Supports only millions, billions, and trillions into this conversion
Million: 10^6(1,000,000)
Billion: 10^9(1,000,000,000)
Trillion: 10^12(1,000,000,000,000)
'''
def num_to_numeric(market_cap_str):
    units = {'B': 10**9, 'M': 10**6, 'T': 10**12}
    if market_cap_str[-1] in units: # Check if last character is one of the keys in units
        return float(market_cap_str[:-1]) * units[market_cap_str[-1]]
    return float(market_cap_str)
            

@api_view(['GET'])
def get_screener(request):
    
    if request.method == "GET":
               
        ticker = request.GET.get("ticker")
        operand = request.GET.get("operand")
        value = request.GET.get("value")
        tickers = si.tickers_sp500()     
        
        print(ticker, operand, value)
        
        if ticker != None and operand == None and value == None:
   
            for ticker in tickers:
                ticker_price = round(si.get_live_price(ticker), 2)
                my_dic = {ticker: ticker_price}
        
        elif ticker and operand and value != None:
            
            for ticker in tickers:
                ticker_price = round(si.get_live_price(ticker), 2)
                ticker_market_cap = si.get_stats_valuation(ticker)
                metadeta = ticker_market_cap[['Current']]
                metadeta["Numeric"] = metadeta['Current'].apply(num_to_numeric)
                
                if metadeta['Numeric'][0] > value:
                
                    my_dic = {ticker: ticker_price}
        
        
        return JsonResponse(my_dic(orient="records"), safe=False, status=200)
    
        # return JsonResponse(my_dic(orient="records"), safe=False, status=200)
    
    else:
        return JsonResponse({"Error": "Invalid Request Method"}, status=400)