import cv2
import numpy as np
import matplotlib.pyplot as plt
import random


def Gauss_noise(image, sigma):
    img = image.astype(np.int16)
    mu = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                img[i, j, k] = img[i, j, k] + random.gauss(mu=mu, sigma=sigma)
        img[img > 255] = 255
        img[img < 0] = 0
        img = img.astype(np.uint8)
        return img

def Arithmetic_algorithm(image):
    #Arithmetic mean filtering
    new_image = np.zeros(image.shape)
    image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_DEFAULT)
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            new_image[i - 1, j - 1] = np.mean(image[i - 1:i + 2, j - 1:j + 2])
    new_image = (new_image - np.min(image)) * (255/ np.max(image))
    return new_image.astype(np.uint8)


def Arithmetic_rgb(image):
    r, g, b = cv2.split(image)
    r = Arithmetic_algorithm(r)
    g = Arithmetic_algorithm(g)
    b = Arithmetic_algorithm(b)
    return cv2.merge([r, g, b])


def Geometric_operator(roi):
    roi = roi.astype(np.float64)
    p = np.prod(roi)
    return p ** (1 / (roi.shape[0] * roi.shape[1]))


def Geometric_algorithm(image):
    #Geometric mean filter
    new_image = np.zeros(image.shape)
    image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_DEFAULT)
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            new_image[i - 1, j - 1] = Geometric_operator(image[i - 1:i + 2, j - 1:j + 2])
    new_image = (new_image - np.min(image)) * (255 / np.max(image))
    return new_image.astype(np.uint8)


def Geometric_rgb(image):
    r, g, b = cv2.split(image)
    r = Geometric_algorithm(r)
    g = Geometric_algorithm(g)
    b = Geometric_algorithm(b)
    return cv2.merge([r, g, b])


if __name__ == '__main__':
    image = cv2.imread('Labs\Lab10\img.jpg')
    image = cv2.resize(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), (274, 285))
    plt.imshow(image)
    plt.axis("off")
    plt.title("Original Image")
    plt.show()

    Gauss = Gauss_noise(image, 18)
    plt.imshow(Gauss)
    plt.axis("off")
    plt.title("Gauss noise Image")
    plt.show()

    plt.imshow(Arithmetic_rgb(Gauss))
    plt.title("Arithmetic Filter")
    plt.show()

    plt.imshow(Geometric_rgb(Gauss))
    plt.title("Geometric Filter")
    plt.show()