# PointOfVue

A simple, opinionated way to incorporate VueJS into your Django applications

## Installation

```
pip install PointOfVue
```

Add `pointofvue` to your Django installed apps:
```
INSTALLED_APPS = [
	...
	'pointofvue',
]
```

## Basic Usage

In your view, import `pointofvue` and send a `pointofvue.VueContext` instance to your template
```python
import pointofvue

def view_handler(request):
    vue_ctx = pointofvue.VueContext()
    vue_ctx.set_data('var1', 'My value')

    return render(request, 'template.html', {
        vue_ctx: vue_ctx,
    })
```

In your template, write your Vue code in a `#app` element and use `${` and `}` for accessing Vue data. Then load the `pointofvue` templates and call the `{% vue %}` tag with your `VueContext` to load VueJS and create an app.

```html
<div id='app'>
    The value of 'var1' is <b>${ var1 }</b>
</div>

{% load pointofvue %}
{% vue vue_ctx %}
```
