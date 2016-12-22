import arcade

class Marijuana(arcade.sprite.Sprite):
    def __init__(self,location):
        super().__init__("./img/marijuana.png")
        self.set_position(location,600)
        self.change_y = -10
