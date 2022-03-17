from django.shortcuts import render

from .models import Supers
from .serializers import SupersSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SupersList(APIView):
    #Gets all Supers
    def get(self, request, format=None):
        supers = Supers.objects.all()
        serializer = SupersSerializer(supers, many=True)
        return Response(serializer.data)
    
    #Creates Super
    def post(self, request, format=None):
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

class SupersDetail(APIView):
    def print(self, request, format=None):
        print('1')