import cv2 as cv
import sys
img = cv.imread('Ch.02\soccer.jpg')

if img is None:
    sys.exit('파일이 없어요')

Small_img = cv.resize(img, dsize=(0,0), fx=0.3, fy= 0.3)

cv.imshow('Image Display',img)
cv.imshow('Desized Image Display',Small_img)

cv.waitKey()
cv.destroyAllWindows()
