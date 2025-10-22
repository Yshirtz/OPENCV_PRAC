import cv2 as cv
import numpy as np

img = cv.imread('Ch.04/soccer.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('aaa',img)

edges = cv.Canny(gray,100,200)

contours, _ = cv.findContours(edges,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

for contour in contours:
    length = cv.arcLength(contour, closed=True)
    if length >= 50:
        cv.drawContours(img, [contour], -1, (0, 255, 0), 1)

cv.imshow('contour',img)

cv.waitKey()
cv.destroyAllWindows()
