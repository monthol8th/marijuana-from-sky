import arcade
from .Item import Item
import random

class Jewel(Item):
    def __init__(self,player,envi):
        super().__init__(player,envi)
        self.limit = 0
        self.count = 0
        self.down = -5

    def add_item(self):
        if random.randint(0,20) == 0:
            item = arcade.sprite.Sprite("./img/jew.png")
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
                self.player.change_y = self.down
                self.limit +=4
                self.count = 0

        if self.player.change_y == self.down:
            if self.count >= self.limit:
                self.count,self.limit = 0,0
                self.player.change_y = 0
            else:
                self.count +=1
        else
            self.count+=1
            if self.count>=50:
                self.down-=1
                self.count = 0


        self.item_list.update()

        self.add_item()
