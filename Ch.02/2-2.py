import cv2 as cv
import sys
img = cv.imread('Ch.02\soccer.jpg')

if img is None:
    sys.exit('파일이 없어요')

Gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Image Display',img)
cv.imshow('Gray Image Display',Gray_img)

cv.waitKey()
cv.destroyAllWindows()
