from django.urls import path
from . import views

'''
@note urlpatterns: Contains a list of URL pattern mappings for the Django project
'''
urlpatterns = [
   path('', views.get_msft, name="test"),  
]
