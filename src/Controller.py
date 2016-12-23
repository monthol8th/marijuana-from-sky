import arcade
import simpleaudio as sa
from .model import *
from .view import *

class Controller(object):
    """docstring for Controller."""
    def __init__(self,parent):

        self.parent = parent
        self.gameover = False

        self.drawer = Drawer();
        self.updater = Updater();

        arcade.set_background_color(arcade.color.BLACK)

        self.background = arcade.sprite.Sprite("./img/background.jpg");
        self.background.set_position(400,300)

        self.player = Player()
        self.playerview = self.player.view

        self.envi = Envi(self.player)
        self.panel = Panel(self.envi)
        self.marijuana = Item(self.playerview,self.envi)
        self.jewel = Jewel(self.playerview,self.envi)
        self.clover = Clover(self.playerview,self.envi)

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

        self.wave_obj = sa.WaveObject.from_wave_file("./fckjw.wav")
        #self.play_obj = self.wave_obj.play()

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.SPACE and (self.envi.pause_status == "USED" or self.envi.pause_status == "DISCHARGE"):
            self.envi.pause_status = "CHARGE"

    def on_key_press(self, key, key_modifiers):

        if self.gameover and key == arcade.key.SPACE:
            self.parent.controller = Controller(self.parent)
        if key == arcade.key.SPACE and self.envi.pause_status == "USABLE":
            self.envi.pause_status = "USED"
        elif key == arcade.key.LSHIFT and self.envi.pause_status != "USED":
            if self.envi.use_permission():
                self.player.change_direction()

    def on_draw(self):
        arcade.start_render()
        self.background.draw()

        if(not self.gameover and self.playerview.center_y>=-40):
            self.updater.update()
            self.drawer.draw()

        else:
            self.gameover = True
            arcade.draw_text("GAME OVER", 0, 250,arcade.color.RED, 100)
