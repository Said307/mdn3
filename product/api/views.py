from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from product.models import *
from .serializers import *




class ProductListAPIView(APIView):

    #permission_classes = [permissions.IsAuthenticated] 

    def get(self,request):

        query= Product.objects.all()
        serializer = ProductSerializer(query,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
           
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class BrowsingAPIView(APIView):

    #permission_classes = [permissions.IsAuthenticated] 

    def get(self,request):

        query= BrowsingHistory.objects.all()
        serializer = BrowsingHistorySerializer(query,many=True)
        return Response(serializer.data)


