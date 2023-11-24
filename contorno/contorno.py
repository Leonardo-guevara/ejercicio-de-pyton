
import  cv2
# import numpy as np 

contorno = cv2.imread('contorno.jpg')
# TODO: Mostrar imagenes   
# status : hecho
def imagen(image):
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

   
# TODO: Crear escala gris
# status : hecho
def grises(path):
    img = cv2.cvtColor(path, cv2.COLOR_BGR2GRAY)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# TODO: Crear contorno
# status : hecho
def contours(path):
    img =cv2.cvtColor(path,cv2.COLOR_BGR2GRAY)
    _,umbral=cv2.threshold(img,100,255,cv2.THRESH_BINARY)
    contorno,jerarquía = cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(path,contorno,-1,(251, 63, 52),3)
    cv2.imshow('contours', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# TODO: picture display show 
contours(contorno)


