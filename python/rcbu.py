def BOTTOMUPCUTROD(p, n):
    r = [0]*10
    r[0] = 0
    for j in range(1, n+1):
        q = -99999
        for i in range(1, j+1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]


p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(BOTTOMUPCUTROD(p, 5))
