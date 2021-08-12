from os.path import join
from .settings import get_setting


class VueContext():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = {}
        self.scripts = []
        # TODO: make this a setting
        self.static_base = join('build', 'js')

    def set_data(self, key, val):
        """ Sets some data to be served to the Vue app """
        self.data[key] = val

    def add_script(self, script_loc):
        """ Add a static JS script to include in the page as well """
        self.scripts.append(script_loc)

    def _to_render(self):
        """ Return a dictionary to use to render the template """
        script_suffix = '.umd.min.js' if self._use_minified else '.umd.js'
        obj = {
            'data': self.data,
            'use_minified': self._use_minified(),
            'scripts': self.scripts,
            'script_locs': [
                join(
                    self.static_base,
                    sc + script_suffix
                ) for sc in self.scripts
            ],
        }
        return obj

    def _use_minified(self):
        return any([
            get_setting('USE_MINIFIED', False),
            get_setting('ENV', prefix=False) == 'prod',
            get_setting('ENVIRONMENT', prefix=False) == 'prod',
            get_setting('ENV', prefix=False) == 'production',
            get_setting('ENVIRONMENT', prefix=False) == 'production',
        ])
