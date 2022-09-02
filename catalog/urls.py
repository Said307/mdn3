


from string import Template
from tempfile import template
from django.views.generic.base import TemplateView

from django.urls import path,include

from . import views


app_name = 'catalog'


urlpatterns = [
    path('',TemplateView.as_view(template_name="home.html") ),



]