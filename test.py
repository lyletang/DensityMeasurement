import serial
import time

ser = serial.Serial('/dev/ttyACM2', 9600, timeout = 1)

def main():
	
	time.sleep(1)
	while True:
		ser.write('w')
		while True:
			weight = ser.readline()
		
			if weight == '':
				continue			
			else:
				break
		print weight

if __name__ == '__main__':
	main()
