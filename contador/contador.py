import cv2
import numpy as np


original = cv2.imread('monedas.jpg')

# TODO:  CREAR IMAGENS EN GRISES
def grises(args):
    gris=cv2.cvtColor(args,cv2.COLOR_BGR2GRAY)
    cv2.imshow('imagen gris', gris)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# TODO:  ELIMINAR RUIDO DE IMAGEN 
def ruido(args):
    valorgauss =3
    valorKernel =3
    gauss = cv2.GaussianBlur(args,(valorgauss,valorKernel),sigmaX=10)
    # gauss = cv2.GaussianBlur(args,ksize=3,sigmaX=10)
    cv2.imshow('imagen de ruido', gauss)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# TODO:  RECONOCE LOS BORDE
def borde(args):
    valorgauss =3
    valorKernel =3
    kernerl = np.ones(args,(valorKernel,valorKernel),np.uint8)
    canny = cv2.Canny(args,80,100)
    cv2.imshow('imagen de ruido', canny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
# TODO:  selecionar los controrno
def morphological(args):
    valorgauss =1
    valorKernel =3
    gris=cv2.cvtColor(args,cv2.COLOR_BGR2GRAY)
    gauss = cv2.GaussianBlur(gris,(valorgauss,valorgauss),sigmaX=10)
    canny = cv2.Canny(gauss,60,100)
    kernel = np.ones((valorKernel,valorKernel),np.uint8)
    cierre = cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)
    contorno,jerarquia = cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    print('moneda encontrada : {}'.format(len(contorno)))
    view = cv2.drawContours(args,contorno,-1,(0,0,255),2)
    cv2.imshow('TRANSFORMACION MORFOLOGICA', view)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
morphological(original)