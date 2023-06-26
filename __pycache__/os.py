import cv2 as cv
from PIL import Image

img = Image.open('Hometernet-icon.png')

new = img.resize((120, 120))

saved = img.save('Hometernet-icon1.png')

image = cv.imread('Hometernet-icon1.png')

cv.imshow('img', image)
cv.waitKey(0)