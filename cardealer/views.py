from django.shortcuts import render_to_response
from cardealer.models import Manufacturer, Car
from django.views.generic import ListView
from django.http import Http404

def home(request):
    return render_to_response('index.html')

def list_all_cars(request):
    title = 'Available cars'
    cars = Car.objects.all()
    context = {
        'cars': cars,
        'title': title,
    }
    return render_to_response('list_cars.html', context)


class ListCars(ListView):
    model = Car
    template_name = 'list_cars.html'
    context_object_name = 'cars'
    
    
    
    