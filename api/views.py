from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from cardealer.models import Manufacturer, Car
from api.serializers import ManufacturerSerializer, CarSerializer

class ManufacturerList(generics.ListCreateAPIView):
    model = Manufacturer
    serializer_class = ManufacturerSerializer


class ManufacturerDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Manufacturer
    serializer_class = ManufacturerSerializer 
    
    
class CarList(generics.ListCreateAPIView):
    model = Car
    serializer_class = CarSerializer
    

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Car
    serializer_class = CarSerializer
 