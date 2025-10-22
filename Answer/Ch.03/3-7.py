import cv2 as cv
import numpy as np

# 이미지 불러오기 (그레이스케일)
img = cv.imread('Ch.03/girl.jpg', cv.IMREAD_GRAYSCALE)

# 엠보싱 커널 정의
kernel = np.array([[-2, -1, 0],
                   [-1,  1, 1],
                   [ 0,  1, 2]], dtype=np.float32)

# 필터 적용 (엠보싱)
embossed = cv.filter2D(img, -1, kernel)

# 원래 이미지와 엠보싱 이미지 디스플레이
cv.imshow('Original', img)
cv.imshow('Embossed', embossed)

cv.waitKey(0)
cv.destroyAllWindows()
