import arcade
from .Item import Item
import random

class Jewel(Item):
    def __init__(self,player,envi):
        super().__init__(player,envi)
        self.limit = 0
        self.count = 0

    def add_item(self):
        if random.randint(0,50) == 0:
            item = arcade.sprite.Sprite("./img/clover.png")
            item.set_position(random.randint(100,700),600)
            item.change_y = (-1)*random.randint(5,10)
            self.item_list.append(item)

    def update(self):

        hit = lambda a, b : abs(a.center_x - b.center_x)<=25 and abs(a.center_y - b.center_y) <= 70

        for item in self.item_list:
            if item.center_y<0:
                item.kill()
            elif hit(self.player,item):
                item.kill()
                self.envi.permission+=1


        self.item_list.update()

        self.add_item()