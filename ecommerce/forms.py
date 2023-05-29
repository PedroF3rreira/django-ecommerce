from django.contrib.auth.forms import (
		AuthenticationForm,  
		PasswordChangeForm, 
		BaseUserCreationForm
	)
from django import forms

class RegisterUserForm(BaseUserCreationForm):
	username = forms.CharField(label="Nome de usuário", widget=forms.TextInput(attrs={"class": "form-control"}))
	password1 = forms.CharField(label = "Digite uma senha", widget=forms.PasswordInput(attrs={"class": "form-control"}))
	password2 = forms.CharField(label = "Confirmar senha", widget=forms.PasswordInput(attrs={"class": "form-control"}))


class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


class PasswordChange(PasswordChangeForm):
	old_password = forms.CharField(label = "Senha antiga",widget=forms.PasswordInput(attrs={"class": "form-control"}))
	new_password1 = forms.CharField(label = "Nova senha", widget=forms.PasswordInput(attrs={"class": "form-control"}))
	new_password2 = forms.CharField(label = "Confirmar nova senha", widget=forms.PasswordInput(attrs={"class": "form-control"}))

