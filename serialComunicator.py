import serial
import io
import time
import timeit


device = serial.Serial('COM4',115200, timeout=1)
print(device.name)
time.sleep(2)


def sendCommand(command, timeout):
    commandFinished = False
    start = timeit.default_timer()
    response = []
    device.write("{}\n".format(command).encode())
    while not commandFinished:
        data=device.readline()[:-2]
        if data:
            print(data.decode("utf-8"))
            response.append(data.decode("utf-8"))
            if data.decode("utf-8") == 'ok':
                return response
        time.sleep(0.001)
        if timeit.default_timer() - start > timeout:
            return response


a = sendCommand('$$', timeout=4)
aa = sendCommand('$X', timeout=4)
b = sendCommand('G21 ; Set units to mm', timeout=4)
c = sendCommand('G91 ; Relative  positioning', timeout=4)
d = sendCommand('G1 X1 Y0 F50', timeout=4)


device.close()
print('end')



