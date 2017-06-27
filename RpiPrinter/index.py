#coding: utf-8
#Project: RaspberryPi drive thermal printer
#Python-escpos—api-doc-url: https://python-escpos.readthedocs.io/en/latest/api/escpos.html
#Author: Jiahui Tang
#Date: 2017-06-22

from escpos.printer import Usb
import time

class Print(object):
	def __init__(self):
		self.p = Usb(0x28e9, 0x0289, 0, out_ep=0x03)
	
	def __str__(self):
		return 
		
	__repr__ = __str__

	def cut(self):
		self.p.cut()
	
	def setText(self, size):
		self.p.set(align = u'center', font = u'a', smooth = True, width = size, height = size)

	def putImage(self, imagePath):
		self.p.image(str(imagePath))

	def putQr(self, qrInfo, qrSize = 10):
		self.p.qr(qrInfo, size = qrSize)

	def putBarcode(self, barcodeInfo):
		self.barcode(barcodeInfo, 'EAN13', 64, 2, '', '')

	def putText(self, text, textSize = 1):
		self.setText(textSize)
		self.p.text(text)

	def printResult(self, weight, volume, density):
		self.putText("******************************\n")
		self.putText(time.asctime())
		self.putText("\n")
		self.putText("\n")
		self.putText("Measured results are as follows:\n")
		self.putText("\n")
		self.putText("Weight: ")
		self.putText(str(weight))
		self.putText("\n")
		self.putText("Volume: ")
		self.putText(str(volume))
		self.putText("\n")
		self.putText("Density: ")
		self.putText(str(density))
		self.putText("\n")
		self.putText("\n")
		self.putText("Scan qr to check the result!\n")
		self.putQr("Weight: {weight}\nVolume: {volume}\nDensity: {density}".format(weight = weight, volume = volume, density = density))
		self.cut()

def main():
	p = Print()
	p.printResult(100, 200, 300)

if __name__ == '__main__':
	main()
