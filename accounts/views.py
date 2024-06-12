from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from . import forms
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import ListView, UpdateView
from django.contrib import messages
from orders.models import Order
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required, name='dispatch')
class ProfileView(ListView):
    model= Order
    template_name = './accounts/profile.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(customer=self.request.user)
        return context

@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    form_class = forms.UpdateProfileForm
    template_name = './accounts/auth.html'
    success_url = reverse_lazy('profile')
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['type'] = 'Update profile'
        return context
    
    def get_object(self, queryset: QuerySet=None):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Your profile updated successfully.')
        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')
class PasswordChange(PasswordChangeView):
    template_name = './accounts/auth.html'
    success_url = reverse_lazy('profile')

def singup(request):
    if request.method =='POST':
        form = forms.CreateUser(request.POST)
        if form.is_valid():
            messages.success(request, message="Account created successfully!")
            form.save(commit=False)
            return redirect('singup')
    else:
        form = forms.CreateUser()
    return render(request, './accounts/auth.html', { 'form':form, 'type':'Sing-up'})

class UserLoginView(LoginView):
    template_name = './accounts/auth.html'
    
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, message='Logged in Successful!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_success_url(self) -> str:
        return reverse_lazy('profile')
    
def user_logout(request):
    logout(request)
    return redirect('login')