from django.urls import path
from . import views

'''
@note urlpatterns: Contains a list of URL pattern mappings for the Django project
'''
urlpatterns = [
   path('get_company_events/', views.get_company_events, name="get_company_events"),  
]