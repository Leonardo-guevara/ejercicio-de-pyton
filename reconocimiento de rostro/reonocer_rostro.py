import cv2
import os 
import numpy as np
from time import time
import imutils
# import face_recognition as face

path = 'reconocimiento de rostro/location'
# reconocimiento de rostro\trainingDataEigan.xml
lista_path = os.listdir(path)
# ruidos 
face_cascade = cv2.CascadeClassifier('opencv-4.x/data/haarcascades/haarcascade_frontalface_default.xml')


def view(path,lista_path,face_cascade):
  
  FaceRecognoizer =cv2.face.EigenFaceRecognizer_create() 
  FaceRecognoizer.read('trainingDataEigan.xml')
  camara = cv2.VideoCapture('Gabriel_levinas.MP4')
  while True:
    respuesta,captura =camara.read()
    if respuesta == False: break
    # bajara la resolucion
    captura=imutils.resize(captura,width=720)
    gray = cv2.cvtColor(captura, cv2.COLOR_BGR2GRAY)
    idcapture = captura.copy()
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x,y,e1,e2)  in faces:
      rostro = idcapture[y:y+e2, x:x+e1]
      rostro=cv2.resize(captura,(160,160),interpolation=cv2.INTER_CUBIC)
      resul= FaceRecognoizer.predict(rostro)
      # cv2.putText(captura,'{}'.format(resul),(x,y-5),(1,1.3),(0,255,0),1,cv2.LINE_AA)
      if resul[1]<8000:
        cv2.putText(captura, '{}'.format(lista_path[resul[0]]), (x,y-20), 2,1.1,(0,255,0),1,cv2.LINE_AA)
        cv2.rectangle(captura, (x,y), (x+e1,y+e2), (255,0,0),2)
      else:
        cv2.putText(captura,"No encontrado", (x,y-20), 2,0.7,(0,255,0),1,cv2.LINE_AA)
        cv2.rectangle(captura, (x,y), (x+e1,y+e2), (255,0,0),2)
    cv2.imshow('mostrar entrenamiento ',captura)  
    if(cv2.waitKey(1) == ord('s')):break
  camara.release()
  cv2.destroyAllWindows()

view(path,lista_path,face_cascade)
  