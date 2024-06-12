from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Order
from cars.models import Car
from .forms import OrderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@login_required
def order_view(request, pk=None):
    try:
        if pk:
            car = Car.objects.get(pk=pk)
        else:
            car = None

        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                form.instance.customer = request.user
                form.instance.car = car
                form.save()
                return redirect('home')
        else:
            form = OrderForm()
        return render(request, './orders/order.html', {
            'form': form,
            'car': car
        })
    except ValueError:
        messages.warning(request, message='Not enough stock available for the requested car!')
        return render(request, './orders/order.html', {
            'form': form,
            'car': car
        })
