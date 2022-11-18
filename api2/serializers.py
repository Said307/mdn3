

from rest_framework import serializers

from catalog.models import Supplier




class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = '__all__'











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