from django import template

register = template.Library()

@register.filter
def limit(items, count):
    return items[:count]
