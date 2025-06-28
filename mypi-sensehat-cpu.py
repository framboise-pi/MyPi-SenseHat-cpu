#!/usr/bin/env python3
############################################ mypi-sensehat-cpu.py
#
#	Copyright(C) LAFONTAINE Cedric Camille 2025
#	contact@codelibre.fr
#	https://github.com/framboise-pi/MyPi-SenseHat-cpu/blob/master/mypi-sensehat-cpu.py
#
#           _        _ _ _             ___
#  ___ ___ _| |___   | |_| |_ ___ ___  |  _|___
# |  _| . | . | -_|  | | | . |  _| -_|_|  _|  _|
# |___|___|___|___|  |_|_|___|_| |___|_|_| |_|
#
# ASCII art generator: http://patorjk.com/software/taag/
#
########################################################################
# USAGE EXAMPLE:
# python3 mypi-sensehat-cpu.py
########################################################################
from sense_hat import SenseHat
import psutil
import time

sense = SenseHat()
sense.rotation = 0
sense.low_light = True
sense.clear()
tour = 0
DELAY_SEC = 2
print("...starting SenseHat cpu script...")

def PixelCpu(cpu_load):
	global tour
	if tour > 7:
		tour = 0
		sense.clear()
	percent = int(cpu_load)
	thresholds = [
		(0, 12, 7, 100),
		(12, 25, 6, 120),
		(25, 37, 5, 140),
		(37, 40, 4, 160),
		(40, 52, 3, 180),
		(52, 65, 2, 200),
		(65, 77, 1, 220),
		(77, 100, 0, 255)
	]
	y = None
	for lower, upper, y_value, red_value in thresholds:
		if lower < percent <= upper:
			if red_value is not None and int(y_value):
				red = (red_value,0,0)
				sense.set_pixel(tour,y_value,red)
				tour += 1
				# DEBUG print ("cpu_load:",percent,"tour:",tour,"pixel y:",y_value)
	
while True:
	cpu_load = psutil.cpu_percent()
	if float(cpu_load):
		PixelCpu(cpu_load)
		time.sleep(DELAY_SEC)
