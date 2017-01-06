def solution(X, Y, D):
    # min N:  X + ND >= Y
    import math
    N = math.ceil(float(Y-X)/D)  # float for Python2.7 division
    return int(N)
