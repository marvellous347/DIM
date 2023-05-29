import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
from math import sqrt, exp 
plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False) 
img = cv2.imread("Lab8\Grayscale.jpg", 0) 
plt.subplot(151), plt.imshow(img, "gray"), plt.title("Original Image") 
 
original = np.fft.fft2(img) 
plt.subplot(152), plt.imshow(np.log(1 + np.abs(original)), "gray"), plt.title("Spectrum") 
 
center = np.fft.fftshift(original) 
plt.subplot(153), plt.imshow(np.log(1 + np.abs(center)), "gray"), plt.title("Centered Spectrum") 
 
inv_center = np.fft.ifftshift(center) 
plt.subplot(154), plt.imshow(np.log(1 + np.abs(inv_center)), "gray"), plt.title("Decentralized") 
 
processed_img = np.fft.ifft2(inv_center) 
plt.subplot(155), plt.imshow(np.abs(processed_img), "gray"), plt.title("Processed Image") 
 
plt.show() 
 
plt.figure(figsize=(6.4 * 5, 4.8 * 5), constrained_layout=False) 
 
plt.subplot(131), plt.imshow(np.log(np.abs(original)), "gray"), plt.title("Spectrum") 
 
plt.subplot(132), plt.imshow(np.angle(original), "gray"), plt.title("Phase Angle") 
plt.show() 
 
def distance(point1, point2): 
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) 
 
def idealFilterLP(D0, imgShape): 
    base = np.zeros(imgShape[:2]) 
    rows, cols = imgShape[:2] 
    center = (rows / 2, cols / 2) 
    for x in range(cols): 
        for y in range(rows): 
            if distance((y, x), center) < D0: 
                base[y, x] = 1 
    return base 
 
def idealFilterHP(D0, imgShape): 
    base = np.ones(imgShape[:2]) 
    rows, cols = imgShape[:2] 
    center = (rows / 2, cols / 2) 
    for x in range(cols): 
        for y in range(rows): 
            if distance((y, x), center) < D0: 
                base[y, x] = 0 
    return base 
 
#def butterworthLP(D0, imgShape, n): 
    #base = np.zeros(imgShape[:2]) 
    #rows, cols = imgShape[:2] 
    #center = (rows / 2, cols / 2) 
    #for x in range(cols): 
       # for y in range(rows): 
            #base[y, x] = 1 / (1 + (distance((y, x), center) / D0) ** (2 * n)) 
    #return base 
 
 
#def butterworthHP(D0, imgShape, n): 
   # base = np.zeros(imgShape[:2]) 
    #rows, cols = imgShape[:2] 
    #center = (rows / 2, cols / 2) 
    #for x in range(cols): 
        #for y in range(rows): 
            #base[y, x] = 1 - 1 / (1 + (distance((y, x), center) / D0) ** (2 * n)) 
    #return base 
 
 
#def gaussianLP(D0, imgShape): 
    #base = np.zeros(imgShape[:2]) 
    #rows, cols = imgShape[:2] 
    #center = (rows / 2, cols / 2) 
    #for x in range(cols): 
        #for y in range(rows): 
            #base[y, x] = exp(((-distance((y, x), center) ** 2) / (2 * (D0 ** 2)))) 
    #return base 
 
def gaussianHP(D0, imgShape): 
    base = np.zeros(imgShape[:2]) 
    rows, cols = imgShape[:2] 
    center = (rows / 2, cols / 2) 
    for x in range(cols): 
        for y in range(rows): 
            base[y, x] = 1 - exp(((-distance((y, x), center) ** 2) / (2 * (D0 ** 2)))) 
    return base 
 
plt.figure(figsize=(6.4 * 5, 4.8 * 5), constrained_layout=False) 
 
plt.subplot(161), plt.imshow(img, "gray"), plt.title("Original Image") 
 
original = np.fft.fft2(img) 
plt.subplot(162), plt.imshow(np.log(1 + np.abs(original)), "gray"), plt.title("Spectrum") 
 
center = np.fft.fftshift(original) 
plt.subplot(163), plt.imshow(np.log(1 + np.abs(center)), "gray"), plt.title("Centered Spectrum") 
 
LowPassCenter = center * idealFilterLP(50, img.shape) 
plt.subplot(164), plt.imshow(np.log(1 + np.abs(LowPassCenter)), "gray"), plt.title( 
   "Centered Spectrum multiply Low Pass Filter") 
 
LowPass = np.fft.ifftshift(LowPassCenter) 
plt.subplot(165), plt.imshow(np.log(1 + np.abs(LowPass)), "gray"), plt.title("Decentralize") 
 
