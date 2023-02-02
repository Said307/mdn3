from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import *

from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "date_of_birthday",
        "phone_number",
        "gender",
        
    ]
    #prepopulated_fields = {"slug": ("title",)}  # slug get populated automatically
    list_filter = ['gender']


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "first_name",
        "last_name",
        "phone_number",
        "address1",
        "city",
        "country"
        
    ]
    #prepopulated_fields = {"slug": ("title",)}  # slug get populated automatically
    list_filter = ['country','city']

admin.site.register(Profile,ProfileAdmin)
 
admin.site.register(Address,AddressAdmin)