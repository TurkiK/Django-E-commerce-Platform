# shop/templatetags/shop_tags.py
from django import template
from django.urls import resolve

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    """Multiplies the given value by the argument."""
    try:
        return value * arg
    except (ValueError, TypeError):
        return ''

register = template.Library()

@register.simple_tag(takes_context=True)
def current_page(context):
    request = context['request']
    return resolve(request.path_info).url_name