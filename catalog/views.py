from multiprocessing import context
from django.core.files.storage import default_storage
from django.shortcuts import render,redirect 
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.views .decorators.cache import cache_page 
from django.utils.decorators import method_decorator
from django.core.cache.backends import locmem
 

from. models import Part
from . forms import ContactForm
from .  extra import Orders
from user.models import CustomUser

 

from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic.base import TemplateView,RedirectView
from django.views.generic import ListView,DetailView


@cache_page(60*15)  
def sadiqcookie1(request):
    
    if request.method =='GET':
        if  'country' in request.COOKIES:
            country= request.COOKIES['country']
        else:
            country = 'No Country'
    elif request.method=='POST':
        country = request.POST.get('country')

    context ={'country':country, }
    response =render(request, 'catalog/sadiqcookie1.html',context )
    response.set_cookie('country',country)
    
    return response



@method_decorator(cache_page(60*5),name='dispatch')
class ListPartView(ListView):
    model = Part
    template_name = "catalog/ListPartsView.html"

    context_object_name ='carparts'
    queryset = Part.parts.all()

    def get_context_data(self, **kwargs): 

        context =  super().get_context_data(**kwargs)
        context['session']= self.request.session.items()
        context['cookies']= self.request.COOKIES
        context['work']= 'Solihull'
        context['cache']= locmem._caches
        return context
    
    def render_to_response(self,context, **response_kwargs): 

        response= super().render_to_response(context, **response_kwargs)
        response.set_cookie('food','desert')
        return response 

class DetailPartView(DetailView):

    model = Part
    template_name = 'catalog/DetailView.html' 
    context_object_name ='partnumber'
 


class ContactUs(FormView):
    template_name =  'ContactUs.html'
    form_class = ContactForm
    
    success_url = '/thanks'
    initial = {'name': 'Haji'}

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(**kwargs)
        initial['name'] = 'Haji'
        return initial

    def form_valid(self,form):

        name= form.cleaned_data['name']
        telephone= form.cleaned_data['telephone']
        message= form.cleaned_data['message']
        image= self.request.FILES['image']
       
        with open(r"C:\Users\ssaid\OneDrive\OneDrive - JAGUAR LAND ROVER\Desktop\ContactUs.txt",'a') as file:
            file.write(f'{name} \n {telephone} \n{message}')
       
        file_name = default_storage.save(image.name,image)
         
         
        return super().form_valid(form)

    
    def process(self,**kwargs):
        """ write to file"""
        pass

 


""" 

  

    def MyLogin(request):
   
    form =  AuthenticationForm()
     
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == 'POST':
        form =  AuthenticationForm(data=request.POST)
        email =  request.POST.get('username')
        password =  request.POST.get('password')
      
        try:
            user =  CustomUser.objects.get(email=email)
        except:
            messages.error(request, "User not found")   
        user = authenticate(request,email=email,password=password)
        if user:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request, "Incorrect password")

  
    context = {"form": form}
    print('sadiiiiiiiq')
    return render(request, "user/loogin.html", context) """


 
  
 