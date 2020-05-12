#!/usr/bin/python

from thermocouples import *
from numpy import arange

for i in arange(-300, 1500, 0.5):

    # prints "x, y" pairs where x is always the same and y is C - to_c(to_uv(C))
    
    # J TYPE
    #out = J_TYPE_TRANSLATE_UV_TO_C(J_TYPE_TRANSLATE_C_TO_UV(i))

    # K TYPE
    #out = K_TYPE_TRANSLATE_UV_TO_C(K_TYPE_TRANSLATE_C_TO_UV(i))

    # T TYPE
    #out = T_TYPE_TRANSLATE_UV_TO_C(T_TYPE_TRANSLATE_C_TO_UV(i))

    # N TYPE
    out = N_TYPE_TRANSLATE_UV_TO_C(N_TYPE_TRANSLATE_C_TO_UV(i))
    
    print ("%.1f, %.3f" % (i, (i - out)))
