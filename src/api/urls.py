from django.urls import path
from . import views
'''
@note urlpatterns: Contains a list of URL pattern mappings for the Django project
'''
urlpatterns = [
    path('stocklist/', views.StockListCreate.as_view(), name="stock_list_create_view"),
    path('stocklist/<int:pk>/', 
         views.StockListPostRetrieveUpdateDelete.as_view(), 
         name="update"
        ),

]
