'''****************************************************************************
* File Name: water_lawn.py                                                    *
* Purpose:   Methods and functions pertaining to the water lawn module.       *
* Date:      11/17/2019                                                       *
* Copyright © 2019 Darren Cicala and Tyler Skene. All rights reserved.        *
* Powered by the DarkSky API.                                                 *
****************************************************************************'''

# document version
__version__ = "0.1.0"

# imports 
import configs   # global configs file for the system
import urllib    # library to handle HTTPGet requests
import json      # library to handle JSON parsing

class Forecast:
  
  # do an initial API call when we create the object 
  def __init__(self):
    # get the API string from the configs file
    self.s_APILink = configs.s_FullAPI   
    # make an API request 
    s_Contents = urllib.request.urlopen(self.s_APILink).read().decode("utf-8") 
    # dump the return string into a dictionary
    self.d_ForecastInformation = json.loads(s_Contents)
    
  

################################## end file ###################################