# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 09:08:31 2015

@author: aurquhart
"""

import os
import gpxpy
import csv

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
            time.append(pointthings.time)
            
#In points we have longitude, lattitude, elevation,  time
            
print(time[0])

with open('C:/Users/angus/Documents/GitHub/strava.time.csv', "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in time:
        writer.writerow([val])
            

    
