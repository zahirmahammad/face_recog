import face_recognition
import cv2
import os
import imutils
import numpy as np
from tqdm import tqdm

mylist=os.listdir('faces')
names=[]
images=[]
for name in (mylist):
    names.append(os.path.splitext(name)[0])


myencodelist=np.load('encodings.npy')
vid=cv2.VideoCapture(0+cv2.CAP_DSHOW)

while True:
    _,video=vid.read()
    show_name='NONE'
    video=imutils.resize(video, width=500)
    vidcvt=cv2.cvtColor(video,cv2.COLOR_BGR2RGB)
    faces=face_recognition.face_locations(vidcvt)
    encode_face=face_recognition.face_encodings(vidcvt)
    for i, j in zip(faces, encode_face):
        results=[]
        cv2.rectangle(video, (i[3],i[0]),(i[1],i[2]),(255,0,0),2)
        for k in myencodelist:
            result=face_recognition.compare_faces([j],k)
            results.append(result)
        if [True] in results:
            index=results.index([True])
            show_name=names[index]
            cv2.putText(video ,show_name, (i[3]+6,i[0]-6),cv2.FONT_HERSHEY_PLAIN,1.0, (255,0,0), 2)
        else:
            cv2.putText(video ,show_name, (i[3]+6,i[0]-6),cv2.FONT_HERSHEY_PLAIN,1.0, (255,0,0), 2)
        print(results)
    cv2.imshow('ok', video)
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
vid.release()
cv2.destroyAllWindows()

