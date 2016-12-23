import arcade
import src

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.controller = src.Controller()


    def on_key_release(self, key, key_modifiers):
        self.controller.on_key_release(key, key_modifiers)

    def on_key_press(self, key, key_modifiers):
        self.controller.on_key_press(key,key_modifiers)

    def on_draw(self):
        self.controller.on_draw()

if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
