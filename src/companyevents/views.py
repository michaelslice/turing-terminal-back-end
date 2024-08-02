from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.http import HttpResponse
from django.http import JsonResponse
import yfinance as yf
from sec_api import QueryApi
import requests
import os
from dotenv import load_dotenv
import pandas as pd
import yahoo_fin.stock_info as si
load_dotenv()
MY_ENV_VAR = os.getenv("EDGAR_SEC_API_KEY")

'''
https://sec-api.io/docs/form-8k-data-search-api#request-parameters
'''
def get_company_events(request):

    if request.method == "GET":
        
        ticker = request.GET.get("ticker")

        queryApi = QueryApi(api_key=MY_ENV_VAR)
        query = {
            "query": f'ticker:{ticker}',
            "from": "0",
            "size": "50"
        }

        response = queryApi.get_filings(query)
        metadata = pd.DataFrame.from_records(response['filings'])

        metadata = metadata[[
            'ticker',
            'formType',
            'linkToTxt',
            'description',
            'filedAt',
            'periodOfReport'
        ]]
        # Replace null values with empty string
        metadata = metadata.fillna('')
    
        return JsonResponse(metadata.to_dict(orient="records"), safe=False, status=200)

    else:
        return Response({"Error": 'Invalid request method.'}, status=405)