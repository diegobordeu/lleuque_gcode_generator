from serialComunicator import Device
from gcode import GCode
from time import sleep
from picamera import PiCamera

gcode = GCode(2,2)
gcode.init_file()
gcode.build_file()

camera = PiCamera()

def start():
    arduino = Device(port='/dev/ttyUSB0', baud_rate=115200)
    arduino.connect_device()
    sleep(2)
    arduino.send_command('$X',timeout=4)
    sleep(2)
    arduino.load_grlb_config()
    sleep(5)
    camera.start_preview()
    lines = gcode.get_gcode()
    do_gcode_lines(lines, arduino)


def finish():
    camera.stop_preview()
    camera.close()


def take_picture(c, delay):
    sleep(delay)
    file_path = f"./pictures/{c}"
    print(file_path)
    camera.capture(file_path, 'jpeg')


def do_gcode_lines(lines, arduino):
    counter = 0
    pic_count = 0
    for line in lines:
        command = line.strip()
        counter += 1
        if command == 'G4 P1':
            pic_count += 1
            take_picture(pic_count, 1)
        response = arduino.send_command(line.strip(), timeout=1)
        # print(response)
        pass

start()
finish()



