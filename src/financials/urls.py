from django.urls import path
from . import views

'''
@note urlpatterns: Contains a list of URL pattern mappings for the Django project
'''
urlpatterns = [
   path('getbalancesheet/', views.get_balance_sheet, name="getbalancesheet"),
   path('getcashflow/', views.get_cash_flow, name="getcashflow"),
   path('getincomestatement/', views.get_income_statement, name="getincomestatement"),

]
