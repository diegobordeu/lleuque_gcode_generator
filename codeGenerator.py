file = open("grilla.gcode", "w")
pause = 1


def build_file():
    xStart = 1
    yStart = 1
    xSteps = 3
    ySteps = 3
    speed = 50

    xTemp = xStart
    yTemp = yStart

    xEnd = xStart + xSteps
    yEnd = yStart + ySteps
    init_file()
    nFotos = 0
    while xTemp < xEnd:
        if yTemp == yStart:
            while yTemp < yEnd - 1:
                move_to(xTemp, yTemp, speed)
                yTemp += 1
            move_to(xTemp, yTemp, speed)
            xTemp += 1
            while yTemp > yStart:
                move_to(xTemp, yTemp, speed)
                yTemp -= 1
            move_to(xTemp, yTemp, speed)
            xTemp += 1

    file.close()
    # open and read the file after the appending:
    f = open("grilla.gcode", "r")
    print(f.read())
    f.close()


def init_file():
    file.write("G21 ; Set units to mm\n")
    file.write("G90 ; Absolute positioning\n")


def move_to(x,y,speed):
    file.write("G90 G1 X{} Y{} F{}\n".format(x,y,speed))
    file.write("G4 P{}\n".format(pause))

build_file()






