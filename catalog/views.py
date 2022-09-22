from ast import Delete
from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView


from. models import Part
from . forms import ContactForm



from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic.base import TemplateView,RedirectView
from django.views.generic import ListView,DetailView

class ListPartView(ListView):
    model = Part
    template_name = "catalog/ListPartsView.html"

    context_object_name ='carparts'
    queryset = Part.parts.all()

class DetailPartView(DetailView):

    model = Part
    template_name = 'catalog/DetailView.html' 
    context_object_name ='partnumber'
    queryset = None



class ContactUs(FormView):
    template_name =  'ContactUs.html'
    form_class = ContactForm
    success_url = '/thanks'



    def form_valid(self,form):

        name= form.cleaned_data['name']
        telephone= form.cleaned_data['telephone']
        message= form.cleaned_data['message']
        with open(r"C:\Users\ssaid\OneDrive\OneDrive - JAGUAR LAND ROVER\Desktop\ContactUs.txt",'w') as file:
            file.write(f'{name} \n {telephone} \n{message}')

        return super().form_valid(form)

    
    def process(self,**kwargs):
        """ write to file"""
        pass


