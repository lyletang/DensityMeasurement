import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)

def main():
	ser.write('w')
	
	time.sleep(1)
	while True:
			a = ser.read();
			print a
if __name__ == '__main__':
	main()
