from http.client import HTTPResponse
import io
from django.shortcuts import render
from django.http import Http404,HttpResponse,HttpResponseNotFound
from rest_framework.response import Response
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics,mixins


from . import serializers

from catalog.models import *



#Parts API views
 
@api_view(['GET', 'POST', 'DELETE'])
def allparts(request):
    if request.method=='GET':
        query = Part.objects.all()
        serializer = serializers.PartSerializer(query,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        #data =JSONParser().parse(request)                                        #  wrong parser for  images/files POSt
        #data = MultiPartParser().parse(request)
        #data = FormParser().parse(request)
 
        serializer = serializers.PartSerializer(data=request.data)
     
        if serializer.is_valid():
           
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def partdetail(request,pk):
    try:
        mypart = Part.objects.get(pk=pk)
    except Part.DoesNotExist:
        raise Http404("Part does not exist")
    if request.method=='GET':
        serializer = serializers.PartSerializer(mypart)
        return Response(serializer.data)
    
    elif request.method=='DELETE':
         
        mypart.delete()
        return Response('Part number deleted succesfully',status=204)

    elif request.method=='PUT':
      
        serializer = serializers.PartSerializer(mypart,data=request.data)  #??????????????
        
        if serializer.is_valid():
            serializer.save()
            return Response('partnumber updated',status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# Supplier API views
 
@api_view(['GET', 'POST', 'DELETE'])
def allsuppliers(request):
    if request.method=='GET':
        query = Supplier.objects.all()
        serializer = serializers.SupplierSerializer(query,many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':  #  Post  with out  images or files

       
        serializer = serializers.SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('new supplier added',  status=status.HTTP_201_CREATED)
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def supplierdetail(request,pk):
    try:
        mysupplier = Supplier.objects.get(pk=pk)
    except Supplier.DoesNotExist:
        raise Http404("Poll does not exist")
    if request.method=='GET':
        serializer = serializers.SupplierSerializer(mysupplier)
        return Response(serializer.data)
    
    elif request.method=='DELETE':
         
        mysupplier.delete()
        return Response('Part number deleted succesfully',status=status.HTTP_204_NO_CONTENT)

    elif request.method=='PUT':
      
        serializer = serializers.SupplierSerializer(mysupplier,data=request.data)  #??????????????
        
        if serializer.is_valid():
            serializer.save()
            return Response('partnumber updated',status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




##########################################################################################################

############################      Class-Based  views        ##############################################


class AllpartsAPIView(APIView):

    def get(self, request):
        query = Part.objects.all()
        serializer = serializers.PartSerializer(query,many=True)
        return Response(serializer.data)

    
    def post(self,request):
        serializer = serializers.PartSerializer(data=request.data)
     
        if serializer.is_valid():
           
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PartdetailAPIView(APIView):
    pass





class AllsuppliersAPIView(APIView):
    
    def get(self,request):
        query = Supplier.objects.all()
        serializer = serializers.SupplierSerializer(query,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = serializers.SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('new supplier added',  status=status.HTTP_201_CREATED)
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)





class SupplierdetailAPIView(APIView):


    def get_object(self,id):
        try:
           
            return  Supplier.objects.get(id=id)
        except Supplier.DoesNotExist:
            raise Http404("Supplier does not exist")
        
    
    def get(self,request,id):
 
        serializer = serializers.SupplierSerializer(self.get_object(id))
        return Response(serializer.data)



    def put(self,request,id):
        serializer = serializers.SupplierSerializer(self.get_object(id),data=request.data)  
        
        if serializer.is_valid():
            serializer.save()
            return Response('Supplier updated',status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request,id):
      
        self.get_object(id).delete() 
  
        return Response('Supplier deleted succesfully',status=status.HTTP_204_NO_CONTENT)





##########################################################################################################

############################      Generic views and mixins        #########################################

class PartsListAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
                        mixins.UpdateModelMixin):
    serializer_class = serializers.PartSerializer
    queryset= Part.objects.all()

    def get(self,request):

        return self.list(request)

    def post(self,request):
        return self.create(request)
    def put(self,request,id=None):
        return self.update(request,id)






#Suppliers
class SuppliersListAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
                          mixins.UpdateModelMixin):
    serializer_class = serializers.SupplierSerializer
    queryset= Supplier.objects.all()
    lookup_field ='id'
    lookup_url_kwarg ='id'

    def get(self,request):

        return self.list(request)
    
    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
        return self.update(request,id)