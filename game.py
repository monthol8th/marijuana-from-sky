import arcade
import model

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.background = arcade.sprite.Sprite("./img/background.jpg");
        self.background.set_position(400,300)

        self.player = model.Player()
        self.playerview = self.player.view

        self.player_can_move = True

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.LSHIFT :
            self.player_can_move = True

    def on_key_press(self, key, key_modifiers):

        if key == arcade.key.LSHIFT :
            self.player_can_move = False
        elif key == arcade.key.SPACE and self.player_can_move:
            self.player.change_direction()



    def on_draw(self):
        arcade.start_render()

        self.background.draw()

        self.player.update()
        if(self.player_can_move):
            self.playerview.update()
        self.playerview.draw()

if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
