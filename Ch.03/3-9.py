import cv2 as cv

img = cv.imread('Ch.03/dog.jpg', cv.IMREAD_GRAYSCALE)

new_size = (img.shape[1]*2, img.shape[0]*2)

res_nearest = cv.resize(img, new_size, interpolation=cv.INTER_NEAREST)
res_linear = cv.resize(img, new_size, interpolation=cv.INTER_LINEAR)
res_cubic = cv.resize(img, new_size, interpolation=cv.INTER_CUBIC)


cv.imshow('Original Image',img)
cv.imshow('INTER_NEAREST',res_nearest)
cv.imshow('INTER_LINEAR',res_linear)
cv.imshow('INTER_CUBIC',res_cubic)

cv.waitKey()
cv.destroyAllWindows()
