from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.http import HttpResponse
from django.http import JsonResponse
import yfinance as yf


@api_view(['GET'])  
def test_view(request): 
    return Response("THIS IS A TEST", status=status.HTTP_200_OK)


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


def get_msft_info(request):
    msft = yf.Ticker("MSFT")
    
    # Get historical market data
    hist = msft.history(period="1mo")
    
    # Show meta information about the history 
    msft.history_metadata
    
    # Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default.
    # Note: If more are needed use msft.get_earnings_dates(limit=XX) with increased limit argument.
    msft.earnings_dates    

    # show ISIN code - *experimental*
    # ISIN = International Securities Identification Number
    msft.isin

    # show news
    msft.news
    
    msft.get_shares_full(start="2022-01-01", end=None)
    
    stock_info = msft.info
    data = {
        'name': stock_info.get('shortName', 'N/A'),
        'symbol': stock_info.get('symbol', 'N/A'),
        'currentPrice': stock_info.get('regularMarketPrice', 'N/A'),
        'marketCap': stock_info.get('marketCap', 'N/A'),
    }
    return JsonResponse(data)


def get_msft_options_data(request):
    msft = yf.Ticker("MSFT")

    # Show options expirations
    msft.options

    # Get option chain for specific expiration
    opt = msft.option_chain('YYYY-MM-DD')
    # Data available via: opt.calls, opt.puts
    
    data = {
        "options":  msft.options,
        "options chain":  opt, 
    }
    return JsonResponse(data)     


def get_msft_recoommendations(request):
    msft = yf.Ticker("MSFT")

    # Show reccomendations
    msft.recommendations
    msft.recommendations_summary
    msft.upgrades_downgrades

    data = {
        "recommendations": msft.recommendations,
        "recommendations summary":  msft.recommendations_summary, 
        "upgrades and downgrades": msft.splits,  
    }
    return JsonResponse(data)    
   

def get_msft_actions(request):
    msft = yf.Ticker("MSFT")
    
    # Show actions 
    msft.actions
    msft.dividends
    msft.splits
    msft.capital_gains
    
    data = {
        "actions":   msft.actions,
        "dividends": msft.dividends,  
        "splits": msft.splits,  
        "capital gains": msft.capital_gains,  
    }
    return JsonResponse(data)    


def get_msft_balance_sheet(request):
    msft = yf.Ticker("MSFT")
    
    # Balance sheet
    msft.balance_sheet
    msft.quarterly_balance_sheet
    
    data = {
        "income balance": msft.balance_sheet,
        "quarterly balance statement": msft.quarterly_balance_sheet,  
    }
    return JsonResponse(data)    


def get_msft_income_statement(request):
    msft = yf.Ticker("MSFT")
    
    # Income statement
    msft.income_stmt
    msft.quarterly_income_stmt
    
    data = {
        "income statement": msft.cash_flow,
        "quarterly income statement": msft.quarterly_cashflow,  
    }
    return JsonResponse(data)


def get_msft_cash_flow_statement(request):
    msft = yf.Ticker("MSFT")
    
    # Cash flow statement
    msft.cash_flow
    msft.quarterly_cashflow
    
    data = {
        "cash flow": msft.cash_flow,
        "quarterly cashflow": msft.quarterly_cashflow,  
    }
    return JsonResponse(data)


def get_msft_holders(request): 
    msft = yf.Ticker("MSFT")
    
    # Show holders
    msft.major_holders
    msft.institutional_holders
    msft.mutualfund_holders
    msft.insider_transactions
    msft.insider_purchases
    msft.insider_roster_holders
    
    data = {
        "major holders": msft.major_holders,
        "institutional holders": msft.institutional_holders,  
        "mutualfund holders": msft.mutualfund_holders,
        "insider transactions": msft.insider_transactions,
        "insider purchase" : msft.insider_purchases,
        "insider roster holders" : msft.insider_roster_holders,
    }
    return JsonResponse(data)
    