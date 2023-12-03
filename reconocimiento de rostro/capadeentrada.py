import cv2 
# import numpy as np
import os  
import imutils


# face_cascade = cv2.CascadeClassifier('E:\Proyecto en git\pyton\ejercicio-de-pyton\opencv-4.x\data\haarcascades\haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier('opencv-4.x\data\haarcascades\haarcascade_frontalface_default.xml')


# TODO: bucar rostro
def buscar_rostro():
    face_cascade = cv2.CascadeClassifier('opencv-4.x\data\haarcascades\haarcascade_frontalface_default.xml')

    camara = cv2.VideoCapture(1)
    while True: 
        _,captura =camara.read()
        captura=imutils.resize(captura,width=720)
        gray = cv2.cvtColor(captura, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for(x,y,e1,e2)  in faces:
            cv2.rectangle(captura,(x,y),(x+e1,y+e2),(0,255,0),2)
        cv2.imshow('mostrar imagen ',captura)
        if cv2.waitKey(1) == ord('q'):
            break
    camara.release()
    cv2.destroyAllWindows()
    

# TODO: bucar rostro
def captura(name, ruta):
    face_cascade = cv2.CascadeClassifier('opencv-4.x\data\haarcascades\haarcascade_frontalface_default.xml')
    modelo = 'photo'
    patch = 'reconocimiento de rostro/location' +'/'+ name
    
    if not os.path.exists(patch) :
        os.makedirs(patch)
    id= 1   
    view = ruta
    camara = cv2.VideoCapture(view)
    print(view)
    while True:
        respuesta,captura =camara.read()
        if respuesta == False: break
        # bajara la resolucion
        captura=imutils.resize(captura,width=720)
        gray = cv2.cvtColor(captura, cv2.COLOR_BGR2GRAY)
        idcapture = captura.copy()
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for(x,y,e1,e2)  in faces:
            cv2.rectangle(captura,(x,y),(x+e1,y+e2),(0,255,0),2)
            rostro = idcapture[y:y+e2, x:x+e1]
            rostro=cv2.resize(captura,(720,720),interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(patch+'/imagen_{}.jpg'.format(id),rostro)
            id = id + 1
        cv2.imshow('mostrar imagen ',captura)
        if  id == 250:
            break
    camara.release()
    cv2.destroyAllWindows()
        
# print(face_cascade)
# captura('Elon_Musk ','reconocimiento de rostro\ElonMusk.mp4')
buscar_rostro()
    

