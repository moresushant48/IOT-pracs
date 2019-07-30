from time import sleep
from picamera import PiCamera
camera=PiCamera()
camera.resolution=(1780,720)
camera.start_preview()
sleep(10)
camera.capture('/home/pi/Desktop/Group 3 (M3)/image.jpg')
camera.stop_preview()
