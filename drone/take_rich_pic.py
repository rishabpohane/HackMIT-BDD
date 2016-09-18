import cv2
import urllib
import time

cap = cv2.VideoCapture(0)

x = 0
while(x<10):
    print "pic in... 2"
    time.sleep(1);
    print "pic in... 1"
    time.sleep(1);
    ret, frame = cap.read()
    cv2.imwrite("rich_pic_%d.png" % (x),frame)
    x = x+1;
