import serial
import time
import timeit
import sys
import

device = serial.Serial('/dev/tty.usbserial-1410', 115200, timeout=1)
print(device.name)
time.sleep(2)


def sendCommand(command, timeout):
    # TODO ordenar funcion
    commandFinished = False
    start = timeit.default_timer()
    response = []
    comand = "{}\n".format(command).encode()
    device.write(comand)
    while not commandFinished:
        data = device.readline()[:-2]
        if data:
            # print(data.decode("utf-8"))
            response.append(data.decode("utf-8"))
            if data.decode("utf-8") == 'ok':
                return response
            if data.decode("utf-8") == 'error:2':
                print('erroooor', comand)
                return sys.exit()
        time.sleep(0.001)
        if timeit.default_timer() - start > timeout:
            return response


file = open('grilla.gcode', 'r')
# print(file.read())


a = sendCommand('$X', timeout=4)
for line in file.readlines():
    print(line)
    a = sendCommand(line[:-1], timeout=4)
    print(a)
    time.sleep(1)

file.close()
