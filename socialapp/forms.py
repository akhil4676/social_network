from cProfile import label
from operator import attrgetter
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from socialapp.models import Posts

from django import forms

class RegistrationForm(UserCreationForm):

    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}),label="PASSWORD1")
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}),label="PASSWORD2")

    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
        }
        labels={
            "first_name":"FIRST NAME",
            "last_name":"LAST NAME",
            "username":"USERNAME",
            "email":"EMAIL",
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),label="USERNAME")
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}),label="PASSWORD")

class PostsForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["post","image"]
        widgets={
            "post":forms.Textarea(attrs={"class":"form-control","rows":3}),
            "image":forms.FileInput(attrs={"class":"form-select"}),
        }
        labels={
            "post":"POST",
            "image":"IMAGE",
        }