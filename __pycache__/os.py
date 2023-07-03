import cv2 as cv
from PIL import Image

img = Image.open('__pycache__/blue-white-balls-shoot-out-open-door-into-large-bright-room.jpg')

new = img.resize((2000, 1200))

saved = new.save('congrats-pic.jpg')

img = cv.imread('__pycache__/blue-white-balls-shoot-out-open-door-into-large-bright-room.jpg')

imga = cv.imread('congrats-pic.jpg')

cv.imshow('img', img)
cv.imshow('imga', imga)
cv.waitKey(0)