import arcade
from .model import *
from .view import *

class Controller(object):
    """docstring for Controller."""
    def __init__(self):
        arcade.set_background_color(arcade.color.BLACK)

        self.drawer = Drawer();
        self.updater = Updater();

        self.background = arcade.sprite.Sprite("./img/background.jpg");
        self.background.set_position(400,300)


        self.player = Player()
        self.playerview = self.player.view

        self.envi = Envi(self.player)
        self.panel = Panel(self.envi)

        self.marijuana = Item(self.playerview,self.envi)
        self.jewel = Jewel(self.playerview,self.envi)
        self.clover = Clover(self.playerview,self.envi)


        self.player_can_move = True

        self.updater.append(self.player)
        self.updater.append(self.envi)
        self.updater.append(self.marijuana)
        self.updater.append(self.jewel)
        self.updater.append(self.clover)
        self.updater.append(self.player.view_updater)

        self.drawer.append(self.player.view)
        self.drawer.append(self.marijuana.view)
        self.drawer.append(self.jewel.view)
        self.drawer.append(self.clover.view)
        self.drawer.append(self.panel)

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.SPACE and (self.envi.pause_status == "USED" or self.envi.pause_status == "DISCHARGE"):
            self.player_can_move = True
            self.envi.pause_status = "CHARGE"

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE and self.envi.pause_status == "USABLE":
            self.player_can_move = False
            self.envi.pause_status = "USED"
        elif key == arcade.key.LSHIFT and self.envi.pause_status != "USED":
            if self.envi.use_permission():
                self.player.change_direction()

    def on_draw(self):
        arcade.start_render()
        self.background.draw()

        if(self.playerview.center_y>=-40):
            self.updater.update()
            self.drawer.draw()

        else:
            arcade.draw_text("GAME OVER", 0, 250,arcade.color.RED, 100)
