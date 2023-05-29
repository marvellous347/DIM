import cv2
import numpy as np

path = 'Lab1\image.png'
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
cv2.imshow('Lab1\image.png', img)
c = cv2.bitwise_not(img)
cv2.imshow('c', c)
d = 255 / np.log(1 + np.max(img))
log_image = d * (np.log(img + 1))
log_image = np.array(log_image, dtype=np.uint8)
cv2.imshow('d', log_image)
e = np.power(img, 0.8)
e = np.array(e, dtype=np.uint8)
cv2.imshow('e', e)
cv2.waitKey(0)