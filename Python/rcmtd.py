def MEMOIZEDCUTROD(p, n):
    r = []
    for i in range(0, n+1):
        r.append(-99999)
    return MEMOIZEDCUTRODAUX(p, n, r)


def MEMOIZEDCUTRODAUX(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -99999
        for i in range(1, n+1):
            q = max(q, p[i] + MEMOIZEDCUTRODAUX(p, n-i, r))
    r[n] = q
    return q


p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(MEMOIZEDCUTROD(p, 5))
