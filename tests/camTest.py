from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Documents/ProjectFiles/PiBirdBox/tests/testimage.jpg')
camera.stop_preview()