import cv2
import numpy as np
import os 
from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
from shot import shot
from statistics import mode
# recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer.read('trainer/trainer.yml')
def emotion():

    label_dict = {1:'Angry',2:'Happy',3:'Neutral',4:'Sad',5:'Surprise',6:'not found'}

    # Emotions related to ids: example ==> Anger: id=0,  etc
    names = ['Angry','Happy','Neutral','Sad','Surprise']
    classifier =load_model('pretrained_models/Emotion_Detection.h5')
    cascadePath = "pretrained_models/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    label_list =[]
    for i in range(1):
        shot('opencv.png')
        font = cv2.FONT_HERSHEY_SIMPLEX

        #iniciate id counter
        id = 0

        img = cv2.imread("opencv.png")

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            roi_gray = gray[y:y+h,x:x+w]
            roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)
            if np.sum([roi_gray])!=0:
                roi = roi_gray.astype('float')/255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi,axis=0)

                preds = classifier.predict(roi)[0]
                print("\nprediction = ",preds)
                label=names[preds.argmax()]
                print("\nprediction max = ",preds.argmax())
                print("\nlabel = ",label)
                label_position = (x,y)
                cv2.putText(img,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
                cv2.imwrite("opencv_test.png",img)
                print("\n [INFO] Done detecting and Image is saved")
                # return label 
            else :
                label = 'not found'
                print('not found')
        for id1, label1 in label_dict.items():
            if label1 == label:
                label_list.append(id1)
    print(label_dict[mode(label_list)])
    return label_dict[mode(label_list)]


if __name__ == '__main__':
    while True:
        emotion()
