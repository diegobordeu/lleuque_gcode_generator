import serial
import io
import time    


device = serial.Serial('COM4',115200, timeout=1)
print(device.name)
time.sleep(2)

device.write(b"\r\n\r\n")

device.write(b"$$\n")
data = device.readline()[:-2]
time.sleep(2)
print(data)

# while True:
# 	data = device.readline()[:-2] #the last bit gets rid of the new-line chars
# 	if data:
# 		print(data)



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



