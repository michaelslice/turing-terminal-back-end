"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/v1/api/", include('api.urls')),
    path("api/v1/test/", include('test.urls')),
   
    path("api/v1/focus/", include('focus.urls')),
    path("api/v1/chart/", include('chart.urls')),
    path("api/v1/chat/", include('chat.urls')),
    path("api/v1/companyevents/", include('companyevents.urls')),
    path("api/v1/equityscreener/", include('equityscreener.urls')),
    path("api/v1/filings/", include('filings.urls')),
    path("api/v1/financials/", include('financials.urls')),
    path("api/v1/help/", include('help.urls')),
    path("api/v1/holders/", include('holders.urls')),
    path("api/v1/ipo/", include('ipo.urls')),
    path("api/v1/news/", include('news.urls')),
    path("api/v1/optionchain/", include('optionchain.urls')),
    path("api/v1/quotemonitor/", include('quotemonitor.urls')),
    path("api/v1/timeandsales/", include('timeandsales.urls')),
]