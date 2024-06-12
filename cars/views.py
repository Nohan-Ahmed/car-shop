from typing import Any
from django.shortcuts import render
from django.views.generic import DetailView
from cars.models import Car
from cars.forms import CommentForm
# Create your views here.
class CarDetailsView(DetailView):
    model = Car
    pk_url_kwarg = 'pk'
    # context_object_name='car'
    template_name = './cars/car_details.html'
    
    def get_context_data(self, **kwargs):
        car = self.get_object()
        context =  super().get_context_data(**kwargs)
        context['comments'] = car.comments.all()
        context['comment_form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.car = self.get_object()
            form.save()
            return self.get(request, *args, **kwargs)