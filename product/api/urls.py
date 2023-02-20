




from django.views.generic.base import TemplateView
from django.urls import path,include

from.views import *
 


app_name = "product"

urlpatterns=[
    
    
    path('products/', ProductListAPIView.as_view(), name='products'),
    path('browsinghistory/', BrowsingAPIView.as_view(), name='categories'),
    path('questions/', ProductQuestionsAPIView.as_view(), name='questions'),



]