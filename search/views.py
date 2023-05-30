from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product


class SearchProductView(ListView):
	template_name = "products/list.html"
	context_object_name = "products"
	
	def get_queryset(self, *args, **kwargs):
		request = self.request
		result = request.GET
		busca = result.get('q')
		
		if busca is not None:
			return Product.objects.filter(name__icontains=busca)

		return Product.objects.featured()
