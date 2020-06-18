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


T_TYPE_MIN_C = -270.0
T_TYPE_MAX_C = 400.0

T_TYPE_MIN_UV = -5603.0
T_TYPE_MAX_UV = 20872.0


E_TYPE_MIN_C = -200.0 #no polynomials for range: -270 to -200
E_TYPE_MAX_C = 1000.0

E_TYPE_MIN_UV = -8825.0
E_TYPE_MAX_UV = 76373.0


B_TYPE_MIN_C = 250.0 #uv->C polys start at 0 oC but not C->uv
B_TYPE_MAX_C = 1820.0

B_TYPE_MIN_UV = 291.0
B_TYPE_MAX_UV = 13820.0


R_TYPE_MIN_C = -50.0
R_TYPE_MAX_C = 1768.1

R_TYPE_MIN_UV = -226.0
R_TYPE_MAX_UV = 21103.0


S_TYPE_MIN_C = -50.0
S_TYPE_MAX_C = 1768.1

S_TYPE_MIN_UV = -235.0
S_TYPE_MAX_UV = 18693.0


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
        et = exp(t) * a0
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


def T_TYPE_TRANSLATE_C_TO_UV(c):

    c = c + 0.0

    if c < T_TYPE_MIN_C or c > T_TYPE_MAX_C:
        return 0.0

    c0 = c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = c11 = c12 = c13 = c14 = 0.0

    if -270.0 < c < 0.0:

        c0 = 0.0
        c1 = 3.8748106364e1
        c2 = 4.4194434347e-2
        c3 = 1.1844323105e-4
        c4 = 2.0032973554e-5
        c5 = 9.0138019559e-7
        c6 = 2.2651156593e-8
        c7 = 3.6071154205e-10
        c8 = 3.8493939883e-12
        c9 = 2.8213521925e-14
        c10 = 1.4251594779e-16
        c11 = 4.8768662286e-19
        c12 = 1.0795539270e-21
        c13 = 1.3945027062e-24
        c14 = 7.9795153927e-28
    
    elif 0.0 < c < 400.0:

        c0 = 0.0
        c1 = 3.8748106364e1
        c2 = 3.3292227880e-2
        c3 = 2.0618243404e-4
        c4 = -2.1882256846e-6
        c5 = 1.0996880928e-8
        c6 = -3.0815758772e-11
        c7 = 4.5479135290e-14
        c8 = -2.7512901673e-17
        c9 = 0.0
        c10 = 0.0
        c11 = 0.0
        c12 = 0.0
        c13 = 0.0
        c14 = 0.0

    else:
        return 0.0

    E = c0 + c * (c1 + c * (c2 + c * (c3 + c * (c4 + c * (c5 + c * (c6 + c * (c7 + c * (c8 + c * (c9 + c * (c10 + c * (c11 + c * (c12 + c * (c13 + c * (c14))))))))))))))
    return E




def T_TYPE_TRANSLATE_UV_TO_C(uv):

    uv = uv + 0.0

    if uv < T_TYPE_MIN_UV or uv > T_TYPE_MAX_UV:
        return 0.0

    c1 = c2 = c3 = c4 = c5 = c6 = c7 = 0.0

    if -5603.0 < uv < 0.0:

        c0 = 0.0
        c1 = 2.5949192e-2
        c2 = -2.1316967e-7
        c3 = 7.9018692e-10
        c4 = 4.2527777e-13
        c5 = 1.3304473e-16
        c6 = 2.20241446e-20
        c7 = 1.2668171e-24

    elif 0.0 < uv < 20872.0:

        c0 = 0.0
        c1 = 2.592800e-2
        c2 = -7.602961e-7
        c3 = 4.637791e-11
        c4 = -2.165394e-15
        c5 = 6.048144e-20
        c6 = -7.293422e-25
        c7 = 0.0

    else:
        return 0.0

    T = c0 + uv * (c1 + uv * (c2 + uv * (c3 + uv * (c4 + uv * (c5 + uv * (c6 + uv * (c7)))))))
    return T



