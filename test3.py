import serial
import time

ser = serial.Serial('/dev/ttyACM2', 9600, timeout = 1)

def main():
	
	while True:
		ser.write('w')
		a = ser.readall()
		print a
if __name__ == '__main__':
	main()
