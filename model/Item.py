import arcade
import random

class Item():
    def __init__(self, player,envi):
        self.marijuana_list =  arcade.sprite.SpriteList()
        random.seed()
        self.player = player
        self.envi = envi

    def add_marijuana(self):
        if random.randint(0,5) == 0:
            marijuana = arcade.sprite.Sprite("./img/marijuana.png")
            marijuana.set_position(random.randint(100,700),600)
            marijuana.change_y = (-1)*random.randint(5,10)
            self.marijuana_list.append(marijuana)

    def update(self):

        hit = lambda a, b : abs(a.center_x - b.center_x)<=15 and abs(a.center_y - b.center_y) <= 30

        for marijuana in self.marijuana_list:
            if marijuana.center_y<0:
                marijuana.kill()
            elif hit(self.player,marijuana):
                marijuana.kill()
                self.envi.score+=1

        self.marijuana_list.update()

        self.add_marijuana()

    def draw(self):
        self.marijuana_list.draw()
