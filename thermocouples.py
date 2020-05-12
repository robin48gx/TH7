from math import exp

#
#
# based in its entirety on the NIST T-90 thermocouple polynomial tables
#
#

J_TYPE_MIN_C = -210.0
J_TYPE_MAX_C = 760.0

J_TYPE_MIN_UV = -8095.0
J_TYPE_MAX_UV = 69553.0


N_TYPE_MIN_C = -200.0 #no polys for -270 to -200
N_TYPE_MAX_C = 1300.0

N_TYPE_MIN_UV = 3990.0
N_TYPE_MAX_UV = 47513.0


K_TYPE_MIN_C = -270.0
K_TYPE_MAX_C = 1372.0

K_TYPE_MIN_UV = -5891.0
K_TYPE_MAX_UV = 54886.0

# converts supplied temperature,  C to uV based on J-type polynomials
def J_TYPE_TRANSLATE_C_TO_UV(c):

    c = c + 0.0 # possibly not needed...    

    if c < J_TYPE_MIN_C or c > J_TYPE_MAX_C:
        return 0.0


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


# uses J-type polynomials to convert supplied microvolt,  uv to celsius
def J_TYPE_TRANSLATE_UV_TO_C(uv):

    uv = uv + 0.0

    if uv < J_TYPE_MIN_UV or uv > J_TYPE_MAX_UV:
        return 0.0

    c0 = c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = 0.0
    
    # temperature range -200 to 0 oC
    if -3990.0 < uv < 0.0:
        c0 = 0.0;
        c1 = 3.8436847e-2
        c2 = 1.1010485e-6
        c3 = 5.2229312e-9
        c4 = 7.2060525e-12
        c5 = 5.8488586e-15
        c6 = 2.7754916e-18    
        c7 = 7.7075166e-22
        c8 = 1.1582665e-25
        c9 = 7.3138868e-30

    # temperature range 0 to 600 oC
    elif 0.0 < uv < 20613.0:
        c0 = 0.0;
        c1 = 3.86896e-2
        c2 = -1.08267e-6
        c3 = 4.70205e-11
        c4 = -2.12169e-18
        c5 = -1.17272e-19
        c6 = 5.39280e-24
        c7 = -7.98156e-29
        c8 = 0.0
        c9 = 0.0

    # temperature range 600 to 1300 oC
    elif 20613.0 < uv < 47513.0:
        c0 = 1.972485e1
        c1 = 3.300943e-2
        c2 = -3.915159e-7
        c3 = 9.855391e-12
        c4 = -1.274371e-16
        c5 = 7.767022e-22
        c6 = 0.0
        c7 = 0.0
        c8 = 0.0
        c9 = 0.0
    #
    else:
        return 0.0
    T = c0 + uv * (c1 + uv * (c2 + uv * (c3 + uv * (c4 + uv * (c5 + uv * (c6 + uv * (c7 + uv * (c8 + uv * (c9)))))))))
    return T



def N_TYPE_TRANSLATE_C_TO_UV(c):

    c = c + 0.0    

    if c < N_TYPE_MIN_C or c > N_TYPE_MAX_C:
        return 0.0

    c0 = c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = 0.0

    # temperature range -270 to 0 oC
    if -270.0 < c < 0.0:
        
        c0 = 0.0
        c1 = 2.6159105962e1
        c2 = 1.0957484228e-2
        c3 = -9.3841111554e-5
        c4 = -4.6412039759e-8
        c5 = -2.6303357716e-9
        c6 = -2.2653438003e-11
        c7 = -7.6089300791e-14
        c8 = -9.3419667835e-17
        c9 = 0.0
        c10 = 0.0

    # temperature range 0 to 1300 oC
    elif 0.0 < c < 1300.0:
        
        c0 = 0.0
        c1 = 2.5929394601e1
        c2 = 1.5710141880e-2
        c3 = 4.3825627237e-5
        c4 = -2.5261169794e-7
        c5 = 6.4311819399e-10
        c6 = -1.0063471519e-12
        c7 = 9.9745338992e-16
        c8 = -6.0863245607e-19
        c9 = 2.0849229339e-22
        c10 = -3.0682196151e-26
    
    # 
    else:
        return 0.0
    E = c0 + c * (c1 + c * (c2 + c * (c3 + c * (c4 + c * (c5 + c * (c6 + c * (c7 + c * (c8 + c * (c9 + c * (c10))))))))))
    return E


