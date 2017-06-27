#coding: utf-8

#import the necessary packages
import os
import sys
import time
import datetime
import serial
import math
import RPi.GPIO as GPIO

#import the own packages
from Calculate import *
from ProgressBar import *
from RpiePaper import *
from RpiPrinter import *
from Voice import *

serialKeys = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1)
serialArduino = serial.Serial('/dev/ttyACM0', 9600, timeout = 1)

materialList = {1: True,\
		2: False,\
		3: False,\
		4: False\
    	  	}
printer = False
start = False

#define the serial signal
MATERIAL1 = '1'
MATERIAL2 = '2'
MATERIAL3 = '3'
MATERIAL4 = '4'
PRINTER_YES = 'y'
PRINTER_NO = 'n'
START = 'x'
END = 'q'

def keysFromArduino():
	try:
		printerOld = False

		while True:
			receive = serialArduino1.read()
			
			if receive in [MATERIAL1, MATERIAL2, MATERIAL3, MATERIAL4]:
				for index, key in enumerate(materialList):
					materialList[key] = True if key == ((lambda x: x + 1)(materialList.index(receive))) else False

			elif receive in (PRINTER_YES, PRINTER_NO):
				printer = True if receive == 'y' else False

			elif receive == START:
				START = True
			
			else:
				pass
	except KeyboardInterrupt, KeysError:
		pass


def main():
	say('HELLO');

	materialOld = 1
	printerOld = False

	#init the progress bar
	bar = ProgressBar()
	
	#init the printer
	p = Printer()
	

	threadKeys = threading.Thread(target = keyFromArduino, args = ())
	
	threads = []

	threads.append(threadKeys)

	for thread in threads:
		thread.setDaemon(True)
		thread.start()

	try：

		while True:
				bar.update(0)				

				material = (filter((lambda x, x == True), materialList)).pop()
				if material != materialOld:
					say(str(material))

				if printer != printOld:
					if printer:
						say(PRINTER_YES)
					else:
						say(PRINTER_NO)
					
					printerOld = not printerOld

				if start:
					#Start measuring
					say(START)

					bar.update(1)
				
					elasticityModulus = getElasticityModulus(material)
					bar.update(2)
					time.sleep(1)
					bar.update(3)

					throughTime = getThroughTime()
					
					bar.update(4)

					density = getDensity(elasticityModulus, throughTime)

					bar.update(5)

					weight = getWeight()
					
					bar.update(6)

					volume = getVolume(weight, density)
					
					bar.update(7)

					showResult(weight, volume, density)
			
					bar.update(8)
					time.sleep(1)
					bar.update(9)
					
					if printer:
						printResult(weight, volume, density)
		
					bar.update(10)

					say(END)
					

if __name__ == '__main__':
	main()
