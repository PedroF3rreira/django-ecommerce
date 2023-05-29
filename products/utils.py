import random
import string

from django.utils.text import slugify
# gera uma string aleatória
def random_string_generator(size=10, chars = string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


def slug_unique_generator(instance, new_slug=None):
	if new_slug is not None:
		slug = new_slug
	else:
		slug = slugify(instance.name)

	klass = instance.__class__ # pega o nome da class da instancia
	qs_exists = klass.objects.filter(slug = slug).exists() # verifica se o slug já existe no db
	if qs_exists:
		new_slug = "{slug}-{randstr}".format(slug = slug, randstr = random_string_generator(size=4) )
		return slug_unique_generator(instance, new_slug = new_slug)
	return slug
	
