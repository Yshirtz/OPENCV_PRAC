import cv2 as cv          # OpenCV 라이브러리를 cv라는 이름으로 가져옴
import sys                # 시스템 종료 등의 기능을 위한 sys 모듈 가져옴

# 이미지 파일 읽기 (상대 경로 기준)
img = cv.imread('Ch.02/soccer.jpg')  

# 이미지가 없는 경우 오류 메시지 출력 후 종료
if img is None:
    sys.exit('File Not Found')  # 이미지 파일을 찾을 수 없으면 프로그램 종료

# 기존 이미지를 축소
Small_image = cv.resize(img, dsize=(0,0), fx=0.5, fy=0.5)

# 이미지 화면에 출력
cv.imshow('Small Image Display', Small_image)  # 'Image Display'라는 이름의 창에 이미지 보여주기

# 키 입력 대기
cv.waitKey()  # 키보드 입력이 있을 때까지 대기

# 열려 있는 모든 OpenCV 창 닫기
cv.destroyWindow()  # 창 닫기 
