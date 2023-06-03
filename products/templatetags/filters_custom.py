from django import template
register = template.Library()


def divide_values(value, divider=10):
		result = value / int(divider)
		return str(format(result, '.2f')).replace('.',',')


register.filter("divide_values", divide_values)