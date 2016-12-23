import arcade
import random

class RandomObj():
    def __init__(self,view,random_limit,speed_low,speed_high,img):
        self.view = view
        self.random_limit = random_limit
        self.img = img
        self.speed_low = speed_low
        self.speed_high = speed_high

class Randommer():
    def __init__(self):
        self.item_container=[]
        random.seed()

    def append(self,view,random_limit,speed_low,speed_high,img):
        self.item_container.append(RandomObj(view,random_limit,speed_low,speed_high,img))

    def random(self):
        for obj in self.item_container:
            if random.randint(0,obj.random_limit) == 0:
                item = arcade.sprite.Sprite("./img/"+obj.img+".png")
                item.set_position(random.randint(100,700),600)
                item.change_y = (-1)*random.randint(obj.speed_low,obj.speed_high)
                obj.view.append(item)
