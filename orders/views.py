from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Order
from cars.models import Car
from .forms import OrderForm
from django.contrib import messages
# Create your views here.
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = './orders/order.html'
    pk_url_kwarg='pk'

    def get_success_url(self) -> str:
        return reverse_lazy('home')

    def form_valid(self, form):
        form.instance.customer=self.request.user
        form.instance.car = self.get_object()
        return super().form_valid(form)


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
    except:
        messages.warning(request, message='Not enough stock available for the requested car!')
        return render(request, './orders/order.html', {
            'form': form,
            'car': car
        })
