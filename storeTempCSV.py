#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, csv, time

from sense_hat import SenseHat

sense = SenseHat()

# read sensor data
hum_temp ="{:.3f}".format(sense.get_temperature())
#sense.show_message("H:%s" % hum_temp)

pres_temp = "{:.3f}".format(sense.get_temperature_from_pressure())
#sense.show_message("P:%s" % pres_temp)

# save temp values into csv file
 
filePath =os.path.dirname(os.path.abspath(__file__))+ "/tempValues.csv"
print filePath

try:	
	f = open(filePath, "a")
	writer = csv.writer(f)

	# Check if file is empty and needs headline
	if os.path.getsize(filePath) == 0:
		print "File was empty, create header:"
		headLine = ["Time","Temp from Hum-Sensor", "Temp from Preas-Sensor"]
		print headLine
		writer.writerow(headLine)
	rowValues = [time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),hum_temp, pres_temp]
	print rowValues
	writer.writerow(rowValues);
	f.close() 
except:
  	print "Write error"

