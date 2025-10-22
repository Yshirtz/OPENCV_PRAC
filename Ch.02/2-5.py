import cv2 as cv
import sys

drawing = False
start_point = (-1,-1)
end_point = (-1,-1)

def draw_rectangle(event, x, y, flags, param):
    global drawing, start_point, end_point, img, temp_img

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x,y)
        end_point = (x,y)
        temp_img = img.copy()

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            end_point = (x,y)
            temp_img = img.copy()
            cv.rectangle(temp_img,start_point,end_point,color=(255,0,0),thickness= 2)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x,y)
        cv.rectangle(img,start_point,end_point,color=(255,0,0),thickness= 2)
        temp_img = img.copy()


img = cv.imread('Ch.02\girl.jpg')

if img is None:
    sys.exit('파일이 없어요')

temp_img = img.copy()

cv.namedWindow('Draw Rectangle')
cv.setMouseCallback('Draw Rectangle', draw_rectangle)

while True:
    cv.imshow('Draw Rectangle',temp_img)
    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break

cv.destroyAllWindows()
