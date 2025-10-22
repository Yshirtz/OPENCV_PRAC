import cv2 as cv
import numpy as np

img = cv.imread('Ch.03\RGB.jpg')

if img is None:
    raise FileNotFoundError("이미지 파일을 찾을 수 없어요")

cv.imshow('Image Display',img)
cv.imshow('B',img[:,:,0])
cv.imshow('G',img[:,:,1])
cv.imshow('R',img[:,:,2])

cv.waitKey()
cv.destroyAllWindows()