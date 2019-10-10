def karatsuba(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        m = max(len(str(x)), len(str(y)))
        m2 = m // 2

        a = x // 10**(m2)
        b = x % 10**(m2)
        c = y // 10**(m2)
        d = y % 10**(m2)

        z0 = karatsuba(b, d)
        z1 = karatsuba((a+b), (c+d))
        z2 = karatsuba(a, c)

        return (z2 * 10**(2*m2)) + ((z1 - z2 - z0) * 10**(m2)) + (z0)


a = 12
b = 5
print(karatsuba(a, b))

a = 7125486542
b = 23456583
print(karatsuba(a, b))

a = 742136284561247845962145632140
b = 214510102547219842103256421872
print(karatsuba(a, b))
