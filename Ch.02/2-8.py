import cv2 as cv

cap =cv.VideoCapture(0)
if not cap.isOpened():
    print("웹 캠을 열 수 없습니다.")
    exit()

captured_img = []

while True:
    ret, frame = cap.read()
    if not ret:
        print("프레임을 가져올 수 없습니다. 종료합니다.")
        break
    
    cv.imshow('Live Cam', frame)

    key = cv.waitKey(1) & 0xFF

    if  key== ord('a'):
        captured_img.append(frame.copy())
        print(f"{len(captured_img)}번째 이미지 캡쳐됨")

    elif key== ord('q'):
        print(f"{len(captured_img)}장의 이미지 캡쳐됨")
        break

cap.release()
cv.destroyAllWindows()

for idx, img in enumerate(captured_img):
    cv.imshow(f'Captured Image {idx + 1}',img)
    cv.waitKey(0)

cv.destroyAllWindows()

