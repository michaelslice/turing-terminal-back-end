from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.http import JsonResponse
import yfinance as yf
import requests
import os
from dotenv import load_dotenv
import pandas as pd
import csv
load_dotenv()
MY_ENV_VAR = os.getenv("ALPHA_VANTAGE_API_KEY")

'''
The function get_ipos(request) is used to handle a GET request and 
retrieve the most recent upcoming IPOs

@param request: Is a HTTP object which contains data about the request

@return JsonResponse: Represents a object of data that is sent back to the client

@note: This function uses the Alpha Vantage API, found at https://www.alphavantage.co/documentation/
'''
@api_view(['GET'])
def get_ipos(request):
    
    if request.method == "GET":

        CSV_URL = f'https://www.alphavantage.co/query?function=IPO_CALENDAR&apikey={MY_ENV_VAR}'

        with requests.Session() as s:
            download = s.get(CSV_URL)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            
        ipos = pd.DataFrame(my_list[1:], columns=my_list[0]).head(100)

        return JsonResponse(ipos.to_dict(orient="records"), safe=False)
    
    else:
        return JsonResponse({"Error": "Invalid Request Method"}, status=400)