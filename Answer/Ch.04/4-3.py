import cv2 as cv
import numpy as np

# 이미지 읽기
image = cv.imread('Ch.04/soccer.jpg')  # 컬러 이미지
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

cv.imshow("aaa", image)

# Canny 엣지 검출
edges = cv.Canny(gray, 100, 200)

# 윤곽선 찾기
contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# 윤곽선 길이가 50 이상인 것만 원본 이미지에 그리기
for contour in contours:
    length = cv.arcLength(contour, closed=True)
    if length >= 50:
        cv.drawContours(image, [contour], -1, (0, 255, 0), 1)  # 초록색, 두께 1

# 결과 이미지 출력
cv.imshow("Contours over Original", image)
cv.waitKey(0)
cv.destroyAllWindows()
