def zeros(x, y, left=True):
    if left == True:
        for i in range(y):
            x = '0' + x
        9
    else:
        for i in range(y):
            x = x+'0'
    return x


def mul(a, b):

    x = str(a)
    y = str(b)
    if (len(x) == 1 and len(y) == 1):
        return a*b
    elif (len(x) < len(y)):
        x = zeros(x, len(y)-len(x))
    elif (len(y) < len(x)):
        y = zeros(y, len(x)-len(y))
    n = len(x)
    j = n//2
    if (n % 2 != 0):
        j += 1
    BZeroPadding = n - j
    AZeroPadding = BZeroPadding * 2
    xl = int(x[:j])
    xr = int(x[j:])
    yl = int(y[:j])
    yr = int(y[j:])
    10
    r1 = mul(xl, yl)
    r2 = mul(xl, yr)
    r3 = mul(xr, yl)
    r4 = mul(yr, xr)
    return (int(zeros(str(r1), AZeroPadding, False)) + int(zeros(str(r2+r3), BZeroPadding, False)) + r4)


a = 150
b = 5
a1 = list(map(int, str(a)))
b1 = list(map(int, str(b)))

print(product(a1, b1))
