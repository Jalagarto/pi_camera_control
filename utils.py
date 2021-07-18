from picamera import PiCamera
from os.path import join
import os
from time import sleep
camera = PiCamera()
camera.rotation = 180


"""  All functions:
__all__ = ['datetime_now', 'multiple_pics', 'show_preview',
'take_still_picts', 'take_video']
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

def take_video():
    pass

# https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/7


if __name__=="__main__":
    # take_still_picts()
    pics_path_root = '/home/pi/results/images' 
    multiple_pics(pics_path_root)

    ### usage: python3 utils.py
