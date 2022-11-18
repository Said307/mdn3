from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics,permissions
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.reverse import reverse
from rest_framework import viewsets
from .serializers import *






# API Root

@api_view(['GET'])
def api_root(request):
    return Response({ 'Suppliers':reverse('api2:SupplierList',request=request),
     'Supplier Detail':reverse('api2:SupplierDetails',request=request,kwargs={'pk':'id'}),   }) 



class SupplierListView(APIView):


    def get(self,request):

        suppliers = Supplier.objects.all()
        serializer = SupplierSerializer(suppliers,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer =  SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response('all done',status=status.HTTP_201_CREATED)


class SupplierDetailView(APIView):


    def get_object(self,pk):
        try:
            return Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        supplier = self.get_object(pk)
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data)

    
    def put(self,request,pk):
        supplier =self.get_object(pk)
        serializer = SupplierSerializer(supplier,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Updated',status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):

        self.get_object.delete()
        return Response("Supplier deleted",status=status.HTTP_204_NO_CONTENT)





##########################################################################################################

############################      Generic views with no mixin      #########################################


class GenericSupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    authentication_classes = [BasicAuthentication,SessionAuthentication]  # THese 2 are default setting
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GenericSupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Supplier.objects.all()
    serializer_class = SupplierSerializer
    #authentication_classes = [BasicAuthentication,]
    permission_classes =  [permissions.IsAuthenticated]



##########################################################################################################

############################     Viewsets      #########################################



class SupplierViewset(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions. """

    queryset =  Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes =  [permissions.IsAuthenticated]

   
    


    #def perform_create(self, serializer):
        #serializer.save(owner=self.request.user)