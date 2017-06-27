#coding: utf-8

def getWeight():
	while True:	
		serialArduino.write('w')

		weight = serialArduino.readline()
		
		if float(weight) > 10:		
			return float(weight)
		else:
			continue
