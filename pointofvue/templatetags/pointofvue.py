from django import template
from ..context import VueContext

register = template.Library()


@register.inclusion_tag('script.html', name='vue')
def vue(vue_ctx):
    if not isinstance(vue_ctx, VueContext):
        raise TypeError("Argument to 'vue' template must be a VueContext")

    return vue_ctx._to_render()
