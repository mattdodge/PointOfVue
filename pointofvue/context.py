class VueContext():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = {}

    def set_data(self, key, val):
        """ Sets some data to be served to the Vue app """
        self.data[key] = val
