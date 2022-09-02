

from django.urls import path,include,reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView


from . import views

app_name = 'user'


urlpatterns = [
path('login/',views.LoginView.as_view(template_name ='user/login.html',
    redirect_authenticated_user= True ),name="login"),
path('logout/',LogoutView.as_view(next_page=reverse_lazy('user:login')),name="logout"),

#path('reset',views.ResetForm.as_view(),name='PasswordResetForm'),

]