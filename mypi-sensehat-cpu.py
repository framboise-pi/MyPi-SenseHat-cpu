#!/usr/bin/env python
#coding=utf-8
#
#*	MyPi-SenseHat-cpu
#*	https://github.com/framboise-pi/MyPi-SenseHat-cpu
#*	Copyright(C) 2020 Cedric Camille Lafontaine http://www.framboise-pi.fr,
#*	version 0.0.1
#

from sense_hat import SenseHat
import random
from random import randint
import psutil
import time

global tour

tour = 0
sense = SenseHat()
sense.rotation = 270
sense.low_light = True
sense.clear()

print("...starting SenseHat cpu script...")
#psutil.virtual_memory().percent

def PixelCpu(tour,cpu_load):
	red = [255,0,0]
	y = 0
	percent = int(cpu_load)
	if (percent <= 12):
		y = 7
		red[0] = 100
	if (percent > 12 and percent <= 25):
		y = 6
		red[0] = 120
	if (percent > 25 and percent <= 37):
		y = 5
		red[0] = 140
	if (percent > 37 and percent <= 40):
		y = 4
		red[0] = 160
	if (percent > 40 and percent <= 52):
		y = 3
		red[0] = 180
	if (percent > 52 and percent <= 65):
		y = 2
		red[0] = 200
	if (percent > 65 and percent <= 77):
		y = 1
		red[0] = 220
	if (percent > 77 and percent <= 100):
		y = 0
	#debug
	#print ("cpu_load:",percent,"tour:",tour,"pixel h:",y)
	sense.set_pixel(tour,y,red)

while True:
	cpu_load = psutil.cpu_percent()
	if (cpu_load is not None):
		if (tour >= 7):
			sense.clear()
			tour = 0
		else: tour = tour + 1
		PixelCpu(tour,cpu_load)
		time.sleep(1)
