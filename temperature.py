'''****************************************************************************
* File Name: temperature.py                                                   *
* Purpose:   Methods and functions pertaining to the temperature module.      *
* Date:      11/17/2019                                                       *
* Copyright © 2019 Darren Cicala and Tyler Skene. All rights reserved.        *
****************************************************************************'''

# document version
__version__ = "0.2.0"

# imports
import configs      # global configs file
import Adafruit_DHT # library to interface with DHT11 sensor

class TemperatureSensor:
	
	'''*****************************************************************
	* Name: __init__                                                                  
	* Description: Constructor for class TemperatureSensor                      
	* Parameters:  int i_InputGPIOPin                                              
	*                    GPIO pin on the Pi that the sensor is wired to.                      
	* Returns:     N/A                     
	*****************************************************************'''
	def __init__(i_InputGPIOPin):
		self.i_SensorType = Adafruit_DHT.DHT11 # type of sensor
		self.i_GPIOPin    = i_InputGPIOPin     # what pin the sensor is connected to
		self.i_ErrorFlag  = configs.SYSERROR_NO_ERROR # shocker! we don't have any errors because we just initialized it
	
	'''*****************************************************************
	* Name: read                                                                  
	* Description: Function to read from the sensor, and update class members.                      
	* Parameters:  N/A                     
	* Returns:     N/A (modifies class members)                 
	*****************************************************************'''	
	def read():
		# update "previous" values
		self.f_HumidityPrev_Pct  = self.f_Humidity_Pct
		self.f_TemperaturePrev_C = self.f_Temperature_C
		self.f_TemperaturePrev_F = self.f_Temperature_F
		
		# get new values 
		self.f_Humidity_Pct, self.f_Temperature_C = Adafruit_DHT.read_retry(sensor_name, sensor_pin)
		self.f_Temperature_F = ((9/5) * self.f_Temperature_C) + 32
		
	'''*****************************************************************
	* Name: MakeHVACDecision                                                                  
	* Description: Makes a decision to cool or warm the house based on
	*              the external temperature of the system. This function
	*              should only be called for the external temperature sensor.                      
	* Parameters:  N/A                     
	* Returns:     ??                 
	*****************************************************************'''
    def MakeHVACDecision():
	    # case 1: external temp less than 65 degrees 
	    if(
    def ChangeSystemState():		
################################## end file ###################################
