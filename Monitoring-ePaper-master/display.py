#!/usr/bin/env python
# coding: utf-8
#Author: Jiahui Tang
#Date: 2017-06-20

#import the necessary packages
import datetime
from ePaper import *

#the main class
class Display(object):
	def __init__(self):
		pass

	def __str__(self):
		return "4.3inch-ePaper display"

	__repr__ = __str__

	@classmethod
	def time_(cls, screen):
		clock_x = 40
		clock_y = 20
		temp_x = 0
		temp_y = 0
		time_now = datetime.datetime.now()
		time_string = time_now.strftime('%H:%M')
		date_string = time_now.strftime('%Y-%m-%d')
		week_string = [u'星期一',u'星期二',u'星期三',u'星期四',u'星期五',u'星期六',u'星期日'][time_now.isoweekday() - 1]
		if time_string[0] == '0':
			time_string = time_string[1:]
			temp_x += 40

		for c in time_string:
			bmp_name = 'NUM{}.BMP'.format('S' if c == ':' else c)
			screen.bitmap(clock_x + temp_x, clock_y, bmp_name)
			temp_x += 70 if c == ':' else 100

		screen.set_ch_font_size(FONT_SIZE_48)
		screen.set_en_font_size(FONT_SIZE_48)
		
		#test print
		print date_string
		print week_string
		
		screen.text(clock_x + 350 + 140, clock_y + 10, date_string)
		screen.text(clock_x + 350 + 170, clock_y + 70, week_string)

	@classmethod
	def logo_(cls, screen):
		bmp_name = 'CCUT.BMP'
		screen.bitmap(80, 0 + 240, bmp_name)

		bmp_name = 'PI.BMP'
		screen.bitmap(80, 0 + 240 + 160, bmp_name)

	@classmethod
	def node_name_(cls,screen):
		screen.set_ch_font_size(FONT_SIZE_48)
		screen.set_en_font_size(FONT_SIZE_48)
		
		screen.text(300, 0 + 300, u'Result are as follows :')

		screen.text(350, 0 + 400, u'Weight :')
		screen.text(350, 0 + 400 + 80, u'Volume :')
		screen.text(350, 0 + 400 + 160, u'Density :')


	@classmethod
	def info_(cls, screen, weight, volume, density):
		screen.set_ch_font_size(FONT_SIZE_64)
		screen.set_en_font_size(FONT_SIZE_64)

		screen.text(450, 0 + 400, u'{weight}'.format(weight = weight))
		screen.text(450, 0 + 400 + 80, u'{volume}'.format(volume = density))
		screen.text(450, 0 + 400 + 160, u'{density}'.format(density = density))