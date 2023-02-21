




from django.views.generic.base import TemplateView
from django.urls import path,include

from.views import *
 


app_name = "product"

urlpatterns=[
    
    
    path('products/', ProductListAPIView.as_view(), name='products'),
    path('products/<int:pk>', ProductDetailAPIView.as_view(), name='product-detail'),
    #path('products/my/', CurrentUserProductsListAPIView.as_view(), name='my_products'),
    #path('products/user/<str:username>/', UserProductsListAPIView.as_view(), name='user_products'),
    path('products/image-upload/', ProductImageCreateAPIView.as_view(), name='product_image_create'),
    path('products/image-delete/<int:id>/', ProductImageDeleteAPIView.as_view(), name='product_image_delete'),

    path('browsinghistory/', BrowsingAPIView.as_view(), name='categories'),
    path('questions/', ProductQuestionsAPIView.as_view(), name='questions'),



]