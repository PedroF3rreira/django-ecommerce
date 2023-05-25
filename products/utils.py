from django.utils.text import slugify
import random
import string

def slug_unique_generator(instance, new_slug=None):
	if new_slug is not None:
		slug = new_slug
	else:
		slug = slugify(instance.name)

	klass = instance.__class__
	qs_exists = klass.objects.filter(slug = slug).exists()
	if qs_exists:
		new_slug = "{slug}-{randstr}".format(slug = slug, randstr = random_string_generator(size=4) )
		return slug_unique_generator(instance, new_slug = new_slug)
	return slug
	
