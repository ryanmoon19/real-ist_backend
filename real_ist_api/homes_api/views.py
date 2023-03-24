from django.shortcuts import render
from rest_framework import generics 
from .serializers import HomeSerializer
from .models import Home

# Create your views here.
class HomeList(generics.ListCreateAPIView):
    queryset = Home.objects.all().order_by('id')
    serializer_class = HomeSerializer

class HomeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Home.objects.all().order_by('id')
    serializer_class = HomeSerializer 