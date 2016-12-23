import arcade
import src

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.drawer = src.Drawer();
        self.updater = src.Updater();

        self.background = arcade.sprite.Sprite("./img/background.jpg");
        self.background.set_position(400,300)


        self.player = src.Player()
        self.playerview = self.player.view

        self.envi = src.Envi(self.player)
        self.panel = src.Panel(self.envi)

        self.marijuana = src.Item(self.playerview,self.envi)
        self.jewel = src.Jewel(self.playerview,self.envi)
        self.clover = src.Clover(self.playerview,self.envi)


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
        #     self.player.update()
        #     self.envi.update()
        #     self.marijuana.update()
        #     self.jewel.update()
        #     self.clover.update()
        #
        #     if(self.envi.pause_status != "USED"):
        #         self.playerview.update()
            self.updater.update()
            self.drawer.draw()

        else:
            arcade.draw_text("GAME OVER", 0, 250,arcade.color.RED, 100)

if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
