#coding: utf-8
#test

from escpos.printer import Usb

""" Seiko Epson Corp. Receipt Printer (EPSON TM-T88III) """
p = Usb(0x28e9, 0x0289, 0, out_ep=0x03)
p.set(align=u'center', font=u'a', smooth=True, width=1, height=1)
p.text("\u90edHello World\n")
#p.image("victors.png")
#p.block_text('guo jian wei and tang jia hui', font='a')
p.qr('Victors', size=10)
p.barcode('1324354657687', 'EAN13', 64, 2, '', '')
p.cut()
