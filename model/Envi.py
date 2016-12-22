
class Envi:
    def __init__(self,player):
        self.point = 0
        self.direction_trigger = 5
        self.pause_val = 200

        self.score = 0
        self.point = 10
        self.permission = 5

        self.player = player

        self.pause_status = "USABLE"

    def pause_status_state(self):
        if self.pause_status == "USED":
            self.pause_val -= 10
            if self.pause_val <= 0:
                self.pause_status = "CHARGE"
        if self.pause_status == "CHARGE":
            self.pause_val += 1
            if self.pause_val >= 200:
                self.pause_status = "USABLE"

    def use_permission(self):
        if self.permission == 0:
            return False

        self.permission -= 1
        return True

    def update(self):
        if(self.score >= self.point):
            self.player.velo+=2
            self.point +=10

        self.pause_status_state()
