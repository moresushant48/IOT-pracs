import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
Led1=29
Led2=31
Led3=33
Led4=35
Led5=36
Led6=37
Led7=38
Led8=40

GPIO.setup(Led1,GPIO.OUT)
GPIO.setup(Led2,GPIO.OUT)
GPIO.setup(Led3,GPIO.OUT)
GPIO.setup(Led4,GPIO.OUT)
GPIO.setup(Led5,GPIO.OUT)
GPIO.setup(Led6,GPIO.OUT)
GPIO.setup(Led7,GPIO.OUT)
GPIO.setup(Led8,GPIO.OUT)

def Ledpattern(ledval1,ledval2,ledval3,ledval4,ledval5,ledval6,ledval7,ledval8):
 GPIO.output(Led1,ledval1)
 GPIO.output(Led2,ledval2)
 GPIO.output(Led3,ledval3)
 GPIO.output(Led4,ledval4)
 GPIO.output(Led5,ledval5)
 GPIO.output(Led6,ledval6)
 GPIO.output(Led7,ledval7)
 GPIO.output(Led8,ledval8)

def patternOne():
 for i in range(0,2):
  Ledpattern(1,0,1,0,1,0,1,0)
  time.sleep(0.2)
  Ledpattern(0,1,0,1,0,1,0,1)
  time.sleep(0.2)

def patternTwo():
 for i in range(0,2):
  Ledpattern(0,0,0,1,1,0,0,0)
  time.sleep(0.2)
  Ledpattern(0,0,1,1,1,1,0,0)
  time.sleep(0.2)
  Ledpattern(0,1,1,1,1,1,1,0)
  time.sleep(0.2)
  Ledpattern(1,1,1,1,1,1,1,1)
  time.sleep(0.2)
  Ledpattern(0,1,1,1,1,1,1,0)
  time.sleep(0.2)
  Ledpattern(0,0,1,1,1,1,0,0)
  time.sleep(0.2)

def patternThree():
 for i in range(0,2):
  Ledpattern(1,1,0,1,1,0,1,1)
  time.sleep(0.2)
  Ledpattern(1,0,0,1,1,0,0,1)
  time.sleep(0.2)
  Ledpattern(0,1,1,0,0,1,1,0)
  time.sleep(0.2)
  Ledpattern(1,1,0,0,0,0,1,1)
  time.sleep(0.2)

def patternFour():
 for i in range(0,2):
  Ledpattern(0,0,1,0,0,1,0,0)
  time.sleep(0.2)
  Ledpattern(0,1,1,0,0,1,1,0)
  time.sleep(0.2)
  Ledpattern(1,0,0,1,1,0,0,1)
  time.sleep(0.2)
  Ledpattern(0,0,1,1,1,1,0,0)
  time.sleep(0.2)

try:
 while True:
  patternOne()
  patternTwo()
  patternThree()
  patternFour()
  
finally:
 GPIO.cleanup()
    
