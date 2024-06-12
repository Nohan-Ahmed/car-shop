from typing import Any
from django.shortcuts import render, redirect
from cars.models import Car
from brands.models import Brand

def home(request, slug=None):
    brands = Brand.objects.all()
    cars = Car.objects.all()
    if slug is not None:
        brand = Brand.objects.get(slug=slug)
        cars = Car.objects.filter(brand=brand)
        
    return render(request, './index.html', {'brands':brands, 'cars':cars})