inverse_LowPass = np.fft.ifft2(LowPass) 
plt.subplot(166), plt.imshow(np.abs(inverse_LowPass), "gray"), plt.title("Processed Image") 
 
plt.show() 
 
plt.figure(figsize=(6.4 * 5, 4.8 * 5), constrained_layout=False) 
 
plt.subplot(151), plt.imshow(np.log(1 + np.abs(center)), "gray"), plt.title("Spectrum") 
 
LowPass = idealFilterLP(50, img.shape) 
plt.subplot(152), plt.imshow(np.abs(LowPass), "gray"), plt.title("Low Pass Filter") 
 
LowPassCenter = center * idealFilterLP(50, img.shape) 
plt.subplot(153), plt.imshow(np.log(1 + np.abs(LowPassCenter)), "gray"), plt.title( 
   "Centered Spectrum multiply Low Pass Filter") 
 
LowPass = np.fft.ifftshift(LowPassCenter) 
plt.subplot(154), plt.imshow(np.log(1 + np.abs(LowPass)), "gray"), plt.title("Decentralize") 
 
inverse_LowPass = np.fft.ifft2(LowPass) 
plt.subplot(155), plt.imshow(np.abs(inverse_LowPass), "gray"), plt.title("Processed Image") 
 
plt.show() 
 
plt.figure(figsize=(6.4 * 5, 4.8 * 5), constrained_layout=False) 
 
plt.subplot(151), plt.imshow(np.log(1 + np.abs(center)), "gray"), plt.title("Spectrum") 
 
HighPass = idealFilterHP(50, img.shape) 
plt.subplot(152), plt.imshow(np.abs(HighPass), "gray"), plt.title("High Pass Filter") 
 
HighPassCenter = center * idealFilterHP(50, img.shape) 
plt.subplot(153), plt.imshow(np.log(1 + np.abs(HighPassCenter)), "gray"), plt.title( 
    "Centered Spectrum multiply High Pass Filter") 
 
HighPass = np.fft.ifftshift(HighPassCenter) 
plt.subplot(154), plt.imshow(np.log(1 + np.abs(HighPass)), "gray"), plt.title("Decentralize") 
 
inverse_HighPass = np.fft.ifft2(HighPass) 
plt.subplot(155), plt.imshow(np.abs(inverse_HighPass), "gray"), plt.title("Processed Image") 
 
plt.show() 
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
from math import sqrt, exp 
 
plt.figure(figsize=(6.4 * 5, 4.8 * 5), constrained_layout=False) 
 
#img = cv2.imread("D:\LNU\Grayscale.jpg", 0)
img = cv2.imread("Lab8\Grayscale.jpg", 0) 
plt.subplot(151), plt.imshow(img, "gray"), plt.title("Original Image") 
 
original = np.fft.fft2(img) 
plt.subplot(152), plt.imshow(np.log(1 + np.abs(original)), "gray"), plt.title("Spectrum") 
 
center = np.fft.fftshift(original) 
#plt.subplot(153), plt.imshow(np.log(1 + np.abs(center)), "gray"), plt.title("Centered Spectrum") 
 
inv_center = np.fft.ifftshift(center) 
plt.subplot(154), plt.imshow(np.log(1 + np.abs(inv_center)), "gray"), plt.title("Decentralized") 
 
processed_img = np.fft.ifft2(inv_center) 
plt.subplot(155), plt.imshow(np.abs(processed_img), "gray"), plt.title("Processed Image") 
 
plt.show() 
 
plt.figure(figsize=(6.4 * 5, 4.8 * 5), constrained_layout=False) 
 
plt.subplot(131), plt.imshow(np.log(np.abs(original)), "gray"), plt.title("Spectrum") 
 
plt.subplot(132), plt.imshow(np.angle(original), "gray"), plt.title("Phase Angle") 
plt.show() 
 
 
def distance(point1, point2): 
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) 
 
 
def idealFilterLP(D0, imgShape): 
    base = np.zeros(imgShape[:2]) 
    rows, cols = imgShape[:2] 
    center = (rows / 2, cols / 2) 
    for x in range(cols): 
        for y in range(rows): 
            if distance((y, x), center) < D0: 
                base[y, x] = 1 
    return base 
 
 
def idealFilterHP(D0, imgShape): 
    base = np.ones(imgShape[:2]) 
    rows, cols = imgShape[:2] 
    center = (rows / 2, cols / 2) 
    for x in range(cols): 
        for y in range(rows): 
            if distance((y, x), center) < D0: 
                base[y, x] = 0 
    return base 
 
 
def butterworthLP(D0, imgShape, n): 
    base = np.zeros(imgShape[:2]) 
    rows, cols = imgShape[:2] 
    center = (rows / 2, cols / 2) 
    for x in range(cols): 
        for y in range(rows): 
            base[y, x] = 1 / (1 + (distance((y, x), center) / D0) ** (2 * n)) 
    return base 
 
 
