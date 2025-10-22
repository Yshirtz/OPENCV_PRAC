import cv2 as cv
import numpy as np

def adjust_gamma(image,gamma):
    image1= image/255.0
    return np.uint8(255*(image1**gamma))
    

img = cv.imread('Ch.03/dog.jpg')
img = cv.resize(img,(300,300))

gammas = [0.5,0.75,1,2,3]

for gamma in gammas:
    adjusted = adjust_gamma(img, gamma)
    window_name = f'Gmma {gamma}'
    cv.imshow(window_name,adjusted)

cv.waitKey()
cv.destroyAllWindows()