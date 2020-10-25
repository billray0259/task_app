from django import forms
from django.forms import ModelForm, Form
from .models import User, Task
from django.core.exceptions import ValidationError

class SignUpForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password"]

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise ValidationError("That username is taken")
        return username

class LoginForm(Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "period"]
    