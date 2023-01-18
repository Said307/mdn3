

from rest_framework import serializers

from catalog.models import Supplier,Part




   
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
    """ All validation is done here in the serializer class"""
    #supplier = SupplierSerializer(many=True, read_only=True)   # explicit nesting
    class Meta:
        model = Part
        fields = '__all__'
        #depth = 1
         
class SupplierSerializer(serializers.ModelSerializer):
    parts= serializers.HyperlinkedRelatedField(
         many=True,
        read_only=True,
        view_name='api2:part-detail')  # appname:viewname
    
    class Meta:
        model = Supplier
        fields = '__all__'
        #depth=2
       


################################  HyperLinkedModel Serializer   ####################################

""" 
class SupplierSerializer(serializers.HyperlinkedModelSerializer):
 
    url = serializers.HyperlinkedIdentityField(
        view_name='api2:supplier-detail',
        lookup_field='pk')

    parts = serializers.HyperlinkedRelatedField(
            view_name='api2:part-detail',
            many=True,read_only=True)
    
    class Meta:
        model = Supplier
        fields = '__all__'
       
        

class PartSerializer(serializers.HyperlinkedModelSerializer):              #must be call  url = 
    url = serializers.HyperlinkedIdentityField(
        view_name='api2:part-detail',
        lookup_field='pk',
       
       )
    supplier = serializers.HyperlinkedRelatedField(
           
            read_only=True,
            view_name='api2:supplier-detail')
  

    class Meta:
        model = Part
        fields = '__all__'
    """