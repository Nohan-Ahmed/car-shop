from django.shortcuts import render
from . import forms
from django.contrib.auth.models import User
# Create your views here.
def profile(request):
    users = User.objects.all()
    return render(request, './accounts/profile.html', {"data":users})

def auth(request):
    if request.method =='POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    return render(request, 'accounts/auth.html', {'form':forms.ContactForm()})