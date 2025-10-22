import cv2 as cv
import numpy as np

img =np.zeros((300,300,3), dtype=np.uint8)

start_point= (100,100)
end_point = (200,200)

cv.rectangle(img, start_point, end_point,  (255,255,255),-1)

tx,ty =50,30
translation_matrix = np.float32([[1,0,tx], [0,1,ty]])
translated =cv.warpAffine(img, translation_matrix,(300,300))

center = (150,150)
angle =45
scale =1.0
rotation_matrix= cv.getRotationMatrix2D(center,angle,scale)
rotated = cv.warpAffine(translated,rotation_matrix,(300,300))

cv.imshow('Original',img)
cv.imshow('translated',translated)
cv.imshow('rotated',rotated)

cv.waitKey()
cv.destroyAllWindows()
