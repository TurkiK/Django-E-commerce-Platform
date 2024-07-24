# shop/templatetags/shop_tags.py
from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    """Multiplies the given value by the argument."""
    try:
        return value * arg
    except (ValueError, TypeError):
        return ''
