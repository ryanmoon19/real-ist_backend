from django.shortcuts import render
from rest_framework import generics 
from .serializers import HomeSerializer
from .models import Home
from rest_framework.views import APIView
from apps.accounts.permissions import CustomPermission



# Create your views here.
class MyView(APIView):
    permission_classes = [CustomPermission]

class HomeList(generics.ListCreateAPIView):
    queryset = Home.objects.all().order_by('-created_at')[:4]
    serializer_class = HomeSerializer
    permission_classes = [CustomPermission]

class AllHomesList(generics.ListCreateAPIView):
    queryset = Home.objects.all().order_by('id')
    serializer_class = HomeSerializer
    permission_classes = [CustomPermission]

class HomeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Home.objects.all().order_by('id')
    serializer_class = HomeSerializer 
    permission_classes = [CustomPermission]
