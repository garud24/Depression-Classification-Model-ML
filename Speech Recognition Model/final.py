#!/usr/bin/env python
# coding: utf-8

# In[1]:


import librosa
import soundfile
import os,glob,pickle
import numpy as np
import speech_recognition as sr
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


# In[2]:


#DataFlair - Extract features (mfcc, chroma, mel) from a sound file
def extract_feature(file_name, mfcc, chroma, mel):
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate=sound_file.samplerate
        if chroma:
            stft=np.abs(librosa.stft(X))
        result=np.array([])
        if mfcc:
            mfccs=np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            result=np.hstack((result, mfccs))
        if chroma:
            chroma=np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
            result=np.hstack((result, chroma))
        if mel:
            mel=np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
            result=np.hstack((result, mel))
    return result


# In[3]:


#DataFlair - Emotions in the RAVDESS dataset
emotions={
  '01':'neutral',
  '02':'calm',
  '03':'happy',
  '04':'sad',
  '05':'angry',
  '06':'fearful',
  '07':'disgust',
  '08':'surprised'
}

#DataFlair - Emotions to observe
observed_emotions=['calm', 'happy', 'fearful', 'disgust']


# In[4]:


#DataFlair - Load the data and extract features for each sound file
def load_data(test_size=0.2):
    x,y=[],[]
    for file in glob.glob("F:\Project\TRAINING_FILES_PATH\Actor_*\\*.wav"):
        file_name=os.path.basename(file)
        emotion=emotions[file_name.split("-")[2]]
        if emotion not in observed_emotions:
            continue
        feature=extract_feature(file, mfcc=True, chroma=True, mel=True)
        x.append(feature)
        y.append(emotion)
    return train_test_split(np.array(x), y, test_size=test_size, random_state=9)


# In[5]:


# Listning to the microphone and giving this output as an input to feature extractor
os.chdir('F:\Project\SpeechDataset')
r= sr.Recognizer()
with sr.Microphone() as source:
    print('Say Something')
    audio = r.listen(source)
    
    with open('speech.wav','wb') as f:
        f.write(audio.get_wav_data())
    


# In[6]:


file = "F:\Project\SpeechDataset\speech.wav"    
feature = extract_feature(file, mfcc=True, chroma= True, mel=True)   


# In[7]:


#DataFlair - Split the dataset
x_train,x_test,y_train,y_test=load_data(test_size=0.25)
print(x_train)
print(x_test)
print(y_train)
print(y_test)


# In[8]:


#DataFlair - Get the shape of the training and testing datasets
print((x_train.shape[0], x_test.shape[0]))


# In[9]:


#DataFlair - Get the number of features extracted
print(f'Features extracted: {x_train.shape[1]}')


# In[10]:


#DataFlair - Initialize the Multi Layer Perceptron Classifier
model=MLPClassifier(alpha=0.01, batch_size=256, epsilon=1e-08, hidden_layer_sizes=(300,), learning_rate='adaptive', max_iter=500)


# In[11]:


#DataFlair - Train the model
model.fit(x_train,y_train)


# In[12]:


#DataFlair - Predict for the test set
y_pred=model.predict(x_test)
y_pre=model.predict([feature])
print(y_pre)


# In[13]:


#DataFlair - Calculate the accuracy of our model
accuracy=accuracy_score(y_true=y_test, y_pred=y_pred)

#DataFlair - Print the accuracy
print("Accuracy: {:.2f}%".format(accuracy*100))


# In[ ]:




