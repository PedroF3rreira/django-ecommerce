from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'description', 'slug', 'price', 'image', 'featured', 'active']


	class meta:
		model=Product


admin.site.register(Product, ProductAdmin)