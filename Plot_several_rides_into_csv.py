# -*- coding: utf-8 -*-
"""
Created on Thu Apr 09 07:45:48 2015

@author: angus
"""

from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import gpxpy
#import pandas as pd
import csv

data_path = 'C:/Users/angus/Documents/Python Scripts/stravadata'

data = [f for f in listdir(data_path) if isfile(join(data_path,f))]



lat = []
lon = []


for activity in data:
    gpx_filename = join(data_path,activity)
    gpx_file = open(gpx_filename, 'r')
    gpx = gpxpy.parse(gpx_file)

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                lat.append(point.latitude)
                lon.append(point.longitude)
    
    
    
with open('C:/Users/angus/Documents/GitHub/strava.test5.csv', "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in lat:
        writer.writerow([val])  
        
        
with open('C:/Users/angus/Documents/GitHub/strava.test6.csv', "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in lon:
        writer.writerow([val])          
        