def N_TYPE_TRANSLATE_UV_TO_C(uv):

    uv = uv + 0.0
    
    if uv < N_TYPE_MIN_UV or uv > N_TYPE_MAX_UV:
        return 0.0
    
    c0 = c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = 0.0
    
    # temperature range -200 to 0 oC
    if -3990.0 < uv < 0.0:
        c0 = 0.0;
        c1 = 3.8436847e-2
        c2 = 1.1010485e-6
        c3 = 5.2229312e-9
        c4 = 7.2060525e-12
        c5 = 5.8488586e-15
        c6 = 2.7754916e-18    
        c7 = 7.7075166e-22
        c8 = 1.1582665e-25
        c9 = 7.3138868e-30

    # temperature range 0 to 600 oC
    elif 0.0 < uv < 20613.0:
        c0 = 0.0;
        c1 = 3.86896e-2
        c2 = -1.08267e-6
        c3 = 4.70205e-11
        c4 = -2.12169e-18
        c5 = -1.17272e-19
        c6 = 5.39280e-24
        c7 = -7.98156e-29
        c8 = 0.0
        c9 = 0.0

    # temperature range 600 to 1300 oC
    elif 20613.0 < uv < 47513.0:
        c0 = 1.972485e1
        c1 = 3.300943e-2
        c2 = -3.915159e-7
        c3 = 9.855391e-12
        c4 = -1.274371e-16
        c5 = 7.767022e-22
        c6 = 0.0
        c7 = 0.0
        c8 = 0.0
        c9 = 0.0
    #
    else:
        return 0.0
    T = c0 + uv * (c1 + uv * (c2 + uv * (c3 + uv * (c4 + uv * (c5 + uv * (c6 + uv * (c7 + uv * (c8 + uv * (c9)))))))))
    return T


# multiplied by 10?
def K_TYPE_TRANSLATE_C_TO_UV(c):

    c = c + 0.0

    if c < K_TYPE_MIN_C or c > K_TYPE_MAX_C:
        return 0.0

    c0 = c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = 0.0
    t = et = E = 0.0

    a0 = 1.185976e2
    a1 = -1.183432e-4

    if c < 0.0:
        c0 = 0.0
        c1 = 3.9450128025e1
        c2 = 2.3622373598e-2
        c3 = -3.2858906784e-4
        c4 = -4.9904828777e-6
        c5 = -6.7509059173e-8
        c6 = -5.7410327428e-10
        c7 = -3.1088872894e-12
        c8 = -1.0451609365e-14
        c9 = -1.9889266878e-17
        c10 = -1.6322697486e-20
        et = 0.0
    
    elif 0 < c < 1372.0:
        c0 = -1.7600413686e1
        c1 = 3.8921204975e1
        c2 = 1.8558770032e-2
        c3 = -9.9457592874e-5
        c4 = 3.1840945719e-7
        c5 = -5.6072844889e-10
        c6 = 5.6075059059e-13
        c7 = -3.2020720003e-16
        c8 = 9.7151147152e-20
        c9 = -1.2104721275e-23
        c10 = 0.0
        t = c
        t -= 126.9686
        t = t * t
        t = t * a1
        et = math.exp(t) * a0
    else:
        return 0.0
    t = c
    E = c0 + t * (c1 + t * (c2 + t * (c3 + t * (c4 + t * (c5 + t * (c6 + t * (c7 + t * (c8 + t * (c9 + t * (c10)))))))))) + et
    return E

def K_TYPE_TRANSLATE_UV_TO_C(uv):

    uv = uv + 0.0

    if uv < K_TYPE_MIN_UV or uv > K_TYPE_MAX_UV:
        return 0.0

    c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = 0.0
    
    if -5891.0 < uv < 0.0:

        c0 = 0.0
        c1 = 2.5173462e-2
        c2 = -1.1662878e-6
        c3 = -1.0833638e-9
        c4 = -8.9773540e-13
        c5 = -3.7342377e-16
        c6 = -8.6632643e-20
        c7 = -1.0450598e-23
        c8 = -5.1920577e-28
        c9 = 0.0

    elif 0.0 < uv < 20644.0:

        c0 = 0.0
        c1 = 2.508335e-2
        c2 = 7.860106e-8
        c3 = -2.503131e-10
        c4 = 8.315270e-14
        c5 = -1.228034e-17
        c6 = 9.804036e-22
        c7 = -4.413030e-26
        c8 = 1.057734e-30
        c9 = -1.052755e-35

    elif 20644.0 < uv < 54886.0:

        c0 = -1.318058e2
        c1 = 4.830222e-2
        c2 = -1.646031e-6
        c3 = 5.464731e-11
        c4 = -9.650715e-16
        c5 = 8.802193e-21
        c6 = -3.110810e-26
        c7 = 0.0
        c8 = 0.0
        c9 = 0.0

    else:
        return 0.0

    T = c0 + uv * (c1 + uv * (c2 + uv * (c3 + uv * (c4 + uv * (c5 + uv * (c6 + uv * (c7 + uv * (c8 + uv * (c9)))))))))
    return T


