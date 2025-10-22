import cv2 as cv

# 이미지 불러오기
img = cv.imread('Ch.03/dog.jpg')  # 이미지 경로를 맞게 수정하세요

# 가우시안 블러 적용 (커널 크기 5x5, 시그마 0은 자동 계산)
blurred = cv.GaussianBlur(img, (5, 5), 0)

# 원본 이미지와 블러 이미지 출력
cv.imshow('Original Image', img)
cv.imshow('Gaussian Blurred Image', blurred)

cv.waitKey(0)
cv.destroyAllWindows()
