#!/usr/bin/env python
# coding: utf-8

# In[98]:


import cv2
import face_recognition
from  PIL import Image


# In[99]:


import matplotlib.pyplot as plt


# In[100]:


from deepface import DeepFace


# In[111]:


img = cv2.imread('F:\FACE\dataset\himan.jpg')


# In[112]:


plt.imshow(img)


# In[103]:


img2 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


# In[104]:


plt.imshow(img2)


# In[105]:


#img3 = face_recognition.load_image_file('F:\Face Emotion\index1.jpg')
#face_locations = face_recognition.face_locations(img3)


# In[106]:


#face_locations


# In[107]:


""""top, right, bottom, left = face_locations[0]
face_img1 = image[top:bottom,left:right]
plt.imshow(face_img1)
image_save = Image.fromarray(face_img1)
image_save.save('img1.jpg')"""


# In[108]:


p = DeepFace.analyze(img2)


# In[109]:


print(p)


# In[110]:


print(p['dominant_emotion'])


# In[ ]:




