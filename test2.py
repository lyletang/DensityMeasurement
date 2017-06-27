import serial
import time

ser = serial.Serial('/dev/ttyACM2', 9600)

def main():
	
	while True:
		ser.write('a')
		while True:
			a = ser.read()
			if a != '':
				print a
			else:
				break
if __name__ == '__main__':
	main()
