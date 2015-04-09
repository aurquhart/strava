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
gpx_file = open('stravadata/20130807-071108-Ride.gpx', 'r')

#
gpx = gpxpy.parse(gpx_file)

#This will start to flatten out the data

for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation)

#This way will create 2 lists of the longitudes and latitudes
lat = []
lon = []

for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            lat.append(point.latitude)
            lon.append(point.longitude)
            
print(lat)

#Finally plot the data in matplot

fig = plt.figure(facecolor = '0.05')
ax = plt.Axes(fig, [0., 0., 1., 1.], )
ax.set_aspect('equal')
ax.set_axis_off()
fig.add_axes(ax)
plt.plot(lon, lat, color = 'deepskyblue', lw = 0.2, alpha = 0.8)