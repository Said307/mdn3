from django.shortcuts import render
from django.http import Http404,HttpResponse,HttpResponseNotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from rest_framework.generics import ListAPIView
from rest_framework import filters

from product.models import *
from .serializers import *




class ProductListAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated] 

    def get(self,request):

        query= Product.objects.all()
        serializer = ProductSerializer(query,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save(seller=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated] 


    def get_object(self,id):
        try:
           
            return  Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404("Supplier does not exist")
        
    
    def get(self,request,pk,*args,**kwargs):
        """ serialize one particular object"""
        serializer = ProductSerializer(self.get_object(pk))
        return Response(serializer.data)
    
    def put(self,requets,pk,*args,**kwargs):
        serializer = ProductSerializer(self.get_object(id=pk),data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(f'product nr {pk} updated',status=status.HTTP_201_CREATED) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):

        object = self.get_object(pk)
        return Response('Part deleted succesfullly',status=status.HTTP_204_NO_CONTENT)




class CurrentUserProductsListAPIView(ListAPIView):

     
    query_set = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
         products = Product.objects.filter(seller=self.request.user)
         
         return products


class UserProductsListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = [filters.DjangoFilterBackend]
    

    def get_queryset(self):
        print(self.kwargs)
        print(self.request.query_params)
        products = Product.objects.filter(seller__username=self.kwargs['username'])
        return products
    






#####################################################################

class ProductImageCreateAPIView(APIView):  
    permission_classes = [permissions.IsAuthenticated] 

    
    def get_object(self,id):
        try:
           
            return  ProductImage.objects.get(id=id)
        except ProductImage.DoesNotExist:
            raise Http404("image does not exist")

    def post(self,request):
        serializer = ProductImageSerializer(data=request.data)
        if  serializer.is_valid():
            serializer.save()
          
            return Response(f'new image uploaded',status=status.HTTP_201_CREATED) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request):
     
        pk = self.request.data['pk']
        image=  self.get_object(id=pk)
        serializer = ProductImageSerializer(image,data=request.data,context={'request':request})
        if  serializer.is_valid(raise_exception=True):
     
          
            serializer.save()
           
            return Response(f'image updated',status=status.HTTP_201_CREATED) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
 
    
class ProductImageDeleteAPIView(APIView):  
    permission_classes = [permissions.IsAuthenticated] 

    def get_object(self,id):
        try:
           
            return  ProductImage.objects.get(id=id)
        except ProductImage.DoesNotExist:
            raise Http404("image does not exist")

    def delete(self,request,id):
        image= self.get_object(id=id)
        return Response("Image deleted",status=status.HTTP_204_NO_CONTENT)


class BrowsingAPIView(APIView):

    #permission_classes = [permissions.IsAuthenticated] 

    def get(self,request):

        query= BrowsingHistory.objects.all()
        serializer = BrowsingHistorySerializer(query,many=True)
        return Response(serializer.data)



class ProductQuestionsAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated] 

    def get(self,request):

        query= ProductQuestion.objects.all()
        serializer = ProductQuestionSerializer(query,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(author=self.request.user):
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)