# lines-by-canny.py
# Property of Opto Labs
# Copyleft license for personal use
#   Author: Alden Kane

import cv2 as cv2
import numpy as np
import math
from matplotlib import pyplot as plt

# VALUE Stash
# Hough Threshold = 150
# Canny MinVal = 180
# Canny MaxVal = 400


# Trackbar Function
def on_trackbar(val):
    # Read from Trackbars
    trackbar_1_pos = cv2.getTrackbarPos(trackbar_1_name, win1_name)
    hough_threshold = trackbar_1_pos

    trackbar_2_pos = cv2.getTrackbarPos(trackbar_2_name, win1_name)
    canny_minval = trackbar_2_pos

    trackbar_3_pos = cv2.getTrackbarPos(trackbar_3_name, win1_name)
    canny_maxval = trackbar_3_pos

    # Read frame from image file and format frame copy for outputting
    frame = cv2.imread("./test-1.jpg")
    bw_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    output = frame.copy()

    # Image Operations
    while True:
        # Absolute Thresholding
        im_bw = cv2.threshold(frame, 150, 255, cv2.THRESH_BINARY)[1]

        # Run canny method
        # Was 180, 400 w/ decent results
        edges = cv2.Canny(bw_frame, canny_minval, canny_maxval, None, 3)

        #  Standard Hough Line Transform
        # Was 150 for alpha with good results
        lines = cv2.HoughLines(edges, 1, np.pi / 180, hough_threshold, None, 0, 0)

        # Copy edges to image to draw lines to
        # output = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

        # Draw the lines
        if lines is not None:
            for i in range(0, len(lines)):
                rho = lines[i][0][0]
                theta = lines[i][0][1]
                a = math.cos(theta)
                b = math.sin(theta)
                x0 = a * rho
                y0 = b * rho
                pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
                pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
                cv2.line(output, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)

        # MATPLOTLIB for Sexiness
        # plt.subplot(221), plt.imshow(frame), plt.title('Frame')
        # plt.xticks([]), plt.yticks([])
        # plt.subplot(222), plt.imshow(edges), plt.title('Canny of Frame')
        # plt.xticks([]), plt.yticks([])
        # plt.subplot(223), plt.imshow(output), plt.title('Lines Detected')
        # plt.xticks([]), plt.yticks([])
        # # Fourth Window
        # # plt.subplot(224), plt.imshow(im_bw), plt.title('Absolute')
        # # plt.xticks([]), plt.yticks([])
        # plt.show()

        # OpenCV GUI Formatting
        cv2.namedWindow(win1_name, cv2.WINDOW_NORMAL)
        #cv2.resizeWindow(win1_name, 800, 450)
        cv2.moveWindow(win1_name, 0, 0)
        cv2.imshow(win1_name, output)

        # Debug Trackbar
        print('------------------------------------')
        print('Hough MaxVal: ' + str(trackbar_1_pos))
        print('Canny MinVal: ' + str(trackbar_2_pos))
        print('Canny MaxVal: ' + str(trackbar_3_pos))
        print('------------------------------------')

        return output


# Image Feed Init - Actually done in on_trackbar
img = cv2.imread("./test.jpg", cv2.IMREAD_GRAYSCALE)

# Trackbar Initialization
hough_threshold_min = 110
hough_threshold_max = 500
canny_minval_slider_max = 299
canny_maxval_slider_min = 300
canny_maxval_slider_max = 750

# Name Window
win1_name = 'Lines Detected'

# OpenCV GUI Formatting - MUST BE HERE so trackbar can initialize
cv2.namedWindow(win1_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(win1_name, 800, 450)
cv2.moveWindow(win1_name, 0, 0)

# Trackbar Formatting and Value Fetch
trackbar_1_name = 'Hough Transform Threshold x %d' % hough_threshold_max
trackbar_2_name = 'Canny Edge Detector Minval x %d' % canny_minval_slider_max
trackbar_3_name = 'Canny Edge Detector Maxval x %d' % canny_maxval_slider_max
cv2.createTrackbar(trackbar_1_name, win1_name, hough_threshold_min, hough_threshold_max, on_trackbar)
cv2.createTrackbar(trackbar_2_name, win1_name, 0, canny_minval_slider_max, on_trackbar)
cv2.createTrackbar(trackbar_3_name, win1_name, canny_maxval_slider_min, canny_maxval_slider_max, on_trackbar)

# Run on_trackbar function
autogrid = on_trackbar(val = 150)

# Wait until user press some key
cv2.waitKey()
