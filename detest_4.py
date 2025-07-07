import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.write(b'1')
time.sleep(1)
ser.write(b'0')