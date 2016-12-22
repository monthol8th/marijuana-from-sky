import arcade

class Player(arcade.sprite.Sprite):
    def __init__(self):

        self.ongoing = "right"
        self.state = "MOVE"

        self.velo = 7
        self.is_direction_change = False
        self.view = arcade.sprite.Sprite("./img/pimp_right.png")
        self.view.set_position(100,100)
        self.view.append_texture(arcade.draw_commands.load_texture("./img/pimp_left.png"))
        self.view.change_x = 5

    def change_direction(self):
        self.ongoing = "right" if self.ongoing == "left" else "left"
        self.is_direction_change = True

    def wall_contact_check(self):
        if (self.ongoing == "right" and self.view.right >= 790) or (self.ongoing == "left" and self.view.left <= 10):
            self.change_direction()

    def update(self):
        self.wall_contact_check()
        self.on_direction_change()

    def on_direction_change(self):
        if self.is_direction_change:
            self.view.change_x = self.velo if self.ongoing == "right" else self.velo*(-1)
            self.view.set_texture(0 if self.ongoing == "right" else 1)
