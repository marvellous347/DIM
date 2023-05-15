import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Read the image
pic = np.array(Image.open('ЦОЗ/Labs/Lab3/pict.png'))

# Display the original image
plt.title('Original')
plt.imshow(pic)
plt.show()

# Extract color channels
red_channel = pic[:, :, 0]
green_channel = pic[:, :, 1]
blue_channel = pic[:, :, 2]

# Display color channels separately
plt.title('Червоний канал')
plt.imshow(red_channel)
plt.show()

plt.title('Зелений канал')
plt.imshow(green_channel)
plt.show()

plt.title('Синій канал')
plt.imshow(blue_channel)
plt.show()

# Display single-channel grayscale image
gray = np.dot(pic[..., :3], [0.299, 0.587, 0.114])
plt.figure(figsize=(10, 10))
plt.title('Градація сірого')
plt.imshow(gray, cmap=plt.get_cmap('gray'))
plt.show()

# Apply contrast enhancement
lab = cv2.cvtColor(pic, cv2.COLOR_RGB2LAB)
l, a, b = cv2.split(lab)
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
l2 = clahe.apply(l)
lab2 = cv2.merge((l2, a, b))
img2 = cv2.cvtColor(lab2, cv2.COLOR_LAB2RGB)

# Display contrast-enhanced image
plt.title('Контрастне зображення')
plt.imshow(img2)
plt.show()