def E_TYPE_TRANSLATE_C_TO_UV(c):

    c = c + 0.0

    if c < E_TYPE_MIN_C or c > E_TYPE_MAX_C:
        return 0.0

    c0 = c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = c11 = c12 = c13 = 0.0

    if -270.0 < c < 0.0:

        c0 = 0.0
        c1 = 5.8665508708e1
        c2 = 4.5410977124e-2
        c3 = -7.7998048686e-4
        c4 = -2.5800160843e-5
        c5 = -5.9452583057e-7
        c6 = -9.3214058667e-9
        c7 = -1.0287605534e-10
        c8 = -8.0370123621e-13
        c9 = -4.3979497391e-15
        c10 = -1.6414776355e-17
        c11 = -3.9673619516e-20
        c12 = -5.5827328721e-23
        c13 = -3.4657842013e-26

    elif 0.0 < c < 1000.0:

        c0 = 0.0
        c1 = 5.8665508710e1
        c2 = 4.5032275582e-2
        c3 = 2.8908407212e-5
        c4 = -3.3056896652e-7
        c5 = 6.5024403270e-10
        c6 = -1.9197495504e-13
        c7 = -1.2536600497e-15
        c8 = 2.1489217569e-18
        c9 = -1.4388041782e-21
        c10 = 3.5960899481e-25
        c11 = 0.0
        c12 = 0.0
        c13 = 0.0

    else:
        return 0.0

    E = c0 + c * (c1 + c * (c2 + c * (c3 + c * (c4 + c * (c5 + c * (c6 + c * (c7 + c * (c8 + c * (c9 + c * (c10 + c * (c11 + c * (c12 + c * (c13)))))))))))))
    return E


def E_TYPE_TRANSLATE_UV_TO_C(uv):

    uv = uv + 0.0

    if uv < E_TYPE_MIN_UV or uv > E_TYPE_MAX_UV:
        return 0.0

    c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = 0.0

    if -8825.0 < uv < 0.0:

        c0 = 0.0
        c1 = 1.6977288e-2
        c2 = -4.3514970e-7
        c3 = -1.5859697e-10
        c4 = -9.2502871e-14
        c5 = -2.6084314e-17
        c6 = -4.1360199e-21
        c7 = -3.4034030e-25
        c8 = -1.1564890e-29
        c9 = 0.0

    elif 0.0 < uv < 76373.0:

        c0 = 0.0
        c1 = 1.7057035e-2
        c2 = -2.3301759e-7
        c3 = 6.5435585e-12
        c4 = -7.3562749e-17
        c5 = -1.7896001e-21
        c6 = 8.4036165e-26
        c7 = -1.3735879e-30
        c8 = 1.0629823e-35
        c9 = -3.2447087e-41

    else:
        return 0.0

    T = c0 + uv * (c1 + uv * (c2 + uv * (c3 + uv * (c4 + uv * (c5 + uv * (c6 + uv * (c7 + uv * (c8 + uv * (c9)))))))))
    return T


def B_TYPE_TRANSLATE_C_TO_UV(c):

    c = c + 0.0

    if c < B_TYPE_MIN_C or c > B_TYPE_MAX_C:
        return 0.0

    c0 = c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = 0.0
    
    if 0.0 < c < 630.15:

        c0 = 0.0
        c1 = -2.4650818346e-1
        c2 = 5.9040421171e-3
        c3 = -1.3257931636e-6
        c4 = 1.5668291901e-9
        c5 = -1.6944529240e-12
        c6 = 6.2290347094e-16
        c7 = 0.0
        c8 = 0.0

    elif 630.15 < c < 1820.0:

        c0 = -3.8938168621e3
        c1 = 2.8571747470e1
        c2 = -8.4885104785e-2
        c3 = 1.5785280164e-4
        c4 = -1.6835344864e-7
        c5 = 1.1109794013e-10
        c6 = -4.4515431033e-14
        c7 = 9.8975640821e-18
        c8 = -9.3791330289e-22

    else:
        return 0.0

    E = c0 + c * (c1 + c * (c2 + c * (c2 + c * (c3 + c * (c4 + c * (c5 + c * (c6 + c * (c7 + c * (c8)))))))))
    return E


