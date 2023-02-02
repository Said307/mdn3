




from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Profile
        fields = ('user',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Profile
        fields = ('user',)
