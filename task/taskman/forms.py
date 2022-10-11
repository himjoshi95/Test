from django import forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError



class UserRegisterForm(UserCreationForm):
    
    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
       return self.cleaned_data

  
    class Meta:
        model = User
        fields = ['username', 'email' ,'password1', 'password2']

class UserLoginForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email' ,'password1']

