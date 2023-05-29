from django.contrib.auth.forms import AuthenticationForm,  PasswordChangeForm
from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


class PasswordChange(PasswordChangeForm):
	old_password = forms.CharField(label = "Senha antiga",widget=forms.PasswordInput(attrs={"class": "form-control"}))
	new_password1 = forms.CharField(label = "Nova senha", widget=forms.PasswordInput(attrs={"class": "form-control"}))
	new_password2 = forms.CharField(label = "Confirmar nova senha", widget=forms.PasswordInput(attrs={"class": "form-control"}))