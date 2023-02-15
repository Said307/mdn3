
from  rest_framework import serializers   
from django.contrib.auth.models import User
from product.models import * 

from ..models import *





class UserSerializer(serializers.ModelSerializer):

    profile =  serializers.PrimaryKeyRelatedField(read_only=True)
    #url = serializers.CharField(source='get_absolute_url',read_only=True )
    class Meta:
        model = User
        fields = ('profile','id','username',  'first_name', 'last_name',  'email','is_active','is_staff','is_superuser')
      







#####################################################################################################


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'




class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        #model = Userm
        fields = '__all__'
