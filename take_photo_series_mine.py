import picamera
from time import sleep
import os

cur_wd = os.getcwd()


camera = picamera.PiCamera()

for i in range(9059):    
    camera.capture(cur_wd + '/holder/current_series_image%04d.jpg' % i)
    sleep(20)
