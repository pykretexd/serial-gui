#!/usr/bin/python3                                                                                                                                                

import time
import serial
import io
import json


# configure the serial connections (the parameters differs on the device you are connecting to)                                                                   
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

# Some experiments here

ser.timeout = None          #block read

#ser.timeout = 5               #non-block read

#ser.timeout = 2              #timeout block read

ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control

ser.isOpen()

packet = ""
line = ""

def is_json(my_json):

    try:
        y = json.loads(my_json)
        #printf("We have a json", flush=True)
        #packet = ""
    except ValueError as e:
        print('.', end='', flush=True)
        return False
    
    #print('-', end='', flush=True)
    print("")
    print("Type : " + y["type"])
    print("Time : " + str(y["time"]))
    print(">" + my_json + "<")

    return True


while(True):
    #line = ser.readline()
    byte = ser.read();

    packet = packet + byte.decode('utf-8')

    if is_json(packet):
        packet = ""        # Blank packete
    
    
    


        
    
    

    

    
