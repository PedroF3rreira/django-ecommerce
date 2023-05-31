from django.urls import path

from products.views import (
		ListProductsView
	)
from .views import SearchProductView

app_name = 'busca'

urlpatterns = [
	path('', SearchProductView.as_view(), name="query")
]	