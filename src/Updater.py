import arcade

class Updater(object):
    """docstring for Updater."""
    def __init__(self):
        self.model_container = []

    def append(self,model):
        self.model_container.append(model)

    def update(self):
        for model in self.model_container:
            model.update()
