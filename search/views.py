from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product


class SearchProductView(ListView):
	template_name = "search/view.html"
	context_object_name = "products"
	
	def get_queryset(self, *args, **kwargs):
		request = self.request
		result = request.GET
		query = result.get('q')
		
		if query is not None:
			return Product.objects.search(query)

		return Product.objects.featured()
