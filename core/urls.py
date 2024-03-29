"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.views.generic import RedirectView
from rest_framework.authtoken.views import obtain_auth_token
from core import settings
from django.conf.urls.static import static

from catalog.views import *

urlpatterns = [
    path('admin/', admin.site.urls,),
     
    path('catalog/', include('catalog.urls',namespace='catalog')),
    path('', include('catalog.urls',namespace='home')),
 
    path("account/",include("user.urls",namespace="account")),
    path('contact/',ContactUs.as_view(),name='contactus'),
    path('api/', include('api.urls',namespace='api')),
    path('api2/', include('api2.urls',namespace='api2')),


]

urlpatterns += [
    path('api2/auth/', include('rest_framework.urls')),  #Authentication URLs
   
]



if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)