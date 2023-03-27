from django.shortcuts import render
from rest_framework import generics 
from .serializers import HomeSerializer
from .models import Home

# Create your views here.
class HomeList(generics.ListCreateAPIView):
    queryset = Home.objects.all().order_by('-created_at')[:4]
    serializer_class = HomeSerializer

class AllHomesList(generics.ListCreateAPIView):
    queryset = Home.objects.all().order_by('id')
    serializer_class = HomeSerializer

class HomeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Home.objects.all().order_by('id')
    serializer_class = HomeSerializer 