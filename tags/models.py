from django.db import models
from products.models import Product
from products.utils import slug_unique_generator
from django.db.models.signals import pre_save

class Tag(models.Model):
	name = models.CharField(max_length=120)
	slug = models.SlugField(blank = True)
	timestamp = models.DateTimeField(auto_now_add = True)
	active = models.BooleanField(default = True)
	products = models.ManyToManyField(Product, blank = True)


	def __str__(self):
		return self.name


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slug_unique_generator(instance)

pre_save.connect(tag_pre_save_receiver, sender = Tag)
