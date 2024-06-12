from django.shortcuts import render
from django.views.generic import DetailView
from cars.models import Car
# Create your views here.
class CarDetailsView(DetailView):
    model = Car
    pk_url_kwarg = 'pk'
    template_name = './cars/car_details.html'