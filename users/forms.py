from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta: 
        model = User
        fields = (
            "first_name", 
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    # password1 = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField()
    # password2 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField()
    



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label = 'Name', 
        widget=forms.TextInput(attrs={"autofocus" : True,
                                      'class':'form-control',
                                      "placeholder":"Enter username", 
                                      }))
    password = forms.CharField(
        label = 'Password', 
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          'class':'form-control',
                                          'placeholder':'Enter your password'})
    )
    class Meta: 
        model = User    

class ProfileForm(UserChangeForm):
    class Meta: 
        model = User
        fields = (
            "image", 
            "first_name", 
            "last_name",
            "username",
            "email",
        )

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name= forms.CharField()
    username = forms.CharField() 
    email = forms.CharField()
    # image = forms.ImageField(
    #     widget=forms.FileInput(attrs={
    #         "class": "form-control mt-3"
    #     }), required=False
    # )