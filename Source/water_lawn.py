#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''****************************************************************************
* File Name: water_lawn.py                                                    *
* Purpose:   Methods and functions pertaining to the water lawn module.       *
* Date:      11/26/2019                                                       *
* Copyright © 2019 Darren Cicala and Tyler Skene. All rights reserved.        *
* Powered by the DarkSky API.                                                 *
****************************************************************************'''

# document version
__version__ = "0.3.0"

# imports 
import configs                # global configs file for the system
import urllib                 # library to handle HTTPGet requests
import json                   # library to handle JSON parsing
from Adafruit_GPIO import SPI # library for SPI communication
import Adafruit_MCP3008       # library for decoding the output of the ADC


class Forecast:
  
  # do an initial API call when we create the object 
  def __init__(self):
    # get the API string from the configs file
    self.s_APILink = configs.s_FullAPI   
    # make an API request 
    s_Contents = urllib.urlopen(self.s_APILink).read().decode("utf-8") 
    # dump the return string into a dictionary
    self.d_ForecastInformation = json.loads(s_Contents)
    
  def update(self):
    # make an API request 
    s_Contents = urllib.urlopen(self.s_APILink).read().decode("utf-8") 
    # dump the return string into a dictionary
    self.d_ForecastInformation = json.loads(s_Contents)
    # capture the hourly forecasts for ease of access 
    self.l_HourlyForecasts = self.d_ForecastInformation["hourly"]["data"]
    
  def CheckForRain(self):
    
  
    
class WaterSensor:
  def __init__(self):
    self.o_AdcDevice = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(configs.i_SPIDevice, configs.i_SPIPort)
    self.o_SysTime   = systime.Systime()
    
  def read(self):
    i_DigitalValue = self.o_AdcDevice.read_adc_difference(configs.i_AdcChannel)
    self.f_WaterLevel_Pct = i_DigitalValue / configs.i_WaterSensorScalar

class WaterModule:
  def __init__(self, o_InputSysTime):
    self.o_WaterSensor = WaterSensor()
    self.o_Forecast = Forecast()
    
  def MakeWateringDecision():
    self.o_Forecast.update()
    
    
    
    


################################## end file ###################################
