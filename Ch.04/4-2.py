import cv2 as cv

img = cv.imread('Ch.04/soccer.jpg', cv.IMREAD_GRAYSCALE)

blurred = cv.GaussianBlur(img,(5,5),1.4)

edges = cv.Canny(blurred,100,200)

cv.imshow('Original',img)
cv.imshow('Canny',edges)

cv.waitKey()
cv.destroyAllWindows()
