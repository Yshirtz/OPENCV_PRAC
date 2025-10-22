import cv2 as cv
import numpy as np

canvas = np.ones((200,600),dtype=np.uint8)*255

cv.putText(canvas,'Signature', (30,130),cv.FONT_HERSHEY_SCRIPT_SIMPLEX,4,(0,),8,cv.LINE_AA)

_, binary = cv.threshold(canvas,127,255,cv.THRESH_BINARY_INV)

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(7,7))

erosion = cv.erode(binary,kernel,iterations=1)
dilation = cv.dilate(binary,kernel,iterations=1)
opening = cv.morphologyEx(binary,cv.MORPH_OPEN,kernel)
closing = cv.morphologyEx(binary,cv.MORPH_CLOSE,kernel)

cv.imshow('Original',binary)
cv.imshow('erosion',erosion)
cv.imshow('dilation',dilation)
cv.imshow('opening',opening)
cv.imshow('closing',closing)



cv.waitKey()
cv.destroyAllWindows()