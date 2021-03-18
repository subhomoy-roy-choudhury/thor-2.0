import time
import cv2
def shot(IMAGE):
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    time.sleep(0.1)  # If you don't wait, the image will be dark
    return_value, image = camera.read()
    cv2.imwrite(IMAGE, image)
    del(camera)