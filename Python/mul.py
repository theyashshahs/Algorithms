def product(x=[], y=[], *args):
    q = 0
    n = int(len(x))
    m = int(len(y))
    s = 0
    if max(n, m) == 1:
        return(x[0]*y[0])
    p = []
    for i in range(m):
        q = 0
        for j in range(n):
            if i == 0:
                p.append(q + x[j]*y[i])
            else:
                p[i+j-1] += q + x[j]*y[i]
            q = p[i+j-1]/10
            p[i+j-1] = p[i+j-1] % 10
        p[i+n-1] += q
        s = p[i+j-1]*pow(10, m) + product(x[int(n/2):], y[int(m/2):])
    return s


a = 12
b = 5
print(product(a, b))

a = 7125486542
b = 23456583
print(product(a, b))

a = 742136284561247845962145632140
b = 214510102547219842103256421872
print(product(a, b))
