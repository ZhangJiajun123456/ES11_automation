import time

import serial

ser = serial.Serial("com3",9600,timeout = 50)
ser.close()
print(ser.name)
print(ser.port)
ser.open()
ser.write('hello'.encode())
time.sleep(4)
print('a')
s = ser.readline()
print('b')
s1 = ser.inWaiting()
print('c')
if s1!=0:
    recv = ser.read(ser.in_waiting).decode('gbk')
    print('d')
    print(recv)
print(s)
