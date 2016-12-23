import arcade
from .Item import Item
import random

class Clover(Item):
    def __init__(self,player,envi):
        super().__init__(player,envi)

    def add_item(self):
        if random.randint(0,60) == 0:
            item = arcade.sprite.Sprite("./img/clover.png")
            item.set_position(random.randint(100,700),600)
            item.change_y = (-1)*random.randint(10,25)
            self.view.append(item)

    def update(self):

        hit = lambda a, b : abs(a.center_x - b.center_x)<=25 and abs(a.center_y - b.center_y) <= 70

        for item in self.view:
            if item.center_y<0:
                item.kill()
            elif hit(self.player,item):
                self.envi.pause_val+=5*abs(item.change_y)
                self.envi.permission+= (abs(item.change_y) - 10)/2+1 if item.change_y>=15 else 2
                item.kill()



        self.view.update()

        self.add_item()
