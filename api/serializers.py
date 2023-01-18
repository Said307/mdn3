



from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import authenticate
from catalog.models import *
 
 
from django.contrib.auth.password_validation import validate_password
class RegisterSerializer(serializers.ModelSerializer):

    password  = serializers.CharField(
        write_only =True,
        required =  True,
        validators = [validate_password],
    )
   
    password2 = serializers.CharField(write_only=True,required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'password2', 'name', 'phoneNum', 'address', 'email')

   
    def validate(self,data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password" : "Password fields didn't match."})
        return data

    
    





################################  Basic Serializer   ####################################

""" class SupplierSerializer(serializers.Serializer):
    id = serializers.IntegerField( )
    name =  serializers.CharField( )
    country = serializers.CharField( )
    email = serializers.EmailField()
    


    def create(self, validated_data):
  
        #Create and return a new `Snippet` instance, given the validated data.
      
        return Supplier.objects.create(**validated_data)

    def update(self, instance, validated_data):
   
       # Update and return an existing `Snippet` instance, given the validated data.
  
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.email = validated_data.get('email', instance.email)

        instance.save()
        return instance """





        



 
################################  Model Serializer   ####################################


class PartSerializer(serializers.ModelSerializer):
    #supplier = SupplierSerializer(many=True, read_only=True)   # explicit nesting
    class Meta:
        model = Part
        fields = '__all__'
        #depth = 1

    def to_representation(self,instance):
        representation = super().to_representation(instance)
        representation["location"]= instance.get_absolute_url()
        return representation


    # def to_internal_value(self,data):

    #     data = super().to_internal_value(data)
    #     data.pop('email')
    #     print(data)
    #     return  data




         
class SupplierSerializer(serializers.ModelSerializer):
    # parts= serializers.HyperlinkedRelatedField(
    #      many=True,
    #     read_only=True,
    #     view_name='api:part-detail')  # appname:viewname
    parts = serializers.PrimaryKeyRelatedField(  
            many=True,
            read_only=True)
 
    url = serializers.CharField(source='get_absolute_url',read_only=True )
    url2= serializers.ReadOnlyField()
    
    class Meta:
        model = Supplier
        fields = '__all__'
        #depth=2
       
    # def to_internal_value(self,data):

    #     data = super().to_internal_value(data)
    #     data.pop('email')
    #     print(data)
    #     return  data


################################  HyperLinkedModel Serializer   ####################################

""" 
class SupplierSerializer(serializers.HyperlinkedModelSerializer):
 
    url = serializers.HyperlinkedIdentityField(
        view_name='api:supplier-detail',
        lookup_field='pk')

    parts = serializers.HyperlinkedRelatedField(
            view_name='api:part-detail',
            many=True,read_only=True)
    
    class Meta:
        model = Supplier
        fields = '__all__'
       
        

class PartSerializer(serializers.HyperlinkedModelSerializer):              #must be call  url = 
    url = serializers.HyperlinkedIdentityField(
        view_name='api:part-detail',
        lookup_field='pk'
       )
    supplier = serializers.HyperlinkedRelatedField(
           
            read_only=True,
            view_name='api:supplier-detail')
  

    class Meta:
        model = Part
        fields = '__all__'
    """