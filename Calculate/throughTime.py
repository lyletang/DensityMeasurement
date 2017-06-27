import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
'''
GPIO.setup(4,GPIO.IN)
GPIO.setup(5,GPIO.OUT)    #inhibit
GPIO.setup(32,GPIO.OUT)   #MOS TRIG
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
'''

#BCM
GPIO.setup(4,GPIO.IN)
GPIO.setup(5,GPIO.OUT)    #inhibit
GPIO.setup(12,GPIO.OUT)   #MOS TRIG
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)


GPIO.output(26,GPIO.LOW)
GPIO.output(19,GPIO.LOW)
GPIO.output(13,GPIO.HIGH)
GPIO.output(6,GPIO.LOW) 

GPIO.output(12,GPIO.LOW)
GPIO.output(5,GPIO.HIGH)

def getThroughTime():
	while True:
		GPIO.output(5,GPIO.LOW)
		#t1 = time.time()
		GPIO.output(12,GPIO.HIGH)
		t1 = time.time()
		while GPIO.input(4):
			print "1111"
		#t2 = time.time()
		while True:
			t2 = time.time()
			while not GPIO.input(4):
				print "222222222"
				if GPIO.input(4):
					t3 = time.time()
					temp = t3 - t2
					GPIO.output(5,GPIO.HIGH)
					
					#return, shutdown the MOS
					GPIO.output(12, GPIO.LOW)
					#return temp
					return 1
			t4 = time.time()
			if (t4-t1) >= 3:
				GPIO.output(12,GPIO.LOW)
				GPIO.output(5,GPIO.HIGH)
				break
		time.sleep(1)

getThroughTime()
