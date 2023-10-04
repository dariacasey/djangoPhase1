from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    is_teacher = forms.BooleanField(required=False, label='I am a Teacher')
    is_student = forms.BooleanField(required=False, label='I am a Student')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name',
                  'last_name', 'is_student', 'is_teacher')
