import cv2 as cv
import numpy as np

# 1. 이미지 불러오기
img = cv.imread('Ch.03/RGB.jpg')  # 이미지 경로 지정
if img is None:
    raise FileNotFoundError("이미지 파일을 찾을 수 없습니다.")

# 2. 이미지 출력 (OpenCV는 BGR 그대로 출력)
cv.imshow('Original Image', img)
cv.imshow('Blue Channel', img[:, :, 0])
cv.imshow('Green Channel', img[:, :, 1])
cv.imshow('Red Channel', img[:, :, 2])

# 6. 키 입력 대기 후 창 닫기
cv.waitKey(0)
cv.destroyAllWindows()
