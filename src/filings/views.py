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

The function get_filings(request) is used to handle a GET request and 
retrieve SEC filings for a specific ticker in the request header

@param request: Is a HTTP object which contains data about the request

@return Response: Represents a object of data that is sent back to the client

@note: This function uses the SEC API, found at https://sec-api.io/docs/query-api/python-example

'''
@api_view(['GET'])
def get_filings(request):
    if request.method == "GET":
        ticker = request.GET.get("ticker")
        if not ticker:
            return Response({"Error": 'No Stock Ticker Provided'}, status=400)

        queryApi = QueryApi(api_key=MY_ENV_VAR)
        query = {
            "query": f"ticker:{ticker}",
            "from": "0",
            "size": "10",
            "sort": [{"filedAt": {"order": "desc"}}]
        }

        response = queryApi.get_filings(query)
        if 'filings' not in response:
            return Response({"Error": "No filings found for the provided ticker."}, status=404)

        metadata = pd.DataFrame.from_records(response['filings'])

        # Keep only necessary columns
        metadata = metadata[[
            "ticker",
            "formType",
            "linkToFilingDetails",
            "description",
            "filedAt",
            "periodOfReport"
        ]]
        # Replace null values with empty string
        metadata = metadata.fillna('')
        
        return Response(metadata.to_dict(orient="records"), status=200)
    
    else:
        return Response({"Error": 'Invalid request method.'}, status=405)