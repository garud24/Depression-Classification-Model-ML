import cv2
import os
import time
path = os.path.dirname(os.path.abspath(__file__))

cam  = cv2.VideoCapture(0)

#cv2.namedWindow('Screen Shot')


ele = 0
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
"""      while True:
        ele +=1
        if ele==10:
           print("Escape Hit ")
           cam.release()
           #cv2.destroyAllWindows()
           break
        else:
           os.chdir('F:\FACE\dataset')
           img_name = "himan.jpg"
           cv2.imwrite(img_name,frame)"""
   
        #cv2.imwrite(dataset/img_name,frame)   


###################################################################
"""
count = 0
while True:
    ret, frame =cam.read()
    face_cascade = cv2.CascadeClassifier('F:\FACE\haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1, 4)
    
    for(x,y,w,h) in faces:
        #cv2.imwrite("dataset/face-"+name +'.'+ str(i) + ".jpg")#, gray[y-offset:y+h+offset,x-offset:x+w+offset])
        cv2.rectangle(frame,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        
        #display
        cv2.imshow('im',frame)
        t= time.strftime("%Y-%m-%d_%H-%M-%S")
        os.chdir('F:\FACE\dataset')
        img_name = "himan.jpg"
        cv2.imwrite(img_name,frame)
        count +=1
        
        cv2.waitKey(1)
        if count==1:
            cam.release()
            cv2.destroyAllWindows()
            break 
############################################################################        





"""


        
# Second Section
im = cv2.imread('F:\FACE\dataset\himan.jpg')

# Converting the image into gray scale image
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

#Loading the haar cascade  file
face_cascade = cv2.CascadeClassifier('F:\FACE\haarcascade_frontalface_default.xml')

#Detect the faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces and crop the faces
for (x, y, w, h) in faces:
    cv2.rectangle(im, (x, y), (x+w, y+h), (0, 0, 255), 2)
    faces = im[y:y + h, x:x + w]
    #cv2.imshow("face",faces)
    cv2.imwrite('himan.jpg', faces)
    
# Display the output
#cv2.imwrite('detcted.jpg', im)
#cv2.imshow('img', im)
cv2.waitKey()
#image_counter +=1

#if image_counter ==1:
cam.release()
#cam.destroyAllWindows()

    