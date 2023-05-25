
from django.urls import path

from . import views


urlpatterns = [
	path('detalhes/<int:pk>', views.ProductDetailView.as_view(), name='detail'),
	path('produtos/', views.ListProductsView.as_view(), name='products'),
	path('produtos/novidades', views.ProductFeaturedView.as_view(), name='products_featured'),
	path('produtos/<slug:slug>/', views.ProductDetailSlugView.as_view()),
	
]

