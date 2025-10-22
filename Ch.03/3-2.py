import cv2 as cv

img = cv.imread('Ch.03\dog.jpg',cv.IMREAD_GRAYSCALE)

if img is None:
    print("파일이 없어요")
    exit()

ret,binary_img= cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

print("자동 계산된 임계값 : ",ret)    

cv.imshow('Original',img)
cv.imshow('OTSU Thresholding',binary_img)

cv.waitKey()
cv.destroyAllWindows()