
# N type; convert celsius to microvolts
def n_c_to_uv(c):
    
    c = c + 0.0    
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

#N type; convert microvolt to celsius
def n_uv_to_c(uv):

    uv = uv + 0.0
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


 


