from http.client import HTTPResponse
import io
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponse,HttpResponseNotFound
from rest_framework.response import Response
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics,mixins
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication, SessionAuthentication,TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import viewsets
from rest_framework.authtoken.models import Token

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
   # authentication_classes = [BasicAuthentication,SessionAuthentication,]
 
    #authentication_classes=[TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated] 
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
    
    def get_object(self,pk):
        try:
           
            object = Part.objects.get(pk=pk)
        except Part.DoesNotExist:
            raise Http404("Part not exist")
        return object
    
    def get(self,request,pk):
        object= self.get_object(pk)
        serializer = serializers.PartSerializer(object)
        return Response(serializer.data)

    def put(self,request,id):
        serializer = serializers.PartSerializer(self.get_object(id),data=request.data)  
        
        if serializer.is_valid():
            serializer.save()
            return Response('Part updated',status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request,id):
      
        self.get_object(id).delete() 
  
        return Response('Part deleted succesfully',status=status.HTTP_204_NO_CONTENT)





class AllsuppliersAPIView(APIView):
    #authentication_classes = [BasicAuthentication,SessionAuthentication,]
    #authentication_classes=[TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated] 
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
        
    
    def get(self,request,id,*args,**kwargs):
       
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

############################      Generic views with mixins        #########################################

class PartsListAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
                        mixins.UpdateModelMixin):
    serializer_class = serializers.PartSerializer
    queryset= Part.objects.all()

    def get(self, request, *args, **kwargs):
      
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class RetrieveUpdateDeletePart(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):

    serializer_class = serializers.PartSerializer
    queryset = Part.objects.all()

    def get(self, request, *args, **kwargs):
      
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




#Suppliers
class SuppliersListAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
                          mixins.UpdateModelMixin):
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]                      
    serializer_class = serializers.SupplierSerializer
    queryset= Supplier.objects.all()
  
 
    def get(self, request, *args, **kwargs):
    
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RetrieveUpdateDeleteSupplier(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):

    serializer_class = serializers.SupplierSerializer
    queryset = Supplier.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


##########################################################################################################

############################      Generic views with no mixin      #########################################


 

class GenericSupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer
    authentication_classes = [BasicAuthentication,SessionAuthentication]  # THese 2 are default setting
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    # def get_queryset(self):
    #     last_two_days = now() - timedelta(days=2)
    #     return Question.objects.filter(pub_date__gt=last_two_days)
    # def list(self, request):
    #      Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)
    

class GenericSupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer
    #authentication_classes = [BasicAuthentication,]
    permission_classes =  [permissions.IsAuthenticated]





##########################################################################################################

############################     Viewsets      #########################################



class SupplierViewset(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions. """

    queryset =  Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer 
    permission_classes =  [permissions.IsAuthenticated]

    #def perform_create(self, serializer):
        #serializer.save(owner=self.request.user)




class PartsViewset(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions. """

    queryset =  Part.objects.all()
    serializer_class = serializers.PartSerializer
    permission_classes =  [permissions.IsAuthenticated]
