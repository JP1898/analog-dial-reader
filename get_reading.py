#! /usr/bin/python

from reader import *
import os

# directory is the directroy where all the files are 

directory = '/home/jj/Desktop/google-drive/RPi_dial_reader/gauges'
for filename in os.listdir(directory):   
    if filename.endswith(".jpg"): 
        (filebase, fileext) = filename.split('.')    
        read(filebase)
print('Done') 
