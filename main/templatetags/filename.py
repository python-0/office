import os
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def get_filename(value):
    print(os.path.basename(value))
    return os.path.basename(value)

