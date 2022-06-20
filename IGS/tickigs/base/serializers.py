from rest_framework import serializers

from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = '__all__'
        # depth = 1

class TechnologySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Technology
        fields = '__all__'
        # depth = 1