from django import template
from Yohann.models import Category


register = template.Library()

@register.inclusion_tag('Yohann/cats.html')
def get_category_list():
    return {'cats': Category.objects.all(),'act_cat': cat}