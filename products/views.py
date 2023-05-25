from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product


class ProductFeaturedView(generic.ListView):
	template_name = 'products/products_featureds.html'
	context_object_name = 'products'

	def get_queryset(self):
		return Product.objects.all().featured()


class ListProductsView(generic.ListView):
	template_name = 'products/list.html'
	context_object_name = 'products'
	
	def get_queryset(self):
		return Product.objects.all()


class ProductDetailView(generic.DetailView):
	template_name = 'products/detail.html'
	context_object_name = 'product'
	

	def get_object(self, *args, **kwargs):
		pk = self.kwargs.get('pk')
		instance = Product.objects.get_by_id(pk=pk)
		if instance is None:
			raise Http404("esse produto não existe")
		return instance


class ProductDetailSlugView(generic.DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'
    context_object_name = 'product'

    def get_object(self, *args, **kwargs):
    	slug = self.kwargs.get('slug')
    	try:
    		instance = Product.objects.get(slug=slug, active=True)# retorna os objetos
    	except Product.DoesNotExits: 
    		raise Http404("Produto não encontrado")
    	except Product.MultipleObjectsReturned:
    		qs = Product.objects.filter(slug=slug, active=True) # retorna um queryset
    		instance = qs.first()
    	return instance