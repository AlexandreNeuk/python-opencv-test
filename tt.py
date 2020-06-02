
import cv2

vcap = cv2.VideoCapture("rtsp://admin:1234567a@192.168.1.76:554")

while(1):

    ret, frame = vcap.read()
    cv2.imshow('VIDEO', frame)
    cv2.waitKey(1)