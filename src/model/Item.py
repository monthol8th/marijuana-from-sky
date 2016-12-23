import arcade
import random

class Item():
    def __init__(self, player,envi):
        self.view =  arcade.sprite.SpriteList()
        random.seed()
        self.player = player
        self.envi = envi

    def add_item(self):
        if random.randint(0,5) == 0:
            item = arcade.sprite.Sprite("./img/marijuana.png")
            item.set_position(random.randint(100,700),600)
            item.change_y = (-1)*random.randint(5,10)
            self.view.append(item)

    def update(self):

        hit = lambda a, b : abs(a.center_x - b.center_x)<=25 and abs(a.center_y - b.center_y) <= 70

        for item in self.view:
            if item.center_y<0:
                item.kill()
            elif hit(self.player,item):
                item.kill()
                self.envi.score+=1
                self.player.center_y += 5 if self.player.center_y <= 500 else 0

        self.view.update()

        self.add_item()

    def draw(self):
        self.view.draw()
