import sys

# compress movement for thermometers
#
# assume centigrade input
#

def tcompress ( t ):
    if t < -55:
        t = ((t+55)/5 - 55)
    if t > 120:
        t = (t/5 + 96)
    return t

while 1:
    n = input('enter num ');
    t  = tcompress(n)
    print " compressed ", n, " is ",t





