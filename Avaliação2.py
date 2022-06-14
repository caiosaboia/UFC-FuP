def soma(x,y):
    W = []
    Z = []
    if len(x) != 0 and len(y) != 0 and len(x) == len(y):
        for e in range(0,len(x)):
            if 0 <= x[e] <= 1 and 0 <= y[e] <= 1:
                Z.append(x[e]^y[e])
        if len(Z) == len(x):
            return Z
    return W
