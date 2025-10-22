import cv2 as cv

# 이미지 불러오기
img = cv.imread('Ch.03/dog.jpg')  # 이미지 경로에 맞게 수정하세요

# 새 크기 지정 (예: 원본보다 2배 확대)
new_size = (img.shape[1]*2, img.shape[0]*2)

# 서로 다른 보간 방법으로 리사이즈
res_nearest = cv.resize(img, new_size, interpolation=cv.INTER_NEAREST)
res_linear = cv.resize(img, new_size, interpolation=cv.INTER_LINEAR)
res_cubic = cv.resize(img, new_size, interpolation=cv.INTER_CUBIC)

# 결과 출력
cv.imshow('Original', img)
cv.imshow('INTER_NEAREST', res_nearest)
cv.imshow('INTER_LINEAR', res_linear)
cv.imshow('INTER_CUBIC', res_cubic)

cv.waitKey(0)
cv.destroyAllWindows()
