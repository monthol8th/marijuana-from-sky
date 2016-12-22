
class Envi:
    def __init__(self):
        self.point = 0
        self.direction_trigger = 5
        self.pause_val = 20

        self.pause_status = "USABLE"

    def pause_status_state(self):
        if self.pause_status == "USED":
            self.pause_val -= 1
            if self.pause_val <= 0:
                self.pause_status = "DISCHARGE"
        if self.pause_status == "CHARGE":
            self.pause_val += 1
            if self.pause_val >= 50:
                self.pause_status = "USABLE"
                self.pause_val = 20

    def update(self):
        self.pause_status_state()
