import matplotlib.pyplot as plt

plt.rc('xtick', labelsize=4.5)
plt.rc('ytick', labelsize=4.5)
plt.rc('axes', titlesize=6)

import numpy as np
from scipy import ndimage
from PIL import Image
def plot(data, title):
    plot.i += 1
    plt.subplot(3,3,plot.i)
    plt.imshow(data)
    plt.gray()
    plt.title(title)
plot.i = 0
#im1 = Image.open('Labs\Lab2\q1.png')
im1 = Image.open('Lab2\q2.png')
im = im1.convert('L')
data = np.array(im, dtype=float)
plot(im, 'Original')

kernel = np.array([[1, 2, 1],
                   [2,  4, 2],
                   [1, 2, 1]])
highpass_3x3 = ndimage.convolve(data, kernel)
plot(highpass_3x3, 'Gauss Low Pass Filter (3x3)')
kernel = np.array([[2, 7, 12, 7, 2],
                   [7, 31, 52, 31, 7],
                   [12, 52, 127, 52, 12],
                   [7, 31, 52, 31, 7],
                   [2, 7, 12, 7, 2]])
highpass_3x3 = ndimage.convolve(data, kernel)
plot(highpass_3x3, 'Gauss Low Pass Filter (5x5)')

kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])
highpass_3x3 = ndimage.convolve(data, kernel)
plot(highpass_3x3, 'Laplace High Pass Filter (3x3)')

kernel = np.array([[-1, -3, -4, -3, -1],
                   [-3, 0, 6, 0, -3],
                   [-4, 6, 20, 6, -4],
                   [-3, 0, 6, 0, -3],
                   [-1, -3, -4, -3, -1]])
highpass_3x3 = ndimage.convolve(data, kernel)
plot(highpass_3x3, 'Laplace High Pass Filter (5x5)')

kernel2 = np.array([[-1, 0, 1],
                   [-1,  0,  1],
                   [-1,  0,  1]])
highpass_5x5 = ndimage.convolve(data, kernel2)
plot(highpass_5x5, 'Prewitt Gradient Filter (vertical)')

kernel2 = np.array([[1, 1, 1],
                   [0,  0,  0],
                   [-1, - 1,  -1]])
highpass_5x5 = ndimage.convolve(data, kernel2)
plot(highpass_5x5, 'Prewitt Gradient Filter (horizontal)')

kernel2 = np.array([[-1, 0, 1],
                   [-2,  0,  2],
                   [-1,  0,  1]])
highpass_5x5 = ndimage.convolve(data, kernel2)
plot(highpass_5x5, 'Sobel Gradient Filter (vertical)')

kernel2 = np.array([[1, 2, 1],
                   [0,  0,  0],
                   [-1, -2,  -1]])
highpass_5x5 = ndimage.convolve(data, kernel2)
plot(highpass_5x5, 'Sobel Gradient Filter (horizontal)')

plt.show()
