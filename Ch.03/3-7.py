import cv2 as cv
import numpy as np

img = cv.imread('Ch.03/girl.jpg', cv.IMREAD_GRAYSCALE)

kernel = np.array([[-2,-1,0],
                   [-1,1,1],
                   [0,1,2]],dtype=np.float32)

embossed = cv.filter2D(img,-1,kernel)

cv.imshow('Original Image',img)
cv.imshow('embossed Image', embossed)

cv.waitKey()
cv.destroyAllWindows()

