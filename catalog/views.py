from rest_framework import generics

from catalog.models import Vehicle, Category
from catalog.serializers import VehicleSerializer, CategorySerializer


""" Vehicle views using specific generics heritage """

class VehicleList(generics.ListCreateAPIView):
    """ 
    Vehicle List Create view. 
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    

class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    """ 
    Vehicle Retrieve Update Destroy view.
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

""" Category views using specific generics heritage """

class CategoryList(generics.ListCreateAPIView):
    """ 
    Category List Create view. 
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """ 
    Category Retrieve Update Destroy view.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer