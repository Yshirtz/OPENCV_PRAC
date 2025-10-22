import cv2 as cv
import sys
img = cv.imread('Ch.02\soccer.jpg', cv.IMREAD_GRAYSCALE)

if img is None:
    sys.exit('파일이 없어요')

cv.imshow('Image Display',img)

cv.imwrite('Ch.02\soccer02.jpg',img)

cv.waitKey()
cv.destroyWindow()