def butterworthHP(D0, imgShape, n): 
    base = np.zeros(imgShape[:2]) 
    rows, cols = imgShape[:2] 
    center = (rows / 2, cols / 2) 
    for x in range(cols): 
        for y in range(rows): 
            base[y, x] = 1 - 1 / (1 + (distance((y, x), center) / D0) ** (2 * n)) 
    return base 
 
 
def gaussianLP(D0, imgShape): 
    base = np.zeros(imgShape[:2]) 
    rows, cols = imgShape[:2] 
    center = (rows / 2, cols / 2) 
    for x in range(cols): 
        for y in range(rows): 
            base[y, x] = exp(((-distance((y, x), center) ** 2) / (2 * (D0 ** 2)))) 
    return base 
 
 
def gaussianHP(D0, imgShape): 
    base = np.zeros(imgShape[:2]) 
    rows, cols = imgShape[:2] 
    center = (rows / 2, cols / 2) 
    for x in range(cols): 
        for y in range(rows): 
            base[y, x] = 1 - exp(((-distance((y, x), center) ** 2) / (2 * (D0 ** 2)))) 
    return base 
 
 
plt.figure(figsize=(6.4 * 5, 4.8 * 5), constrained_layout=False) 
 
plt.subplot(161), plt.imshow(img, "gray"), plt.title("Original Image") 
 
original = np.fft.fft2(img) 
plt.subplot(162), plt.imshow(np.log(1 + np.abs(original)), "gray"), plt.title("Spectrum") 
 
center = np.fft.fftshift(original) 
plt.subplot(163), plt.imshow(np.log(1 + np.abs(center)), "gray"), plt.title("Centered Spectrum") 
 
LowPassCenter = center * idealFilterLP(50, img.shape) 
plt.subplot(164), plt.imshow(np.log(1 + np.abs(LowPassCenter)), "gray"), plt.title( 
    "Centered Spectrum multiply Low Pass Filter") 
 
LowPass = np.fft.ifftshift(LowPassCenter) 
plt.subplot(165), plt.imshow(np.log(1 + np.abs(LowPass)), "gray"), plt.title("Decentralize") 
 
inverse_LowPass = np.fft.ifft2(LowPass) 
plt.subplot(166), plt.imshow(np.abs(inverse_LowPass), "gray"), plt.title("Processed Image") 
 
plt.show() 
 
plt.figure(figsize=(6.4 * 5, 4.8 * 5), constrained_layout=False) 
 
plt.subplot(151), plt.imshow(np.log(1 + np.abs(center)), "gray"), plt.title("Spectrum") 
 
LowPass = idealFilterLP(50, img.shape) 
plt.subplot(152), plt.imshow(np.abs(LowPass), "gray"), plt.title("Low Pass Filter") 
 
LowPassCenter = center * idealFilterLP(50, img.shape) 
plt.subplot(153), plt.imshow(np.log(1 + np.abs(LowPassCenter)), "gray"), plt.title( 
    "Centered Spectrum multiply Low Pass Filter") 
 
LowPass = np.fft.ifftshift(LowPassCenter) 
plt.subplot(154), plt.imshow(np.log(1 + np.abs(LowPass)), "gray"), plt.title("Decentralize") 
 
inverse_LowPass = np.fft.ifft2(LowPass) 
plt.subplot(155), plt.imshow(np.abs(inverse_LowPass), "gray"), plt.title("Processed Image") 
 
plt.show() 
 
plt.figure(figsize=(6.4 * 5, 4.8 * 5), constrained_layout=False) 
 
plt.subplot(151), plt.imshow(np.log(1 + np.abs(center)), "gray"), plt.title("Spectrum") 
 
HighPass = idealFilterHP(50, img.shape) 
plt.subplot(152), plt.imshow(np.abs(HighPass), "gray"), plt.title("High Pass Filter") 
 
HighPassCenter = center * idealFilterHP(50, img.shape) 
plt.subplot(153), plt.imshow(np.log(1 + np.abs(HighPassCenter)), "gray"), plt.title( 
    "Centered Spectrum multiply High Pass Filter") 
 
HighPass = np.fft.ifftshift(HighPassCenter) 
plt.subplot(154), plt.imshow(np.log(1 + np.abs(HighPass)), "gray"), plt.title("Decentralize") 
 
inverse_HighPass = np.fft.ifft2(HighPass) 
plt.subplot(155), plt.imshow(np.abs(inverse_HighPass), "gray"), plt.title("Processed Image") 
 
plt.show() 

 