import cv2 as cv
import numpy as np

# 이미지 불러오기 (그레이스케일)
img = cv.imread('Ch.04/soccer.jpg', cv.IMREAD_GRAYSCALE)

# Sobel 연산자 적용 (64F로 계산 후 절댓값, uint8 변환)
sobel_x = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
sobel_y = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)

# 엣지 강도 계산: sqrt(sobel_x^2 + sobel_y^2)
magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

# 정수형으로 변환
abs_sobel_x = cv.convertScaleAbs(sobel_x)
abs_sobel_y = cv.convertScaleAbs(sobel_y)
edge_strength = cv.convertScaleAbs(magnitude)

# 출력
cv.imshow('Original', img)
cv.imshow('Sobel X', abs_sobel_x)
cv.imshow('Sobel Y', abs_sobel_y)
cv.imshow('Edge Strength (Magnitude)', edge_strength)

cv.waitKey(0)
cv.destroyAllWindows()
