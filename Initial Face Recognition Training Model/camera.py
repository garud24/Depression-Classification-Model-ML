import cv2
import os
import time
import csv
from  PIL import Image
import pandas as pd
#import matplotlib.pyplot as plt
from deepface import DeepFace

class Video(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)
        #time.sleep(5)

    def  closing(self):
        self.video.release()

    def  get_frame(self, i):
        ret,frame=self.video.read()
        os.chdir('F:\FA')
        img_name = str(i)+".jpg"
        cv2.imwrite(img_name,frame)
        

        ret,jpg=cv2.imencode('.jpg', frame)
        return jpg.tobytes()

    def predict(self):
        im = cv2.imread('xyz.jpg')
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier('F:\FACE\haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x+w, y+h), (0, 0, 255), 2)
            faces = im[y:y + h, x:x + w]
            cv2.imwrite('xyz.jpg', faces)
        img = cv2.imread('xyz.jpg')
        #plt.imshow(img)
        img2 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        #plt.imshow(img2)
        p = DeepFace.analyze(img2)
        print('dominant_emotion : '+p['dominant_emotion'])
        print('age : '+str(p['age']))
        print('gender : '+p['gender'])
        print('race : ' +p['dominant_race'])

        f = open("user.csv", "a",newline="")
        tuple1 = (p['dominant_emotion'],p['age'],p['gender'],p['dominant_race'])

        writer = csv.writer(f)
        writer.writerow(tuple1)
        f.close()

    




    
           