def B_TYPE_TRANSLATE_UV_TO_C(uv):

    uv = uv + 0.0

    if uv < B_TYPE_MIN_UV or uv > B_TYPE_MAX_UV:
        return 0.0

    c0 = c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = 0.0

    if 291.0 < uv < 2431.0:

        c0 = 9.8423321e1
        c1 = 6.9971500e-1
        c2 = -8.4765304e-4
        c3 = 1.0052644e-6
        c4 = -8.3345952e-10
        c5 = 4.5508542e-13
        c6 = -1.5523037e-16
        c7 = 2.9886750e-20
        c8 = -2.4742860e-24

    elif 2431.0 < uv < 13820.0:

        c0 = 2.1315071e2
        c1 = 2.8510504e-1
        c2 = -5.2742887e-5
        c3 = 9.9160804e-9
        c4 = -1.2965303e-12
        c5 = 1.1195870e-16
        c6 = -6.0625199e-21
        c7 = 1.8661696e-25
        c8 = -2.4878585e-30

    else:
        return 0;

    T = c0 + uv * (c1 + uv * (c2 + uv * (c3 + uv * (c4 + uv * (c5 + uv * (c6 + uv * (c7 + uv * (c8))))))))
    return T


def R_TYPE_TRANSLATE_C_TO_UV(c):

    c = c + 0.0
    
    if c < T_TYPE_MIN_C or c > T_TYPE_MAX_C:
        return 0.0

    c0 = c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = 0.0

    if -50.0 < c < 1064.18:

        c0 = 0.0
        c1 = 5.28961729765
        c2 = 1.39166589782e-2
        c3 = -2.38855693017e-5
        c4 = 3.56916001063e-8
        c5 = -4.62347666298e-11
        c6 = 5.00777441034e-14
        c7 = -3.73105886191e-17
        c8 = 1.57716482367e-20
        c9 = -2.81038625251e-24

    elif 1064.18 < c < 1664.5:

        c0 = 2.95157925316e3 # assuming "* 103" was a typo
        c1 = -2.52061251332
        c2 = 1.59564501865e-2
        c3 = -7.64085947576e-6
        c4 = 2.05305291024e-9
        c5 = -2.93359668173e-13
        c6 = 0.0
        c7 = 0.0
        c8 = 0.0
        c9 = 0.0

    elif 1664.5 < c < 1768.1:
        
        c0 = 1.52232118209e5
        c1 = -2.68819888545e2
        c2 = 1.71280280471e-1
        c3 = -3.45895706453e-5
        c4 = -9.34633971046e-12
        c5 = 0.0
        c6 = 0.0
        c7 = 0.0
        c8 = 0.0
        c9 = 0.0

    else:
        return 0.0

    E = c0 + c * (c1 + c * (c2 + c * (c3 + c * (c4 + c * (c5 + c * (c6 + c * (c7 + c * (c8 + c * (c9)))))))))
    return E


def R_TYPE_TRANSLATE_UV_TO_C(uv):

    uv = uv + 0.0

    if uv < T_TYPE_MIN_UV or uv > T_TYPE_MAX_UV:
        return 0.0

    c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = 0.0

    if -226.0 < uv < 1923.0:

        c0 = 0.0
        c1 = 1.8891380e-1
        c2 = -9.3835290e-5
        c3 = 1.3068619e-7
        c4 = -2.2703580e-10
        c5 = 3.5145659e-13
        c6 = -3.8953900e-16
        c7 = 2.8239471e-19
        c8 = -1.2607281e-22
        c9 = 3.1353611e-26
        c10 = -3.3187769e-30

    elif 1923.0 < uv < 13228.0:

        c0 = 1.334584505e1
        c1 = 1.472644573e-1
        c2 = -1.844024844e-5
        c3 = 4.031129726e-9
        c4 = -6.249428360e-13
        c5 = 6.468412046e-17
        c6 = -4.458750426e-21
        c7 = 1.994710146e-25
        c8 = -5.313401790e-30
        c9 = 6.481976217e-35
        c10 = 0.0

    elif 11361.0 < uv < 19739.0:

        c0 = -8.199599416e1
        c1 = 1.553962042e-1
        c2 = -8.342197663e-6
        c3 = 4.279433549e-10
        c4 = -1.191577910e-14
        c5 = 1.492290091e-19
        c6 = 0.0
        c7 = 0.0
        c8 = 0.0
        c9 = 0.0
        c10 = 0.0

    elif 19739.0 < uv < 21103.0:

        c0 = 3.406177836e4
        c1 = -7.023729171
        c2 = 5.582903813e-4
        c3 = -1.952394635e-8
        c4 = 2.560740231e-13
        c5 = 0.0
        c6 = 0.0
        c7 = 0.0
        c8 = 0.0
        c9 = 0.0
        c10 = 0.0

    else:
        return 0.0

    T = c0 + uv * (c1 + uv * (c2 + uv * (c3 + uv * (c4 + uv * (c5 + uv * (c6 + uv * (c7 + uv * (c8 + uv * (c9 + uv * (c10))))))))))
    return T


