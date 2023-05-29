import cv2
import numpy as np

def form(file):
    def gaus_noise(img):
        row, col, ch = img.shape
        mean = 100
        var = 0.6
        sigma = var ** 0.5
        gauss = np.random.normal(mean, sigma, (row, col, ch))
        gauss = gauss.reshape(row, col, ch)
        noisy = img + gauss
        return noisy

    def exp_noise(img):
        row, col, ch = img.shape
        mean = 100
        expo = np.random.exponential(mean, (row, col, ch))
        expo = expo.reshape(row, col, ch)
        noisy = img + expo
        return noisy

    def save_file():
        image = cv2.imread(file)
        images = [gaus_noise(image), exp_noise(image)]
        names = ['Labs\Lab9\gauss.jpg', 'Labs\Lab9\exp.jpg']
        [cv2.imwrite(name, img) for name, img in zip(names, images)]

    save_file()

if __name__ == '__main__':
    file = 'D:\LNU\logo.png'
    form(file)
