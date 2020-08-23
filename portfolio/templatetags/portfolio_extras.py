from django import template

register = template.Library()

@register.filter(name='get_dict_value')
def get_dict_value(dict, key):
    return dict[key]
