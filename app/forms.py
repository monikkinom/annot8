from django.contrib.auth.models import User
from django import forms
from app.models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = "form-control input-md"
        self.fields['password'].widget.attrs['class'] = "form-control input-md"
        self.fields['email'].widget.attrs['class'] = "form-control input-md"
        self.fields['username'].widget.attrs['placeholder'] = "Username"
        self.fields['password'].widget.attrs['placeholder'] = "Password"
        self.fields['email'].widget.attrs['placeholder'] = "Email"
        self.fields['username'].widget.attrs['required'] = "yes"
        self.fields['password'].widget.attrs['required'] = "yes"
        self.fields['email'].widget.attrs['required'] = "yes"

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CodeForm(forms.ModelForm):
    code = forms.Textarea()
    def __init__(self, *args, **kwargs):
        super(CodeForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = "form-control input-md"
        self.fields['code'].widget.attrs['class'] = "form-control input-md"
        self.fields['language'].widget.attrs['class'] = "form-control input-md"
        self.fields['title'].widget.attrs['placeholder'] = "Title"
        self.fields['code'].widget.attrs['placeholder'] = "Text"
        self.fields['language'].widget.attrs['placeholder'] = "Language"
        self.fields['title'].widget.attrs['required'] = "yes"
        self.fields['code'].widget.attrs['required'] = "yes"
        self.fields['language'].widget.attrs['required'] = "yes"
    class Meta:
        model = Code
        fields = ['title','code','language']