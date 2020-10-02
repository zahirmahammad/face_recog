import face_recognition
import os
import glob2
import cv2
import numpy as np
import tqdm


ok=glob2.glob('faces\*.jpg')
print(len(ok))
array=np.zeros((len(ok), 128))
for j,i in enumerate(ok):
    encode=[]
    img=face_recognition.load_image_file(i)
    cvt=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    face=face_recognition.face_encodings(cvt)[0]
    array[j,:]=face
np.save('encodings.npy', array)

