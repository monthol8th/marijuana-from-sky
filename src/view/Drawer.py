import arcade

class Drawer():
    def __init__(self):
        self.view_container = []

    def append(self,view):
        self.view_container.append(view)

    def draw(self):
        for view in self.view_container:
            view.draw()
