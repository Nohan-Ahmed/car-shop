from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Enter your Name:")
    email = forms.EmailField()
    age = forms.IntegerField()
    height = forms.DecimalField()
    balance = forms.FloatField()
    check = forms.BooleanField()
    brithDate = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'date'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    choices = forms.ChoiceField(choices=CHOICES)
    MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    meal = forms.MultipleChoiceField(choices=MEAL)