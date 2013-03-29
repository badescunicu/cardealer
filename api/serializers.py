from rest_framework import serializers
from cardealer.models import Manufacturer, Car

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('name', 'founder', 'number_of_employees', 'date_founded')
        

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('name', 'manufacturer', 'mileage', 'fabrication_date',
                  'price', 'photo')