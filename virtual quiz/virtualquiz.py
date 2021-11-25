import cv2
import csv

cap=cv2.VideoCapture(0)
cap.set(3,1200)
cap.set(4,720)


while True:
    success, img=cap.read()
    img = cv2.flip(img,1)
    cv2.imshow("Img",img)
    cv2.waitKey(1)
