import arcade.shape_objects

class Panel():
    def __init__(self, envi):
        self.envi = envi


    def draw(self):
        #arcade.draw_commands.draw_rectangle_filled( 70 ,50 , 50 , 400 ,arcade.color.WHITE)
        fuckjew = "GAUGE: "+str(self.envi.pause_val/2.0)+"%"
        fuckjewcolor = arcade.color.BLUE if self.envi.pause_status != "CHARGE" else arcade.color.RED
        arcade.draw_text(fuckjew, 20, 20,fuckjewcolor, 20)

        fuckjew = "SWAP: "+str(self.envi.permission)
        fuckjewcolor = arcade.color.BLUE if self.envi.permission > 0 else arcade.color.RED
        arcade.draw_text(fuckjew, 250, 20,fuckjewcolor, 20)
