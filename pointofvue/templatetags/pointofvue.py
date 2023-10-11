from django import template
from ..context import VueContext
from ..settings import get_setting

register = template.Library()

script_name = 'script_vue3.html' if get_setting('VUE_VERSION', '2') == '3' else 'script.html'


@register.inclusion_tag(script_name, name='vue')
def vue(vue_ctx):
    if not isinstance(vue_ctx, VueContext):
        raise TypeError("Argument to 'vue' template must be a VueContext")

    return vue_ctx._to_render()
