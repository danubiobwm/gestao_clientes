from django import template

register = template.library()

@register.filter
def my_filter(data):
    return data + ' - ' + 'Alterado pelo filter'

@register.filter
def arredonda(value, casas):
    return round (value, casas)