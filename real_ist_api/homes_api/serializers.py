from rest_framework import serializers
from .models import Home

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ('id', 'houseNum', 'street', 'city', 'state', 'zip', 'price', 'bedroom', 'bathroom', 'description', 'squareFeet', 'image')