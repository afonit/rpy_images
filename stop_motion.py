import picamera
from time import sleep
import os

cur_wd = os.getcwd()


with picamera.PiCamera() as camera:
    camera.start_preview()
    
    frame = 0
    while True:    
        take_photo = raw_input("Press enter to take the next photo")
        camera.capture(cur_wd + '/holder/current_series_image%03d.jpg' % frame)
        print('you just took % frame' % frame)
        frame += 1
    camera.stop_preview()
