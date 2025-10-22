import cv2 as cv
import numpy as np

img = cv.imread('Ch.03/dog.jpg', cv.IMREAD_GRAYSCALE)

blurred = cv.GaussianBlur(img,(5,5),0)

cv.imshow('Original Image',img)
cv.imshow('Histogram blurred Image', blurred)

cv.waitKey()
cv.destroyAllWindows()
