# PointOfVue

A simple, opinionated way to incorporate VueJS into your Django applications

## Installation

```
pip install PointOfVue
```

Add `pointofvue` to your Django installed apps:
```python
INSTALLED_APPS = [
    # other apps ...
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

## Custom JavaScript

It is likely that you won't be able to get away with just writing HTML Vue alone, you may need to define methods and other JS native entities in custom JavaScript.

 > **Note:** pointofvue encourages you to not write inline JavaScript in your Django HTML templates. Write separate JS files and serve them via staticfiles instead

Define a Vue entry point that exports your Vue data. It may look like this:
```javascript
import MyCustomComponent from './my-component.js';

const components = {
    MyCustomComponent,
};

export {
    components,
};
```

Build that JS file (target as a library if using vue-cli-service). Then register your script with the Python VueContext in your view:
```python
vue_ctx.add_script('myscript')
```

Now you can use your custom component in your template:
```html
<div id="app">
    <b>My Custom Component</b>
    <MyCustomComponent />
</div>
```
