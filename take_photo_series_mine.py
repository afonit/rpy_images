import picamera
from time import sleep
import os

cur_wd = os.getcwd()


camera = picamera.PiCamera()

for i in range(459):    
    camera.capture(cur_wd + '/holder/current_series_image%03d.jpg' % i)
    sleep(2)
