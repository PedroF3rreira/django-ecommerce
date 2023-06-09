from django.db.models import Q
from django.db import models
from .utils import slug_unique_generator
from django.db.models.signals import pre_save

from django.urls import reverse

# custom queryset usado para alterar comportamento padrão do queryset retornado pelo manager
class ProductQuerySet(models.QuerySet):
	
	def active(self):
		return self.filter(active = True)


	def featured(self):
		return self.filter(featured = True)

	# método queryset para busca produtos por varios campos com Q lookups
	def search(self, query):
		lookups = Q(name__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query) | Q(tag__name__icontains=query)
		return self.filter(lookups).distinct()


"""
esta tecnica pode ser usada por exemplo para termos métodos que retornem os produtos
pela sua categoria tipo Product.eletronics_objects.all(), Product.plates_objects.all() etc...

"""

# usuando custom managers para adicionar métodos de busca extras ao db no modelo
class ProductManager(models.Manager):
	
	# método extra adicionado
	def get_by_id(self, pk):
		qs = self.get_queryset().filter(id=pk)
		if qs.count() == 1:# método count() usado para saber se algo foi encontrado
			return qs.first()
		return None

	# método extra adicionado
	def search(self, query):
		return self.get_queryset().active().search(query)

	
	#sobrescrevendo o método get_queryset do manager para retornar o qs custom ProductQuerySet
	def get_queryset(self):
		return ProductQuerySet(self.model, using = self._db)

	# metodo sobreescrito
	def all(self):
		# retorna get_queryset().filter(active = True)
		return self.get_queryset().active()

	# novo método
	def featured(self):
		# retorna get_queryset().filter(fetured = True) 
		return self.get_queryset().featured()


class Product(models.Model):
	name = models.CharField(max_length=150)
	slug = models.SlugField(max_length=30, default='', unique=True, blank=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=20, decimal_places=2, default=10.00)
	image = models.ImageField(upload_to='products/', blank=True, null=True)
	featured = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	
	# definindo um manager personalizado para o model Product
	objects = ProductManager()
	# eletronics_objects = ProductEletronicsManager()
	

	def __str__(self):
		return self.name

	# pega url do produto
	def get_absolut_url(self):
		#return '/produtos/{slug}/'.format(slug = self.slug) hard code
		return reverse("products:detail", kwargs={"slug": self.slug})



def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slug_unique_generator(instance)

# sinal antes de salvar o registro executa o método para gerar um slug unica
pre_save.connect(product_pre_save_receiver, sender = Product)

