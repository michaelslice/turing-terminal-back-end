from django.urls import path
from . import views

'''
@note urlpatterns: Contains a list of URL pattern mappings for the Django project
'''
urlpatterns = [
   path('', views.test_view, name="test"),
   
    # yfinance test routes
    path('msft/', views.get_msft, name="get_msft"),
    path("msftholders/", views.get_msft_holders, name="getholders"),
    path('msft/options/', views.get_msft_options_data, name="get_msft_options"),
    path('msft/recommendations/', views.get_msft_recoommendations, name="get_msft_recommendations"),
    path('msft/actions/', views.get_msft_actions, name="get_msft_actions"),
    path('msft/balance-sheet/', views.get_msft_balance_sheet, name="get_msft_balance_sheet"),
    path('msft/income-statement/', views.get_msft_income_statement, name="get_msft_income_statement"),
    path('msft/cash-flow/', views.get_msft_cash_flow_statement, name="get_msft_cash_flow"),
]
