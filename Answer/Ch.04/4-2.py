import cv2 as cv

# 이미지 불러오기 (그레이스케일)
img = cv.imread('Ch.04/soccer.jpg', cv.IMREAD_GRAYSCALE)

# 가우시안 블러 적용 (노이즈 제거)
blurred = cv.GaussianBlur(img, (5, 5), 1.4)

# 캐니 엣지 검출 (임계값1, 임계값2)
edges = cv.Canny(blurred, 100, 200)

# 결과 출력
cv.imshow('Original', img)
cv.imshow('Canny Edge', edges)

cv.waitKey(0)
cv.destroyAllWindows()
