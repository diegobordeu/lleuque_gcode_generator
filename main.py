from serialComunicator import Device
import codeGenerator
from time import sleep
from picamera import PiCamera

codeGenerator.build_file()
gcode_file = open("grilla.gcode", "r")

camera = PiCamera()


def start():
    arduino = Device(port='/dev/ttyUSB0', baud_rate=115200)
    arduino.connect_device()
    lines = gcode_file.readlines()
    sleep(2)
    arduino.send_command('$X',timeout=4)
    camera.start_preview()
    do_lines(lines, arduino)


def finish():
    gcode_file.close()
    camera.stop_preview()
    camera.close()


def take_picture(c, delay):
    sleep(delay)
    file_path = "./pictures/{}".format(c)
    print(file_path)
    camera.capture(file_path, 'jpeg')


def do_lines(lines, arduino):
    counter = 0
    pic_count = 0
    for line in lines:
        command = line.strip()
        print(command)
        counter += 1
        if command == 'G4 P1':
            pic_count += 1
            take_picture(pic_count, 3)
        # print(line, counter)
        response = arduino.send_command(line.strip(), timeout=1)
        print(response)
        pass

start()
finish()



