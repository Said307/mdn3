from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User

from .serializers import *

class UserView(APIView):

    #permission_classes = [permissions.IsAuthenticated] 

    def get(self,request):

        query= User.objects.all()
        serializer = UserSerializer(query,many=True)
        return Response(serializer.data)



