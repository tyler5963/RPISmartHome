'''****************************************************************************
* File Name: configs.py                                                       *
* Purpose:   Global variables and configurations for RPI Smart Home.          *
* Date:      11/17/2019                                                       *
* Copyright © 2019 Darren Cicala and Tyler Skene. All rights reserved.        *
****************************************************************************'''

# document version
__version__ = "0.1.0"

# API information
s_ApiBase            = "https://api.darksky.net/forecast/"     # root API 
s_ApiKey             = "" # modify this with your own darksky key
s_GPSLocation_LatLon = "" # modify this with your own GPS coordinates, e.g. "37.5148,15.7891"
s_FullAPI = s_ApiBase + s_ApiKey +  "/" + s_GPSLocation_LatLon # full API path

################################## end file ###################################