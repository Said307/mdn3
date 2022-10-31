



from rest_framework import serializers
from catalog.models import *
 
 
class PartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Part
        fields= '__all__'


 
class SupplierSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Supplier
        fields= '__all__'