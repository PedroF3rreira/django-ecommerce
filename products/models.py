from django.db import models
from .utils import sluni_unique_generator
from django.db.models.signals import pre_save

# custom queryset usado para alterar comportamentoi padrão do queryset retornado pelo manager
class ProductQuerySet(models.QuerySet):
	
	def active(self):
		return self.filter(active = True)


	def featured(self):
		return self.filter(featured = True)

"""
esta tecnica pode ser usada por exemplo para termos métodos que retornem os produtos
pela sua categoria tipo Product.eletronics_objects.all(), Product.plates_objects.all() etc...

"""

# usuando custom managers para adicionar métodos de busca extras ao db no modelo
class ProductManager(models.Manager):
	
	# método extra adicionado
	def get_by_id(self, pk):
		qs = self.get_queryset().filter(id=pk)
		if qs.count() == 1:# método count() usuado para saber se algo foi encontrado
			return qs.first()
		return None

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
	slug = models.SlugField(max_length=30, default='slug', unique=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=20, decimal_places=2, default=10.00)
	image = models.ImageField(upload_to='products/', blank=True, null=True)
	featured = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	

	objects = ProductManager()
	# eletronics_objects = ProductEletronicsManager()
	def __str__(self):
		return self.name


def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
	pre_save.connect(product_pre_save_receiver, sender = Product)

