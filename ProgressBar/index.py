#coding: utf-8

import time
import RPi.GPIO as GPIO
'''
setDic = {1: 12,\
	  2: 11,\
	  3: 13,\
	  4: 15,\
	  5: 16,\
	  6: 18,\
	  7: 22,\
	  8: 36,\
	  9: 38,\
	  10: 40\
	  }
'''

setDic = {1: 18,\
	  2: 17,\
	  3: 27,\
	  4: 22,\
	  5: 23,\
	  6: 24,\
	  7: 25,\
	  8: 16,\
	  9: 20,\
	  10: 21\
	  }


GPIO.setmode(GPIO.BCM)
for index, key in enumerate(setDic):
	GPIO.setup(setDic[key], GPIO.OUT)
	#GPIO.output(setDic[key], GPIO.LOW)

class ProgressBar(object):
	def __init__(self):
		print '55555'
		#define the Pin
		#self.bar1 = 12 
		#self.bar2 = 11
		#self.bar3 = 13
		#self.bar4 = 15
		#self.bar5 = 16
		#self.bar6 = 18
		#self.bar7 = 22
		#self.bar8 = 36
		#self.bar9 = 38
		#self.bar10 = 40

		self.bar1 = 18 
		self.bar2 = 17
		self.bar3 = 27
		self.bar4 = 22
		self.bar5 = 23
		self.bar6 = 24
		self.bar7 = 25
		self.bar8 = 16
		self.bar9 = 20
		self.bar10 = 21

		self.myDic = {0: None,\
			      1: self.bar1,\
			      2: self.bar2,\
			      3: self.bar3,\
			      4: self.bar4,\
			      5: self.bar5,\
			      6: self.bar6,\
			      7: self.bar7,\
		   	      8: self.bar8,\
			      9: self.bar9,\
			      10: self.bar10\
			      }

	def __str__(self):
		return 'Progress Bar'	

	__repr__ =  __str__

	#yield
	def getPinList(self, schedule):
		#for i in range(schedule):
		#	yield i + 1
		
		if schedule == 0:
			return [i + 1 for i in range(10)]
		else:
			return [i + 1  for i in range(schedule)]

	def update(self, schedule):
		try:
			print '3333'
			if schedule in self.myDic:
				if schedule == 0:
					for pin in self.getPinList(10):
						GPIO.output(setDic[pin], GPIO.LOW)
				
				else:
					for pin in self.getPinList(schedule):
						GPIO.output(setDic[pin], GPIO.HIGH)
			
			else:
				pass
	
		except KeyboardInterrupt, Exception:
			print Exception
			GPIO.cleanup()
		
		#GPIO.output(schedule, GPIO.HIGH)
	
def main():
	bar = ProgressBar()
	bar.update(5)

if __name__ == '__main__':
	main()
