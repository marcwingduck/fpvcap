#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#######################################################
#
#    #, #,         CCCCCC  VV    VV MM      MM RRRRRRR
#   %  %(  #%%#   CC    CC VV    VV MMM    MMM RR    RR
#   %    %## #    CC        V    V  MM M  M MM RR    RR
#    ,%      %    CC        VV  VV  MM  MM  MM RRRRRR
#    (%      %,   CC    CC   VVVV   MM      MM RR   RR
#      #%    %*    CCCCCC     VV    MM      MM RR    RR
#     .%    %/
#        (%.      Computer Vision & Mixed Reality Group
#
#######################################################
__author__ = "Marc Lieser"
__copyright__ = "Copyright 2018, " \
                "Hochschule RheinMain" \
                "University of Applied Sciences"
__license__ = "WTFPL"
__version__ = "1.0"
#######################################################

import cv2
import time

# capture, use 1 if device has a webcam
cap = cv2.VideoCapture(0)

# grab a frame to get the capture device's image size
while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("fpv", frame)
        break
    cv2.waitKey(10)
h, w = frame.shape[:2]

# get fps prop (todo hard-code fps if this is not working with our setup)
fps = cap.get(cv2.CAP_PROP_FPS)
print h, w, fps

# create video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter('fpv.avi', fourcc, fps, (w, h))

record = False

# start acquisition
while True:
    ret, frame = cap.read()
    if ret:
        if record:  # disable ui to get full fps
            writer.write(frame)
        else:  # display frame
            cv2.imshow("fpv", frame)

    c = cv2.waitKey(1) & 0xFF
    if c == ord('q'):  # quit application
        break
    elif c == ord('r'):  # toggle recording
        record = not record
        if record:
            writer.release()  # release former instance
            writer = cv2.VideoWriter('fpv{}.avi'.format(time.strftime("%Y%m%d%H%M%S")), fourcc, fps, (w, h))

cap.release()
writer.release()
cv2.destroyAllWindows()
