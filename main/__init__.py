import os
from django import template

reg = template.Library()


@reg.filter
def filename(value):
    return os.path.basename(value)

