
from django.views.generic.base import TemplateView
from django.urls import path,include

from.views import UserView
 


app_name = "users"

urlpatterns=[
    
    path('users/',UserView.as_view(),name='allusers'),



]