#!/usr/bin/env bash

# wlanalytics.sh
# Measures critical wlan paramaters and outputs them to a .json file for data interchange
# Uses hostname, ifconfig, iwconfig, ping
# Property of Opto Labs
#   Author: Alden Kane


##################################################
# MEASUREMENT SECTION
##################################################

# Get Hostname
HOSTN=$(hostname)

# Get IP address for wlan0 network using ifconfig
IPADDR=$(ifconfig | grep -A1 wlan0 | grep -o -P '.{0,0}inet.{0,14}'| grep -o -P '.{0,0}1.{0,13}')

# Write Stdout and Stderr of ifwconfig to file
iwconfig > ../tmp/script_data/iw.out 2>&1

# Get WLAN network name (SSID). Standard Length of SSID is 32 characters per spec
SSID=$(grep -o -P '.{0,0}ESSID.{0,50}' ../tmp/script_data/iw.out | grep -o -P '.{0,0}".{0,35}' | tr -d '"')

# Get BITRATE
BITRATE=$(grep -o -P '.{0,0}Rate=.{0,12}' ../tmp/script_data/iw.out | grep -o -P '.{0,0}=.{0,13}' | tr -d '=')

# Get FREQUENCY of channel
FREQUENCY=$(grep -o -P '.{0,0}Frequency:.{0,11}' ../tmp/script_data/iw.out | grep -o -P '.{0,0}:.{0,11}' | tr -d ':')

# Get TX Power of Router
TXPOWER=$(grep -o -P '.{0,0}Power=.{0,10}' ../tmp/script_data/iw.out | grep -o -P '.{0,0}=.{0,10}' | tr -d '=')

# Get RX Power on Module
RXPOWER=$(grep -o -P '.{0,0}level=.{0,10}' ../tmp/script_data/iw.out | grep -o -P '.{0,0}=.{0,10}' | tr -d '=')

# Get Link Qualitycat
LINKQUALITY=$(grep -o -P '.{0,0}Quality=.{0,7}' ../tmp/script_data/iw.out | grep -o -P '.{0,0}=.{0,5}' | tr -d '=')

##################################################
# OUTPUT SECTION
##################################################

echo WLAN Network: $SSID
echo Device Hostname: $HOSTN
echo WLAN IP Address: $IPADDR
echo WLAN Channel Freq.: $FREQUENCY
echo Router Tx Power: $TXPOWER
echo Device Rx Power: $RXPOWER
echo Bitrate: $BITRATE
echo Link Quality: $LINKQUALITY

