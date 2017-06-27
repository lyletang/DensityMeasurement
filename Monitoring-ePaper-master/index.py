#!/usr/bin/env python
# coding: utf-8

'''
Equipment: RaspberryPi 3B, 4.3inch-ePaper(Waveshare)
Author: Jiahui Tang
Date: 2017-6-11
'''

#import the necessary packages
import time
import datetime
import json
import os
import sys
import time

#import the own packages
from ePaper import *
from display import *

#define the bmp name
ccut_bmp = 'CCUT.BMP'
raspberrypi_bmp = 'PI.BMP'

#connect to the 4.3inch-ePaper(UART)
screen_width = 800
screen_height = 600
screen = Screen('/dev/ttyAMA0') #if you use the USB-TTL, please replaced with '/dev/ttyACM0'
screen.connect()
screen.handshake()

#load font and pictures from the tf-card
#screen.load_font()
screen.load_pic()
#time.sleep(5)

#test the command
#screen.test()

#init the 4.3inch-ePaper
screen.clear()
screen.set_memory(MEM_FLASH)
screen.set_rotation(ROTATION_180)

#test display
'''
Display.time_(screen)
Display.logo_(screen)
Display.node_name_(screen)
Display.info_(screen, 'master')
Display.info_(screen, 'slave1')
Display.info_(screen, 'slave2')
Display.info_(screen, 'slave3')
Display.info_(screen, 'slave4')
'''

Display.time_(screen)
Display.logo_(screen)
Display.node_name_(screen)


def showResult(weight, volume, density):
	try:
		Display.time_(screen)
		Display.logo_(screen)
		Display.node_name_(screen)
		Display.info_(screen, weight, volume, density)

		screen.update()
		#screen.disconnect()

	except Exception:
		pass

if __name__ == '__main__':
	showResult(100, 200, 300)