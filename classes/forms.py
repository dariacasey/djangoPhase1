from django import forms
from .models import Class


class ClassCreationForm(forms.Form):
    class_name = forms.CharField(max_length=255)


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name']


class JoinClass(forms.Form):
    class_code = forms.CharField(label='Class Code', max_length=100)