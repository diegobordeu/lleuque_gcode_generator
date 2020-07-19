import serialComunicator
import codeGenerator

lines = open("grilla.gcode", "r").readlines()

serialComunicator.time.sleep(2)

counter = 0
for line in lines:
    counter += 1
    print(line, counter)
    serialComunicator.sendCommand(line.strip(), timeout=1)
    pass


