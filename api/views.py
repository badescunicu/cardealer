from cardealer.models import Manufacturer, Car
from api.serializers import ManufacturerSerializer, CarSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ManufacturerList(APIView):
    """
    List all Manufacturers, or create a new one
    """
    def get(self, request, format=None):
        manufacturers = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(manufacturers, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ManufacturerSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    
class CarList(APIView):
    """
    List all cars, or create a new one
    """
    def get(self, request, format=None):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CarSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ManufacturerDetail(APIView):
    """
    Retrieve, update or delete a manufacturer instance
    """
    def get_object(self, pk):
        try:
            return Manufacturer.objects.get(pk=pk)
        except Manufacturer.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        manufacturer = self.get_object(pk)
        serializer = ManufacturerSerializer(manufacturer)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        manufacturer = self.get_object(pk)
        serializer = ManufacturerSerializer(manufacturer, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        manufacturer = self.get_object(pk)
        manufacturer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class CarDetail(APIView):
    """
    Retrieve, update or delete a car instance
    """
    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CarSerializer(car, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk ,format=None):
        car = self.get_object(pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
 