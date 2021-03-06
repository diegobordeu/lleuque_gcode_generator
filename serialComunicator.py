import serial
import time
import timeit
import sys


class Device:

    def __init__(self, port, baud_rate):
        self.port = port
        self.baud_rate = baud_rate

    def connect_device(self):
        self.device = serial.Serial(self.port, self.baud_rate, timeout=1)

    def send_command(self, command, timeout, is_setup=False):
        if is_setup:
            time.sleep(0.2)
        else:
            time.sleep(1)
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

    def load_grlb_config(self):
        f = open("grlb.conf", "r")
        content = f.readlines()
        for line in content:
            self.send_command(line, timeout=1, is_setup=True)
            print(f"initial setup ---->{line}")
        f.close()

