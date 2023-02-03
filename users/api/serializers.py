
from  rest_framework import serializers   
from django.contrib.auth.models import User
from ..models import *





class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('id','username',  'first_name', 'last_name',  'email','is_active','is_staff','is_superuser')
        depth = 2