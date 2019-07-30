import RPi.GPIO as GPIO
import time
import serial
def read_rfid():
    ser=serial.Serial("/dev/ttyUSB0")
    data=ser.read(12)
    return data
try:
    while True:
        id=read_rfid()
        print(id)
        if id=="1C0039C009EC":
            print("Access Granted")
            time.sleep(2)
        else:
            print("Acess Denied")
            time.sleep(2)
        
finally:
    GPIO.cleanup()
