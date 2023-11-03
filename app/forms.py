from django import forms
from .models import User, App, AppTask

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'username', 'password']

class LogInForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    
class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = '__all__'
        widgets = {
            'catagory': forms.Select(choices=App.CATEGORY_CHOICES),
            'sub_catagory': forms.Select(choices=App.SUB_CATEGORY_CHOICES)
        }

class AppTaskForm(forms.ModelForm):
    class Meta:
        model = AppTask
        fields = ['screenshot']
        