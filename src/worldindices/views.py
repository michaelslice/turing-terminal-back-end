from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.http import HttpResponse
from django.http import JsonResponse
import yfinance as yf
import yahoo_fin.stock_info as si
import requests
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv()
MY_ENV_VAR = os.getenv("ALPHA_VANTAGE_API_KEY")

'''

The function get_world_indices(request) is used to handle a GET request
and retrive the most recent financial data for the world indices

@param request: Is a HTTP object which contains data about the request

@return JsonResponse: Represents a object of data that is sent back to the client

'''
@api_view(['GET'])
def get_world_indices(request):
    
    if request.method == "GET":
               
        major_indices = pd.read_html("http://finance.yahoo.com/world-indices")[0]

        major_indices.drop([
                        "Intraday High/Low", 
                        "52 Week Range",
                        "Day Chart",
                        "Volume"],
        axis=1, inplace=True)

        major_indices.rename(columns={
            "Symbol": "symbol",
            "Name":"name",
            "Last Price": "last_price",
            "Change": "change",
            "% Change": "change_percent",
        }, inplace=True)

        return JsonResponse(major_indices.to_dict(orient="records"), safe=False)
    
    else:
        return JsonResponse({"Error": "Invalid Request Method"}, status=400)