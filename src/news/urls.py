from django.urls import path
from . import views

'''
@note urlpatterns: Contains a list of URL pattern mappings for the Django project
'''
urlpatterns = [
   path('getnews/', views.get_news, name="getnews"),
]
