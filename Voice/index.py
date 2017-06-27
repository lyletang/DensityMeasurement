#coding: utf-8

import time
import os

def say(siganl):
	voiceName = {'HELLO': 'hello.wav',\
		     '1': 'set1.wav',\
		     '2': 'set2.wav',\
		     '3': 'set3.wav',\
		     '4': 'set4.wav',\
		     'y': 'py.wav',\
		     'n': 'pn.wav',\
		     'x': 'start.wav',\
		     'q': 'end.wav'\
		     } 

	try:
		cmd = 'sudo aplay ' + '/home/pi/object/voice/' + voiceName[siganl]
		
		os.system(cmd)
		
	except Exception:
		pass
