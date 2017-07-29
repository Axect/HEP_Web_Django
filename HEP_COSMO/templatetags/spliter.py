from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='split')
def split(string, sep):
    """Return the string split by sep.

    Example usage: {{ value|split:"," }}
    """
    return string.split(sep)

@register.filter
def is_in(var, obj):
    return var in obj

@register.filter(name='strip')
@stringfilter
def strip(string):
    return string.strip()