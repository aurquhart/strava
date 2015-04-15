# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 09:08:31 2015

@author: aurquhart
"""

import os
import gpxpy
import csv
import pandas as pd

#import matplotlib.pyplot as plt

#reset working directory
os.chdir('C:/Users/angus/Documents/Python Scripts')

#import 1st strava file
gpx_file = open('stravadata/20150314-145601-Ride.gpx', 'r')
#type(gpx_file) #file

#get file ready for parsing
gpx = gpxpy.parse(gpx_file)
#type (gpx) #instance

#create some empty lists to put the data from the gpx file into

lon =[]
lat = []
time = []
elevation = []
        
for things in gpx.tracks:
    for lowerthings in things.segments:
        for pointthings in lowerthings.points:
            lon.append(pointthings.longitude)
            lat.append(pointthings.latitude)
            time.append(pointthings.time)
            elevation.append(pointthings.elevation)
 
d = {'lon':lon, 'lat':lat, 'time':time, 'elevation':elevation} 

df =   pd.DataFrame(data=d) 

df.to_csv('C:/Users/angus/Documents/GitHub/strava/firstride.csv')

       
#In points we have longitude, lattitude, elevation,  time
            


    
