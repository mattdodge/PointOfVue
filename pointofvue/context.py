from os.path import join


class VueContext():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = {}
        self.scripts = []
        self.static_base = join('build', 'js')

    def set_data(self, key, val):
        """ Sets some data to be served to the Vue app """
        self.data[key] = val

    def add_script(self, script_loc):
        """ Add a static JS script to include in the page as well """
        self.scripts.append(script_loc)

    def _to_render(self):
        """ Return a dictionary to use to render the template """
        # TODO: Make it '.min.js' for prod
        script_suffix = '.umd.js'
        obj = {
            'data': self.data,
            'scripts': self.scripts,
            'script_locs': [
                join(
                    self.static_base,
                    sc + script_suffix
                ) for sc in self.scripts
            ],
        }
        return obj
