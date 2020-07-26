import serial
import time
import timeit
import sys


class Device:

    def __init__(self, port, baud_rate, timeout):
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout

    def connect_device(self):
        self.device = serial.Serial(self.port, self.bandrate, self.timeout)

    def send_command(self, command, timeout):
        commandFinished = False
        start = timeit.default_timer()
        response = []
        command = "{}\n".format(command).encode()
        self.device.write(command)
        while not commandFinished:
            data = self.device.readline()[:-2]
            if data:
                decoded = data.decode("utf-8")
                response.append(decoded)
                if decoded == 'ok':
                    return response
                if decoded == 'error:2':
                    print('erroooor', command)
                    return sys.exit()
            time.sleep(0.001)
            if timeit.default_timer() - start > timeout:
                return response

# a = sendCommand('$$', timeout=4)
# aa = sendCommand('$X', timeout=4)
