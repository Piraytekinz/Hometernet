import cv2 as cv
from PIL import Image

img = Image.open('Hometernet-new-icon.png')

new = img.resize((150, 150))

saved = new.save('Hometernet-new-icon-1.png')

img = cv.imread('Hometernet-new-icon.png')

imga = cv.imread('Hometernet-new-icon-1.png')

cv.imshow('img', img)
cv.imshow('imga', imga)
cv.waitKey(0)