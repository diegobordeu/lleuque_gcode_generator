from serialComunicator import Device
import codeGenerator
from time import sleep
from picamera import PiCamara

codeGenerator.build_file()
gcode_file = open("grilla.gcode", "r")

camera = PiCamara()


def start():
    arduino = Device(port='/dev/tty.usbserial-1410', baud_rate=115200, timeout=1)
    lines = gcode_file.readlines()
    sleep(2)
    camera.start_preview()
    do_lines((lines, arduino))


def finish():
    gcode_file.close()
    camera.stop_preview()
    camera.close()


def take_pictures(c):
    file_path = "./pictures/{}".format(c)
    print(file_path)
    camera.capture(file_path, 'jpeg')


def do_lines(lines, arduino):
    counter = 0
    for line in lines:
        counter += 1
        print(line, counter)
        arduino.send_command(line.strip(), timeout=1)
        pass

start()
finish()



