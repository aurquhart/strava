# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 09:08:31 2015

@author: aurquhart
"""

import os
import gpxpy
#import matplotlib.pyplot as plt

#reset working directory
os.chdir('C:/Users/angus/Documents/Python Scripts')

#import 1st strava file
gpx_file = open('stravadata/20150314-145601-Ride.gpx', 'r')
#type(gpx_file) #file

#
gpx = gpxpy.parse(gpx_file)
#type (gpx) #instance

#explore data

#print(gpx)
#GPX(tracks=[GPXTrack(name='Afternoon Ride', number=0, segments=[GPXTrackSegment(points=[...])])])

#for things in gpx.tracks:
#    print(things)
#so in tracks you have basically the top level info - name of ride
    
for ting in track.segments:
    print ting
#Nothing seems to be at this level
    

for thing in segment.points:
    print(thing)
