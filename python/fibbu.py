import time

def fib(n):
    f = [0]*(n+1)
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

start = time.time()
print(fib(1))
end = time.time()
Ftime = end - start
print("Time Taken: ", Ftime)

start = time.time()
print(fib(3))
end = time.time()
Ftime = end - start
print("Time Taken: ", Ftime)

start = time.time()
print(fib(11))
end = time.time()
Ftime = end - start
print("Time Taken: ", Ftime)

start = time.time()
print(fib(107))
end = time.time()
Ftime = end - start
print("Time Taken: ", Ftime)

start = time.time()
print(fib(8508))
end = time.time()
Ftime = end - start
print("Time Taken: ", Ftime)

# start = time.time()
# print(fib(3033018665))
# end = time.time()
# Ftime = end - start
# print("Time Taken: ", Ftime)
