import time

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return(fibo(n-1)+fibo(n-2))

start = time.time()
print(fibo(1))
end = time.time()
Ftime = end - start
print("Time Taken: ", Ftime)

start = time.time()
print(fibo(3))
end = time.time()
Ftime = end - start
print("Time Taken: ", Ftime)

start = time.time()
print(fibo(11))
end = time.time()
Ftime = end - start
print("Time Taken: ", Ftime)

# print(fibo(107))
# print(fibo(8508))
# print(fibo(3033018665))
