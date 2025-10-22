import cv2 as cv

# 이미지 불러오기 (흑백)
img = cv.imread('Ch.03/dog.jpg', cv.IMREAD_GRAYSCALE)

# 히스토그램 평활화
equalized = cv.equalizeHist(img)

# 결과 디스플레이
cv.imshow('Original Image', img)
cv.imshow('Histogram Equalized Image', equalized)

# 아무 키나 누르면 종료
cv.waitKey(0)
cv.destroyAllWindows()