def S_TYPE_TRANSLATE_C_TO_UV(c):

    c = c + 0.0

    if c < S_TYPE_MIN_C or c > S_TYPE_MAX_C:
        return 0.0

    c0 = c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = 0.0

    if -50.0 < c < 1064.18:

        c0 = 0.0
        c1 = 5.40313308631
        c2 = 1.25934289740e-2
        c3 = -2.32477968689e-5
        c4 = 3.22028823036e-8
        c5 = -3.31465196389e-11
        c6 = 2.55744251786e-14
        c7 = -1.25068871393e-17
        c8 = 2.71443176145e-21

    elif 1064.18 < c < 1664.5:

        c0 = 1.32900445085e3
        c1 = 3.34509311344
        c2 = 6.45805192818e-3
        c3 = -1.64856259209e-6
        c4 = 1.29989605174e-11
        c5 = 0.0
        c6 = 0.0
        c7 = 0.0
        c8 = 0.0

    elif 1664.5 < c < 1768.1:

        c0 = 1.46628232636e5
        c1 = -2.58430516752e2
        c2 = 1.63693574641e-1
        c3 = -3.30439046987e-5
        c4 = -9.43223690612e-12
        c5 = 0.0
        c6 = 0.0
        c7 = 0.0
        c8 = 0.0

    else:
        return 0.0

    E = c0 + c * (c1 + c * (c2 + c * (c2 + c * (c3 + c * (c4 + c * (c5 + c * (c6 + c * (c7 + c * (c8)))))))))
    return E



def S_TYPE_TRANSLATE_UV_TO_C(uv):

    uv = uv + 0.0

    if uv < S_TYPE_MIN_UV or uv > S_TYPE_MAX_UV:
        return 0.0

    c0 = c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = 0.0

    if -235.0 < uv < 1874.0:

        c0 = 0.0
        c1 = 1.84949460e-1
        c2 = -8.00504062e-5
        c3 = 1.02237430e-7
        c4 = -1.52248592e-10
        c5 = 1.88821343e-13
        c6 = -1.59085941e-16
        c7 = 8.23027890e-20
        c8 = -2.34181944e-23
        c9 = 2.79786260e-27

    elif 1874.0 < uv < 11950.0:

        c0 = 1.291507177e1
        c1 = 1.466298863e-1
        c2 = -1.534713402e-5
        c3 = 3.145945973e-9
        c4 = -4.163257839e-13
        c5 = 3.187963771e-17
        c6 = -1.291637500e-21
        c7 = 2.183475087e-26
        c8 = -1.447379511e-31
        c9 = 8.211272125e-36

    elif 10332.0 < uv < 17536.0:

        c0 = -8.087801117e1
        c1 = 1.621573104e-1
        c2 = -8.536869453e-6
        c3 = 4.719686453e-10
        c4 = -1.441693666e-14
        c5 = 2.081618890e-19
        c6 = 0.0
        c7 = 0.0
        c8 = 0.0
        c9 = 0.0

    elif 17536.0 < uv < 18693.0:

        c0 = 5.333875126e4
        c1 = -1.235892298e1
        c2 = 1.092657613e-3
        c3 = -4.265693686e-8
        c4 = 6.247205420e-13
        c5 = 0.0
        c6 = 0.0
        c7 = 0.0
        c8 = 0.0
        c9 = 0.0

    else:
        return 0.0

    T = c0 + uv * (c1 + uv * (c2 + uv * (c3 + uv * (c4 + uv * (c5 + uv * (c6 + uv * (c7 + uv * (c8 + uv * (c9)))))))))
    return T

