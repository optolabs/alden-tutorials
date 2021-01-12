# wlanalytics.py
# Property of Opto Labs
#   Author: Alden Kane

import time
import speedtest

########################################
# Time Config
########################################

time_tuple = time.localtime()                       # Unpack time.localtime() into tuple
month = time_tuple[1]                               # Month (e.g. 12)
day = time_tuple[2]                                 # Day (e.g. 30)
hour = time_tuple[3]                                # Hour (e.g. 5)
minute = time_tuple[4]                              # Minute (e.g. 30)
second = time_tuple[5]                              # Second (e.g. 57)
year = time_tuple[0]                                # Year (e.g. 2020)

########################################
# WLAN Speed Test
########################################

threads = None
speed = speedtest.Speedtest()
download_speed = speed.download(threads=threads)    # Returns bit/s
upload_speed = speed.upload(threads=threads)        # Returns bit/s

########################################
# Format and Print Data
########################################

scale_factor = 1000000
print("Download Speed: " + str(download_speed/scale_factor) + " Mbit/s")
print("Upload Speed: " + str(upload_speed/scale_factor) + " Mbit/s")
