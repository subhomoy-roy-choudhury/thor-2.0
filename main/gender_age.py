"""
Face detection
"""
import cv2
import os, random
from time import sleep
import time
import numpy as np
import argparse
from wide_resnet import WideResNet
from keras.utils.data_utils import get_file
from shot import shot

class FaceCV(object):
    
  
    """
    Singleton class for face recongnition task
    """
    CASE_PATH = ".\\pretrained_models\\haarcascade_frontalface_alt.xml"
    WRN_WEIGHTS_PATH = ".\\pretrained_models\\weights.18-4.06.hdf5"


    def __new__(cls, weight_file=None, depth=16, width=8, face_size=64):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FaceCV, cls).__new__(cls)
        return cls.instance

    def __init__(self, depth=16, width=8, face_size=64):
        self.face_size = face_size
        self.model = WideResNet(face_size, depth=depth, k=width)()
        model_dir = os.path.join(os.getcwd(), "pretrained_models").replace("//", "\\")
        fpath = get_file('weights.18-4.06.hdf5',
                         self.WRN_WEIGHTS_PATH,
                         cache_subdir=model_dir)
        self.model.load_weights(fpath)

    @classmethod
    def draw_label(cls, image, point, label, font=cv2.FONT_HERSHEY_SIMPLEX,
                   font_scale=1, thickness=2):
        size = cv2.getTextSize(label, font, font_scale, thickness)[0]
        x, y = point
        cv2.rectangle(image, (x, y - size[1]), (x + size[0], y), (255, 0, 0), cv2.FILLED)
        cv2.putText(image, label, point, font, font_scale, (255, 255, 255), thickness)

    def crop_face(self, imgarray, section, margin=40, size=64):
        """
        :param imgarray: full image
        :param section: face detected area (x, y, w, h)
        :param margin: add some margin to the face detected area to include a full head
        :param size: the result image resolution with be (size x size)
        :return: resized image in numpy array with shape (size x size x 3)
        """
        img_h, img_w, _ = imgarray.shape
        if section is None:
            section = [0, 0, img_w, img_h]
        (x, y, w, h) = section
        margin = int(min(w,h) * margin / 100)
        x_a = x - margin
        y_a = y - margin
        x_b = x + w + margin
        y_b = y + h + margin
        if x_a < 0:
            x_b = min(x_b - x_a, img_w-1)
            x_a = 0
        if y_a < 0:
            y_b = min(y_b - y_a, img_h-1)
            y_a = 0
        if x_b > img_w:
            x_a = max(x_a - (x_b - img_w), 0)
            x_b = img_w
        if y_b > img_h:
            y_a = max(y_a - (y_b - img_h), 0)
            y_b = img_h
        cropped = imgarray[y_a: y_b, x_a: x_b]
        resized_img = cv2.resize(cropped, (size, size), interpolation=cv2.INTER_AREA)
        resized_img = np.array(resized_img)
        return resized_img, (x_a, y_a, x_b - x_a, y_b - y_a)

    def detect_face(self):
        face_cascade = cv2.CascadeClassifier(self.CASE_PATH)
        label_dict = []
        for i in range(1):
            shot('gender.png')
            frame = cv2.imread("gender.png")

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=10,
                minSize=(self.face_size, self.face_size)
            )
            if faces is not ():
                
                # placeholder for cropped faces
                face_imgs = np.empty((len(faces), self.face_size, self.face_size, 3))
                for i, face in enumerate(faces):
                    face_img, cropped = self.crop_face(frame, face, margin=40, size=self.face_size)
                    (x, y, w, h) = cropped
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 200, 0), 2)
                    face_imgs[i,:,:,:] = face_img
                
                if len(face_imgs) > 0:
                    # predict ages and genders of the detected faces
                    results = self.model.predict(face_imgs)
                    predicted_genders = results[0]
                    ages = np.arange(0, 101).reshape(101, 1)
                    predicted_ages = results[1].dot(ages).flatten()
                    
                # draw results
                for i, face in enumerate(faces):
                    label = "{}, {}".format(int(predicted_ages[i]),
                                            "F" if predicted_genders[i][0] > 0.5 else "M")
                    print(int(predicted_ages[i]),predicted_genders[i][0])
                    if predicted_genders[i][0] < 0.5 and ((int(predicted_ages[i])>10) and (int(predicted_ages[i])<20)) :
                        print("beta")
                        label_position = (150,200)
                        cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
                        cv2.imwrite("gender_test.png",frame) 
                        label1 = 'beta'
                    elif predicted_genders[i][0] < 0.5 and ((int(predicted_ages[i])>=20) and (int(predicted_ages[i])<40)) :
                        print("Sir")
                        label_position = (150,200)
                        cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
                        cv2.imwrite("gender_test.png",frame) 
                        label1 = 'sir'
                    elif predicted_genders[i][0] > 0.5 and ((int(predicted_ages[i])>10) and (int(predicted_ages[i])<20)) :
                        print("beti")
                        label_position = (150,200)
                        cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
                        cv2.imwrite("gender_test.png",frame) 
                        label1 = 'beti'
                    elif predicted_genders[i][0] > 0.5 and ((int(predicted_ages[i])>=20) and (int(predicted_ages[i])<40)) :
                        print("maam")
                        label_position = (150,200)
                        cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
                        cv2.imwrite("gender_test.png",frame) 
                        label1 = 'maam'
                    label_dict.append(label1)
                    self.draw_label(frame, (face[0], face[1]), label)
            else:
                print('No faces')
                label1 = 'Sir'
                label_dict.append(label1)
        return label_dict[-1]

def get_args():
    parser = argparse.ArgumentParser(description="This script detects faces from web cam input, "
                                                 "and estimates age and gender for the detected faces.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("--depth", type=int, default=16,
                        help="depth of network")
    parser.add_argument("--width", type=int, default=8,
                        help="width of network")
    args = parser.parse_args()
    return args

def gender_age():
    args = get_args()
    depth = args.depth
    width = args.width

    face = FaceCV(depth=depth, width=width)

    name = face.detect_face()
    return name

if __name__ == "__main__":
    while True:
        print('$$$$$$$'+str(gender_age()))
    
    






