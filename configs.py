'''****************************************************************************
* File Name: configs.py                                                       *
* Purpose:   Global variables and configurations for RPI Smart Home.          *
* Date:      11/24/2019                                                       *
* Copyright © 2019 Darren Cicala and Tyler Skene. All rights reserved.        *
****************************************************************************'''

# document version
__version__ = "0.2.0"

# there should be no imports in this file!

# global switches
SW_USE_METRIC_UNITS = False

# error codes
SYSERROR_NO_ERROR                    = 0
SYSERROR_TEMP_OUTDOOR_SENSOR_FAILURE = 1
SYSERROR_TEMP_INDOOR_SENSOR_FAILRUE  = 2
SYSERROR_WL_MOISTURE_SENSOR_FAILURE  = 3
SYSERROR_WL_API_CALL_FAILURE         = 4
SYSERROR_GUI_GENERAL_FAILURE         = 5

# API information
s_ApiBase            = "https://api.darksky.net/forecast/"     # root API 
s_ApiKey             = "" # modify this with your own darksky key
s_GPSLocation_LatLon = "" # modify this with your own GPS coordinates, e.g. "37.5148,15.7891"
s_FullAPI = s_ApiBase + s_ApiKey +  "/" + s_GPSLocation_LatLon # full API path

# temperature sensor information
i_IndoorSensorPin  = 17   # modify this with your own sensor signal pin for the outside
i_OutdoorSensorPin = 16   # modify this with your own sensor signal pin for indoors

i_DoNothingFlag    = 0
i_HeatFlag         = 1
i_CoolFlag         = 2

# moisture sensor information
# note: to enable SPI for you:
# 1. run sudo raspi-config
# 2. go to interfacing options
# 3. go to SPI, press enter to enable
# check to see if /dev/spidev0.0 exists 
i_SPIDevice = 0
i_SPIPort   = 0

################################## end file ###################################
