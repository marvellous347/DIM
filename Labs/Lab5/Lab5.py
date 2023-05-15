import numpy as np 
import random 
import math 
import cv2 
from matplotlib import pyplot as plt 

#img read
logo = cv2.imread("D:\LNU\logo.png") 
img = cv2.imread("D:\LNU\img.jpg") 

#Отримую розміри зчитаних зображень
(wH, wW) = logo.shape[:2] 
(h, w) = img.shape[:2]

#Визначення області "Destination" на основному зображенні, до якого буде накладений водяний знак
destination = img[h - wH - 10:h - 10, w - wW - 10:w - 10]

#Накладання водяного знаку
result = cv2.addWeighted(destination, 1, logo, 0.7, 0) 
img[h - wH - 10:h - 10, w - wW - 10:w - 10] = result 

#Збереження зображення з водяним знаком
cv2.imwrite("ЦОЗ\Labs\Lab5\watermarked.jpg", img)

#Відображення зображення
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
plt.imshow(RGB_img) 
plt.show() 