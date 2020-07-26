f = open("grilla.gcode", "w")


xStart = 1
yStart = 1
xSteps=3
ySteps=3
pause= 1
speed = 50

xTemp=xStart
yTemp=yStart

xEnd=xStart+xSteps
yEnd=yStart+ySteps

nFotos=0

def initFile():
    f.write("G21 ; Set units to mm\n")
    f.write("G90 ; Absolute positioning\n")

def moveTo(x,y,speed):
    f.write("G90 G1 X{} Y{} F{}\n".format(x,y,speed))
    f.write("G4 P{}\n".format(pause))


initFile()
while xTemp<xEnd:
    if yTemp==yStart:
        while yTemp<yEnd-1:
            moveTo(xTemp,yTemp,speed)
            yTemp+=1
        moveTo(xTemp, yTemp, speed)
        xTemp+=1
        while yTemp > yStart:
            moveTo(xTemp, yTemp, speed)
            yTemp -= 1
        moveTo(xTemp, yTemp, speed)
        xTemp += 1




f.close()

#open and read the file after the appending:
f = open("grilla.gcode", "r")
print(f.read())
f.close()
