'''****************************************************************************
* File Name: configs.py                                                       *
* Purpose: Global variables and configurations for RPI Smart Home.            *
* Date: 11/17/2019                                                            *
* Authors: Darren Cicala and Tyler Skene                                      *
****************************************************************************'''

__version__ = "1.0.0"

s_ApiBase            = "https://api.darksky.net/forecast/"
s_ApiKey             = "" # modify this with your own darksky key
s_GPSLocation_LatLon = "" # modify this with your own GPS coordinates, e.g. "37.5148,15.7891"

s_FullAPI = s_ApiBase + s_ApiKey +  "/" + s_GPSLocation

