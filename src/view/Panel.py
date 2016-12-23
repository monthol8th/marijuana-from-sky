import arcade.shape_objects

class Panel():
    def __init__(self, envi):
        self.envi = envi


    def draw(self):
        #arcade.draw_commands.draw_rectangle_filled( 70 ,50 , 50 , 400 ,arcade.color.WHITE)

        fuckjew = "SWAP: "+str(self.envi.permission)
        fuckjewcolor = arcade.color.YELLOW if self.envi.permission > 0 else arcade.color.RED

        arcade.draw_text(fuckjew, 20, 550,fuckjewcolor, 20)

        fuckjew = "GAUGE: "+str(self.envi.pause_val/2.0)+"%"
        fuckjewcolor = arcade.color.YELLOW if self.envi.pause_status != "CHARGE" else arcade.color.RED
        arcade.draw_text(fuckjew, 150, 550,fuckjewcolor, 20)

        fuckjew = "SCORE:"
        fuckjewcolor = arcade.color.BLUE
        arcade.draw_text(fuckjew, 680, 550,fuckjewcolor, 15)
        arcade.draw_text(str(self.envi.score), 680, 535,fuckjewcolor, 15)
