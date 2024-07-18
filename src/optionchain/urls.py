from django.urls import path
from . import views

'''
@note urlpatterns: Contains a list of URL pattern mappings for the Django project
'''
urlpatterns = [
   path('getoptionchain/', views.get_option_chain, name="getoptionchain"),
   path('getcalls/', views.get_option_chain, name="getcalls"),
   path('getputs/', views.get_option_chain, name="getputs"),
]
