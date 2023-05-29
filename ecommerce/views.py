from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from .forms import LoginForm, PasswordChange, RegisterUserForm
from  django.contrib.auth.models import User
from django.urls import reverse

# class LoginUser(auth_views.LoginView):
# 	template_name = 'auth/login.html'
# 	authentication_form = LoginForm
	
# 	next_page = '/'

def registerUser(request):
	form = RegisterUserForm(request.POST or None)

	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')

		user = User.objects.create_user(username=username, password=password)
		user.save()
		
		return redirect('login')
	

	return render(request, 'auth/register.html', {"form": form})

def loginUser(request):

	form = LoginForm(request.POST or None)

	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(request, username=username, password=password)

		if user is not None: 
			login(request, user)
			if user.is_superuser:
				return redirect('/admin')
			else:
				return redirect('/')
		else:
			messages.info(request, "Erro ao efetuar login verifique usuario e senha")
			return redirect(reverse('login'))
		
	return render(request, 'auth/login.html', {"form" : LoginForm})

class LogoutView(auth_views.LogoutView):
	template_name = 'auth/logout.html'


class PasswordChange(auth_views.PasswordChangeView):
	template_name = 'auth/password_changer.html'
	form_class = PasswordChange


# class RegisterView(auth_views.RegisterView):
# 	template_name = 'auth/login.html'

		


