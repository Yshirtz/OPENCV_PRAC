import cv2 as cv
import numpy as np

img = cv.imread('Ch.03/dog.jpg', cv.IMREAD_GRAYSCALE)

equalized = cv.equalizeHist(img)

cv.imshow('Original Image',img)
cv.imshow('Histogram Equalized Image', equalized)

cv.waitKey()
cv.destroyAllWindows()