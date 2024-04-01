import cv2
import os
import time
import face_recognition
from  PIL import Image
import pandas as pd

# In[99]:


import matplotlib.pyplot as plt


# In[100]:


from deepface import DeepFace


# In[111]:
"""
Here I will Add the Capture.py code 
so that i can capture the images and 
store in a file. Later that image will 
be use for detecting the emotion of a 
person
"""

## Implementing Capture.py Functions

"""
The Capture.py is divided into 2 sections 
section1:- Image will be capture with the help of 
camera
Section2:- In this stored image will be taken and 
only face is croped and stroed in same dataset
"""

## Section 1

def capture():
    path = os.path.dirname(os.path.abspath(__file__))

    cam  = cv2.VideoCapture(0)

    while True:
       ret, frame = cam.read()
    
       if not ret:
          print('Fail to grab frame')
          break
       
       
       cv2.imshow('test',frame)   
    
       k = cv2.waitKey(1)
    
       os.chdir('F:\FACE\dataset')
       img_name = "himan.jpg"
       cv2.imwrite(img_name,frame)
    
    
       cam.release()
       cv2.destroyAllWindows()
       break

## Section2
    im = cv2.imread('F:\FACE\dataset\himan.jpg')

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier('F:\FACE\haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
       cv2.rectangle(im, (x, y), (x+w, y+h), (0, 0, 255), 2)
       faces = im[y:y + h, x:x + w]
       cv2.imwrite('himan.jpg', faces)
    

    cv2.waitKey()
    cam.release()




####################################################################################3


#for i in range(0,3):
capture()
img = cv2.imread('F:\FACE\dataset\himan.jpg')


plt.imshow(img)
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img2)





p = DeepFace.analyze(img2)
print(p)

print(p['dominant_emotion'])



