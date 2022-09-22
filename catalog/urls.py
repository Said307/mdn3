


from string import Template
from tempfile import template
from django.views.generic.base import TemplateView

from django.urls import path,include

from . import views


app_name = 'catalog'


urlpatterns = [
    path('',TemplateView.as_view(template_name="home.html"),name='home' ),
    path('parts/',views.ListPartView.as_view(),name='allparts'),
    path('parts/<str:pk>/',views.DetailPartView.as_view(), name='detailpart'),
    path('thanks/',TemplateView.as_view(template_name='thanks.html'),name='thanks'),
 



]