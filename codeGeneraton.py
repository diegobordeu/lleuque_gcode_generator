f = open("grilla.gcode", "w")


xAxis = 50
yAxis = 20
pause= 1
speed = 50

def initFile():
    f.write("G21 ; Set units to mm\n")
    f.write("G91 ; Relative positioning\n")

def buildFileY():
    for y in range(0, yAxis-1):
        f.write("G1 X{} Y{} F{}\n".format(0, 1,speed))
        f.write("G4 P{}\n".format(pause))

def buildFileX():
    for x in range(0, xAxis-1):
        f.write("G1 X{} Y{} F{}\n".format(-1, 0,speed))
        f.write("G4 P{}\n".format(pause))


initFile()
# buildFileY()
buildFileX()

# f.write("G1 X{} Y{} F{}\n".format(0, -1 * (yAxis - 1),speed))
# f.write("G1 X{} Y{} F{}\n".format(-1 * (xAxis - 1), 0,speed))
#open and read the file after the appending:
f = open("grilla.gcode", "r")
print(f.read())