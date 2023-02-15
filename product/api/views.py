from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


from product.models import *
from .serializers import *




class ProductListAPIView(APIView):

    #permission_classes = [permissions.IsAuthenticated] 

    def get(self,request):

        query= Product.objects.all()
        serializer = ProductSerializer(query,many=True)
        return Response(serializer.data)


