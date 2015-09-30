import picamera
import time

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    time.sleep(1) # Camera warm-up time
    for i, filename in enumerate(camera.capture_continuous('image{counter:02d}.jpg')):
        print('Captured %s' % filename)
        # Capture one image a minute
        time.sleep(60)
        if i == 5:
            break
