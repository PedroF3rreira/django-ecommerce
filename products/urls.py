
from django.urls import path

from . import views

# define namespace das rotas
app_name = "products"

urlpatterns = [
	#path('detalhes/<int:pk>', views.ProductDetailView.as_view(), name='detail'),
	path('', views.ListProductsView.as_view(), name='index'),
	path('novidades/', views.ProductFeaturedView.as_view(), name='featured'),
	path('<slug:slug>/', views.ProductDetailSlugView.as_view(), name='detail'),
	
]

