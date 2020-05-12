
# J type; convert celsius to microvolts
def j_c_to_uv(c):
    
    c = c + 0.0    
    c0 = c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = 0.0

    # temperature range -210 to 760 oC
    if -210.0 < c < 760.0:
        
        c0 = 0.0
        c1 = 5.0381187815e1
        c2 = 3.0475836930e-2
        c3 = -8.5681065720e-5
        c4 = 1.3228195295e-7
        c5 = -1.7052958337e-10
        c6 = 2.0948090697e-13
        c7 = -1.2538395336e-16
        c8 = 1.5631725697e-20

    # temperature range 760 to 1200 oC
    elif 760.0 < c < 1200.0:
        
        c0 = 2.9645625681e5
        c1 = -1.4976127786e3
        c2 = 3.1787103924
        c3 = -3.1847686701e-3
        c4 = 1.5720819004e-6
        c5 = -3.0691369056e-10
        c6 = 0.0
        c7 = 0.0
        c8 = 0.0
    
    # 
    else:
        return 0.0
    E = c0 + c * (c1 + c * (c2 + c * (c3 + c * (c4 + c * (c5 + c * (c6 + c * (c7 + c * (c8))))))))
    return E

#J type; convert microvolt to celsius
def j_uv_to_c(uv):

    uv = uv + 0.0
    c0 = c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = 0.0
    
    # temperature range -210 to 0 oC
    if -8095.0 < uv < 0.0:
        c0 = 0.0;
        c1 = 1.9528268e-2
        c2 = -1.2286185e-6
        c3 = -1.0752178e-9
        c4 = -5.9086933e-13
        c5 = -1.7256713e-16
        c6 = -2.8131513e-20    
        c7 = -2.3963370e-24
        c8 = -8.3823321e-29

    # temperature range 0 to 760 oC
    elif 0.0 < uv < 42919.0:
        c0 = 0.0;
        c1 = 1.978425e-2
        c2 = -2.001204e-7
        c3 = 1.036969e-11
        c4 = -2.549687e-16
        c5 = 3.585153e-21
        c6 = -5.344285e-26
        c7 = 5.099890e-31
        c8 = 0.0;

    # temperature range 760 to 1200 oC
    elif 42919.0 < uv < 69553.0:
        c0 = -3.11358187e3
        c1 = 3.00543684e-1
        c2 = -9.94773230e-6
        c3 = 1.70276630e-10
        c4 = -1.43033468e-15
        c5 = 4.73886084e-21
        c6 = 0.0
        c7 = 0.0
        c8 = 0.0
    #
    else:
        return 0.0
    T = c0 + uv * (c1 + uv * (c2 + uv * (c3 + uv * (c4 + uv * (c5 + uv * (c6 + uv * (c7 + uv * (c8))))))))
    return T


 


