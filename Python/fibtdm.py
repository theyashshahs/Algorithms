import time


def fibo(n, a):

    if n == 0 or n == 1:
        a[n] = n
    if a[n] is None:
        a[n] = fibo(n-1, a) + fibo(n-2, a)
    return a[n]


a = [None]*(1000)

start = time.time()
print(fibo(1, a))
end = time.time()
Ftime = end - start
print "Time Taken: ", Ftime

start = time.time()
print(fibo(3, a))
end = time.time()
Ftime = end - start
print "Time Taken: ", Ftime

start = time.time()
print(fibo(11, a))
end = time.time()
Ftime = end - start
print "Time Taken: ", Ftime

start = time.time()
print(fibo(107, a))
end = time.time()
Ftime = end - start
print "Time Taken: ", Ftime

# start = time.time()
# print(fibo(8508, a))
# end = time.time()
# Ftime = end - start
# print("Time Taken: ", Ftime)
