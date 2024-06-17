from django.urls import path
from . import views

# Logic to Configure URL
urlpatterns = [
    path("", views.home, name="home")
]