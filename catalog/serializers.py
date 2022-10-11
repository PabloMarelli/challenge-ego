from rest_framework import serializers
from catalog.models import Vehicle, Category


class VehicleSerializer(serializers.Serializer):
    
    class Meta:
        model = Vehicle
        fields = '__all__'
        

class CategorySerializer(serializers.Serializer):
    
    class Meta:
        model = Category
        fields = '__all__'
        