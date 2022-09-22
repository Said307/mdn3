

from django.urls import path,include,reverse_lazy
from django.contrib.auth import views as authviews


 

app_name = 'user'


urlpatterns = [
path('login/',authviews.LoginView.as_view(template_name ='user/login.html',

    redirect_authenticated_user= True ),name="login"),
path('logout/',authviews.LogoutView.as_view(next_page=reverse_lazy('user:login')),name="logout"),

path('reset/',authviews.PasswordResetView.as_view(template_name='user/PasswordResetForm.html',success_url = reverse_lazy('user:emailsent'),
                 email_template_name='user/email_template.html'),name='reset'),
path('reset/done/',authviews.PasswordResetDoneView.as_view(template_name='user/PasswordResetConfirmation.html',
),name='emailsent'),


path('password_reset_confirm/<uidb64>/<token>',authviews.PasswordResetConfirmView.as_view(template_name='user/NewpasswordForm.html',success_url = reverse_lazy('user:password_reset_done')),name='resetlink'),
path('reset/complete/',authviews.PasswordResetCompleteView.as_view(template_name='user/ResetComplete.html'),name="password_reset_done")

]