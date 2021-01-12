#!/usr/bin/env python3

# lines-by-canny.py
# Property of Opto Labs
# Copyleft license for personal use
#   Author: Alden Kane

import cv2 as cv2

# Conditional Initialization
video_feed = False
image_feed = True

if video_feed:
    cam = cv2.VideoCapture("./test.mp4")

while True:
    if video_feed:
        # Read in frame from video feed
        retval, frame = cam.read()

    if image_feed:
        # Read frame from image file
        frame = cv2.imread("./image.jpg")

    # Run canny method
    edges = cv2.Canny(frame, 180, 200)

    # Standard OpenCV Formatting
    cv2.namedWindow("Camera Feed", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Camera Feed", 400, 225)

    cv2.namedWindow("Canny of Feed", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Canny of Feed", 400, 225)

    cv2.moveWindow("Camera Feed", 0, 0)
    cv2.moveWindow("Canny of Feed", 420, 0)

    cv2.imshow("Camera Feed", frame)
    cv2.imshow("Canny of Feed", edges)

    # cv2 Syntax for Processing
    action = cv2.waitKey(1)
    if action == 27:
        break

cv2.destroyAllWindows()

