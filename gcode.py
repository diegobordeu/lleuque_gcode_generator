class GCode(object):
    

    def __init__(self, x_steps=49, y_steps=19, pause=1, speed=50):
        self.x_steps = x_steps
        self.y_steps = y_steps
        self.pause = pause
        self.speed = speed
        self.file = open("grilla.gcode", "w")
        self.x_start = 1
        self.y_start = 1

    def move_to(self, x, y, speed):
        self.file.write(f"G90 G1 X{x} Y{y} F{speed}\n")
        self.file.write(f"G4 P{self.pause}\n")

    def init_file(self):
        self.file.write("G21 ; Set units to mm\n")
        self.file.write("G90 ; Absolute positioning\n")

    def build_file(self):
        x_end = self.x_start + self.x_steps
        y_end = self.y_start + self.y_steps
        x_temp = self.x_start
        y_temp = self.y_start
        self.file.write(f"G4 P{self.pause}\n") # initial picture
        while x_temp < x_end:
            if y_temp == self.y_start:
                while y_temp < y_end:
                    self.move_to(x_temp, y_temp, self.speed)
                    y_temp += 1
                self.move_to(x_temp, y_temp, self.speed)
                x_temp += 1
                while y_temp > self.y_start:
                    self.move_to(x_temp, y_temp, self.speed)
                    y_temp -= 1
                self.move_to(x_temp, y_temp, self.speed)
                x_temp += 1
        self.file.close()

    def get_gcode(self):
        f = open("grilla.gcode", "r")
        content = f.readlines()
        f.close()
        return content