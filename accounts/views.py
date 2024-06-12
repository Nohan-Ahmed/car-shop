from django.shortcuts import render, redirect
from . import forms
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
# Create your views here.
def profile(request):
    users = User.objects.all()
    return render(request, './accounts/profile.html', {"data":users})

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