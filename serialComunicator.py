import serial
import io
import time    


device = serial.Serial('COM4',115200, timeout=1)
print(device.name)
time.sleep(5)

rawString = device.readline()
print(rawString)

device.write(b'$$')
out = ''
        # let's wait one second before reading output (let's give device time to answer)
time.sleep(1)
while device.inWaiting() > 0:
    out +=  ''device.read(1)

if out != '':
    print(">>" + out)

time.sleep(2)
rawString = device.readline()
print(rawString)

# sio = io.TextIOWrapper(io.BufferedRWPair(device, device))
# sio.write(unicode("$$\n"))
# sio.flush() # it is buffering. required to get the data out *now*
# hello = sio.readline()
# print(hello)

# response = device.write(b'$$')



# device.write(b'G21 ; Set units to mm')
# device.write(b'G91 ; Relative  positioning')
# device.write(b'G1 X1 Y0 F50')
# # print(response)
# time.sleep(5)
device.close()
print('end')



