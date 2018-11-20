##breathing backlight adjuster
##reinkn
##11 20 2018
##at economy class

import os
import time
a = 0

def upwd():
    for a in xrange(0,33,1):##Also adjust here
        b = a * 0.03##Speed adjustment
        print b
        c = str(b)
        os.system('./kbrightness '+c)#Adjust backlight brightnessThank to @pirate @tcr
##os.system('./dbrightness '+c)#Used to adjust screen brightness
def dnwd():      
    for a in xrange(0,33,1):
        b = (33-a) * 0.03
        print b
        c = str(b)
        os.system('./kbrightness '+c)
##os.system('./dbrightness '+c)
while True:
    upwd()##Lightup
    dnwd()##Lightdown
