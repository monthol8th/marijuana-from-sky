import arcade

class PlayerViewUpdater(object):
    """docstring for ."""
    def __init__(self,view):
        self.view = view
        self.moveable = True

    def upddate(self):
        if self.moveable:
            self.view.update()
