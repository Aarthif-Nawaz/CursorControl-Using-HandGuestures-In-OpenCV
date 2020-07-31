import cv2
import numpy as np

import mouse
palm = cv2.CascadeClassifier('palm.xml')

fist = cv2.CascadeClassifier('fist.xml')


cap = cv2.VideoCapture(0)
mouse.FAILSAFE = False
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    palm_cascade = palm.detectMultiScale(gray,1.3,5)
    hand = 0
    for (x, y, w, h) in palm_cascade:
        cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
        print(x,w,y,h)
        # define range of skin color in HSV
        lower_skin = np.array([0, 20, 70], dtype=np.uint8)
        upper_skin = np.array([20, 255, 255], dtype=np.uint8)

        # extract skin colur imagw

        mouse.move(x+w, y+h,absolute=True)
        #mouse.move(x, y)



    # cv2.namedWindow("img",cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty("img",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow('img', img)
    cv2.imshow('hand', hand)
    k = cv2.waitKey(30) & 0xff

    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

