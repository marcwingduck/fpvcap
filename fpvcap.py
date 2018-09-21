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
import argparse

parser = argparse.ArgumentParser(description='Basic video capture application.')
parser.add_argument('-i', '--index', help='Capture device index.', nargs='?', const=1, type=int, default=0)
args = parser.parse_args()

# change index to device
cap = cv2.VideoCapture(args.index)

if not cap.isOpened():
    exit(0)

# get camera props
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# create video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = None

record = False

# start acquisition
while True:
    ret, frame = cap.read()
    if ret:
        # disable stream to get full fps
        writer.write(frame) if record else cv2.imshow("fpv", frame)

    c = cv2.waitKey(1) & 0xFF
    if c == ord('q'):  # quit application
        break
    elif c == ord('r'):  # toggle recording
        record = not record
        if record:
            if writer:
                writer.release()  # release former instance
            writer = cv2.VideoWriter('fpv{}.avi'.format(time.strftime("%Y%m%d%H%M%S")), fourcc, fps, (w, h))

cap.release()
if writer:
    writer.release()
cv2.destroyAllWindows()
