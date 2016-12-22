import arcade
import model

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.background = arcade.sprite.Sprite("./img/fckjw.jpg");
        self.background.set_position(400,300)


        self.player = model.Player()
        self.playerview = self.player.view

        self.envi = model.Envi(self.player)
        self.panel = model.Panel(self.envi)

        self.marijuana_generator = model.Item(self.playerview,self.envi)
        self.jewel_generator = model.Jewel(self.playerview,self.envi)
        self.clover_generator = model.Clover(self.playerview,self.envi)


        self.player_can_move = True

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.SPACE and (self.envi.pause_status == "USED" or self.envi.pause_status == "DISCHARGE"):
            self.player_can_move = True
            self.envi.pause_status = "CHARGE"

    def on_key_press(self, key, key_modifiers):

        if key == arcade.key.SPACE and self.envi.pause_status == "USABLE":
            self.player_can_move = False
            self.envi.pause_status = "USED"
        elif key == arcade.key.LSHIFT and self.player_can_move:
            if self.envi.use_permission():
                self.player.change_direction()

    def on_draw(self):
        arcade.start_render()
        self.background.draw()

        if(self.playerview.center_y>=50):
            self.player.update()
            self.envi.update()
            self.marijuana_generator.update()
            self.jewel_generator.update()
            self.clover_generator.update()

            if(self.envi.pause_status != "USED"):
                self.playerview.update()
            self.playerview.draw()
            self.marijuana_generator.draw()
            self.jewel_generator.draw()
            self.clover_generator.draw()

        else:
            arcade.draw_text("GAME OVER", 0, 250,arcade.color.RED, 100)
        self.panel.draw()

if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
