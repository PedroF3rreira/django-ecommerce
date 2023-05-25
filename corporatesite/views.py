
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings



def home(request):
	return render(request, 'corporatesite/home.html')


def about(request):
	return render(request, 'corporatesite/about.html')


def contact(request):
	form = ContactForm(request.POST or None)

	context = {
		"form": form
	}

	if form.is_valid():
		name = form.cleaned_data.get("name")
		email = form.cleaned_data.get("email")
		message = form.cleaned_data.get("message")

		send_mail('Ecommerce Django', f"Olá {name} bem vindo!", settings.EMAIL_HOST_USER, [email] )

		return redirect('mail_suscess')



	return render(request, 'corporatesite/contact.html', context)

def mail_suscess(request):
	return render(request, 'corporatesite/mail_suscess.html')

