import arcade
import model

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.envi = model.Envi()
        self.panel = model.Panel(self.envi)

        self.background = arcade.sprite.Sprite("./img/fckjw.jpg");
        self.background.set_position(400,300)

        self.marijuana_generator = model.Item(self.player)

        self.player = model.Player()
        self.playerview = self.player.view

        self.marijuana_generator = model.Item(self.player)


        self.player_can_move = True

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.LSHIFT and (self.envi.pause_status == "USED" or self.envi.pause_status == "DISCHARGE"):
            self.player_can_move = True
            self.envi.pause_status = "CHARGE"

    def on_key_press(self, key, key_modifiers):

        if key == arcade.key.LSHIFT and self.envi.pause_status == "USABLE":
            self.player_can_move = False
            self.envi.pause_status = "USED"
        elif key == arcade.key.SPACE and self.player_can_move:
            if self.envi.use_permission():
                self.player.change_direction()

    def on_draw(self):
        arcade.start_render()
        self.background.draw()

        self.player.update()
        self.envi.update()
        self.marijuana_generator.update()

        if(self.envi.pause_status != "USED"):
            self.playerview.update()
        self.playerview.draw()
        self.marijuana_generator.draw()
        self.panel.draw()

if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
