import arcade
import random

class Item():
    def __init__(self, player):
        self.marijuana_list =  arcade.sprite.SpriteList()
        random.seed()
        self.player = player

    def add_marijuana(self):
        if random.randint(0,5) == 0:
            marijuana = arcade.sprite.Sprite("./img/marijuana.png")
            marijuana.set_position(random.randint(100,700),600)
            marijuana.change_y = (-1)*random.randint(5,10)
            self.marijuana_list.append(marijuana)

    def update(self):
        for marijuana in self.marijuana_list:
            if

        self.marijuana_list.update()

        self.add_marijuana()

    def draw(self):
        self.marijuana_list.draw()
