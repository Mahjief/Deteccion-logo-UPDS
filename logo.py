import numpy as np
import cv2

logo = cv2.CascadeClassifier('./prueba.xml')

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('upds.mp4')


while True:
    # img: variable de tipo Mat -> array

    #print("Camara")
    ret, img = cap.read()   

    # ESCALA DE GRISES
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('foto1',grayImage)
    

    logos = logo.detectMultiScale(grayImage,scaleFactor=1.5,minNeighbors=2, minSize=(20,20), maxSize=(500,500))
    for (x,y,w,h) in logos:
        cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,255),2)
    
    cv2.imshow("FOTO",img)

    k=cv2.waitKey(30) & 0xff
    if k == 27:
        break


    #print("Mostrando")



cap.release()
cv2.destroyAllWindows()