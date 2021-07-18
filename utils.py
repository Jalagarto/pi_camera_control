from picamera import PiCamera
from os.path import join
import os
from time import sleep
camera = PiCamera()
camera.rotation = 180


"""
__all__ = ['datetime_now', 'multiple_pics', 'show_preview',
'take_still_picts', 'take_video']

# https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/7
# https://picamera.readthedocs.io/en/release-1.10/recipes1.html
"""

def datetime_now():
    from datetime import datetime
    d = datetime.now()
    print(d)
    return f"{d.year}-{d.strftime('%B')}-{d.day}"


def show_preview(t=5):
    """   t=preview_time: seconds to show   """
    camera.start_preview() # alpha=150)
    sleep(3)
    camera.stop_preview()


def take_still_picts(t=5):
    camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()


def multiple_pics(pics_path_root):
    new_dir = join(pics_path_root, datetime_now())
    os.makedirs(new_dir, exist_ok=True)
    camera.start_preview()
    for i in range(5):
        sleep(3)
        camera.capture(join(new_dir, 'image%s.jpg' % i))
    camera.stop_preview()


def take_video(secs=10):
    camera.resolution = (640, 480)
    camera.start_recording('/home/pi/results/my_video.h264')
    camera.wait_recording(secs)
    camera.stop_recording()


if __name__=="__main__":
    # take_still_picts()
    # pics_path_root = '/home/pi/results/images' 
    # multiple_pics(pics_path_root)
    take_video(secs=10)
