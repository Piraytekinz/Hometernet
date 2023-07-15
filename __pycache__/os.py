import cv2 as cv
from PIL import Image

img = Image.open('__pycache__\discover.jpg')

new = img.resize((1024, 500))

saved = new.save('__pycache__\discover-new.jpg')

img = cv.imread('__pycache__\discover.jpg')

imga = cv.imread('__pycache__\discover-new.jpg')

cv.imshow('img', img)
cv.imshow('imga', imga)
cv.waitKey(0)