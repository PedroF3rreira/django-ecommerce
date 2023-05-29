"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import loginUser, LogoutView, PasswordChange, registerUser

urlpatterns = [
    path('', include('corporatesite.urls')),
    path('produtos/', include('products.urls',  namespace="products")),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('contas/login/', loginUser, name='login'),
    path('contas/logout/', LogoutView.as_view(), name='logout'),
    path('contas/alterar/senha', PasswordChange.as_view(), name='changer_password'),
    path('contas/registrar/', registerUser, name='register'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)