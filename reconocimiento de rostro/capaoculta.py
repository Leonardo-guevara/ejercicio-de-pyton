import cv2
import os 
import numpy as np
from time import time
import imutils
# import face_recognition as face

path = 'reconocimiento de rostro/location'
lista_path = os.listdir(path)

def entre():
    ids =[]
    rostro_data=[]
    id = 0
    time_inicial = time()
    for fila in lista_path:
        rutaocompleta=path+'/'+fila
        print('iniciar la lectura..')
        for archivo in os.listdir(rutaocompleta):
            ids.append(id)
            rostro_data.append(cv2.imread(rutaocompleta+'/'+archivo,0 ))
        id =1 + id
        time_final = time()
        time_total = time_final - time_inicial
        print('time : ' , time_final,'imagen: ', fila+'/'+archivo,0)
        
    recognise = cv2.face.EigenFaceRecognizer_create()  
    # recognise = cv2.face.LBPHFaceRecognizer_create()
    print('iniciado')
    recognise.train(rostro_data,np.array(ids))
    recognise.write('reconocimiento de rostro/trainingDataEigan.xml')
    print('finalizado')
    # recognise.read("Recogniser/trainingDataEigan.xml")
            
            
entre()
