from django.urls import path
from . import views

'''
@note urlpatterns: Contains a list of URL pattern mappings for the Django project
'''
urlpatterns = [
    path('', views.test_view, name="test"),
   
    path('ticker/', views.get_ticker, name="ticker"),
   
    # yfinance test routes
]
