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
    for (x, y, w, h) in palm_cascade:
        cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
        mouse.move(x, y,absolute=True,duration=.2);
        #mouse.move(x, y)

    fist_cascade = fist.detectMultiScale(gray, 1.3, 5)
    for (xf, yf, wf, hf) in fist_cascade:
        cv2.rectangle(img, (xf, yf), ((xf + wf), (yf + hf)), (0, 0, 255), 2)
        mouse.move(xf, yf)

    # cv2.namedWindow("img",cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty("img",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff

    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
