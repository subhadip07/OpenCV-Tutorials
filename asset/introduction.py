import cv2

img = cv2.imread('asset/sale.png', 0)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite('new_image.png', img)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
