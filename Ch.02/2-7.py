import cv2 as cv

cap =cv.VideoCapture(0)

if not cap.isOpened():
    print("웹 캠을 열 수 없습니다.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("프레임을 가져올 수 없습니다. 종료합니다.")
        break
    
    cv.imshow('Live Video', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()