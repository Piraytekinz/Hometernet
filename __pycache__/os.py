from PIL import Image
import cv2 as cv
import os

path = '__pycache__/Empty.jpg'

image = Image.open(path)


if image.size[0] > 1200 and image.size[1] > 600:


    resize = image.resize((1200,600))

pathnum = path.rfind("/")
print(pathnum)
path = path[pathnum+1: ]
print(path)

saved = resize.save(str(path))


img = cv.imread(path)

cv.imshow('resize', img)


cv.waitKey(0)

os.remove(path)

