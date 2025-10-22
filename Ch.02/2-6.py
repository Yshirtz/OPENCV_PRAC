import cv2 as cv
import sys

def draw(event, x, y, flags, param):
    global drawing_left, drawing_right, img

    if event == cv.EVENT_LBUTTONDOWN:
        drawing_left = True

    elif event == cv.EVENT_MOUSEMOVE and drawing_left:
        cv.circle(img, (x,y), 5, (255,0,0), -1)
            
    elif event == cv.EVENT_LBUTTONUP:
        drawing_left = False
    
    if event == cv.EVENT_RBUTTONDOWN:
        drawing_right = True

    elif event == cv.EVENT_MOUSEMOVE and drawing_right:
        cv.circle(img, (x,y), 5, (0, 0, 255), -1)
            
    elif event == cv.EVENT_RBUTTONUP:
        drawing_right = False
        

img = cv.imread('Ch.02\soccer.jpg')
if img is None:
    sys.exit('파일이 없어요')

cv.namedWindow('Draw Circles')
cv.setMouseCallback('Draw Circles', draw)

while True:
    cv.imshow('Draw Circles',img)
    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break

cv.destroyAllWindows()