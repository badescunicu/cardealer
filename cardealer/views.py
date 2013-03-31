from django.shortcuts import render_to_response
from cardealer.models import Manufacturer, Car
from django.views.generic import ListView
from django.http import Http404

def home(request):
    return render_to_response('index.html')


class ListCars(ListView):
    model = Car
    template_name = 'list_cars.html'
    context_object_name = 'cars'
    