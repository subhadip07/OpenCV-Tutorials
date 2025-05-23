import cv2
import random

img = cv2.imread('asset/sale.png', -1)

# print(img)

# print(img.shape)

# print(img[0])

# Change first 100 rows to random pixels
for i in range(100):
	for j in range(img.shape[1]):
		img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255]

# Copy part of image
tag = img[500:700, 600:900]
img[100:300, 650:950] = tag

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
