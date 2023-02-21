
from django.template.defaultfilters import slugify
from  rest_framework import serializers  



from product.models import *


class DeliveryTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model= DeliveryType
        fields = '__all__'

class ProductQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model= ProductQuestion
        fields = '__all__'

class ProductReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model= ProductReview
        fields = '__all__'

 
class ProductSerializer(serializers.ModelSerializer):
    
    total_price = serializers.SerializerMethodField('get_total_price')
    tags = serializers.SerializerMethodField('get_tags')
    seller = serializers.SerializerMethodField('get_seller')
    rating = serializers.DecimalField(max_digits=10,decimal_places=2,source='get_rating',read_only=True)
    #delivery_type = DeliveryTypeSerializer(read_only=True)              # shows nested record
    delivery_type = serializers.PrimaryKeyRelatedField(read_only=True)  # shows FK only
    questions = ProductQuestionSerializer(read_only=True, many=True)
    reviews = ProductReviewSerializer(read_only=True, many=True)

    class Meta:
        model= Product
        fields = '__all__'
 
    

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def get_total_price(self, obj):
        if obj.discount and obj.price:
            discount_amount = (obj.price * obj.discount) / 100
            total_price = round(obj.price - discount_amount, 2)
            return total_price
        return obj.price
    
    def get_tags(self, obj):
        if obj.tags:
            tags = []
            for tag in obj.tags.all():
                tags.append(tag.title)
            return tags
        return None
    
    def get_seller(self, obj):
        if obj.seller:
            return {
                'id': obj.seller.id,
                'email': obj.seller.email,
                'first_name': obj.seller.first_name,
                'last_name': obj.seller.last_name,
            }
        return None



 
class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model= ProductImage
        fields= '__all__'
 

    def update(self,validated_data,instance):

        instance.image = validated_data.get('image',instance.email)
        instance.save()
        return instance



class ProductQuestionSerializer(serializers.ModelSerializer):  

    class Meta:
        model = ProductQuestion
        fields ='__all__'





class BrowsingHistorySerializer(serializers.ModelSerializer):
    #products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = BrowsingHistory
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = ProductImage
        fields = '__all__'
