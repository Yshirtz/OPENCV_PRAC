import cv2 as cv
import sys
img = cv.imread('Ch.02\girl.jpg')

if img is None:
    sys.exit('파일이 없어요')

cv.rectangle(img,(330,470),(530,640),color=(255,0,0),thickness= 3)

cv.putText(img,'Hello OpenCV', org=(330,450),fontFace=cv.FONT_HERSHEY_COMPLEX,fontScale=1,color=(0,255,0),thickness=2)

Small_img = cv.resize(img, dsize=(0,0), fx=0.8, fy= 0.8)


cv.imshow('Image Display',Small_img)


cv.waitKey()
cv.destroyAllWindows()
