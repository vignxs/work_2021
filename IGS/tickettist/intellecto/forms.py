# from dataclasses import fields
# from tkinter import Widget
from django.forms import ModelForm, widgets
from django import forms
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets ={
            'UserName' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'Email' : forms.EmailInput(attrs = {'class' : 'form-control'}),
            'MobileNumber' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'IsProjectStarted' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'Description' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'Status' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'CreatedOn' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'UpdatedOn' : forms.TextInput(attrs = {'class' : 'form-control'})
        } 