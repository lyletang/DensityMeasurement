import usb.core
import usb.util
import sys
 
dev =  usb.core.find(idVendor= 0x5345, idProduct= 0x1234)
 
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]
ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
    usb.util.endpoint_direction(e.bEndpointAddress) == \
    usb.util.ENDPOINT_OUT
)
dev.reset()
