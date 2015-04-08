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
