import time

def fib(n): 
	a = 0
	b = 1
	if n <= 1:
		return n
	else: 
		for i in range(2,n+1): 
			c = a + b 
			a = b 
			b = c 
		return b 

start = time.time()
print(fib(1))
end = time.time()
Ftime = end - start
print "Time Taken: ", Ftime

start = time.time()
print(fib(3))
end = time.time()
Ftime = end - start
print "Time Taken: ", Ftime

start = time.time()
print(fib(11))
end = time.time()
Ftime = end - start
print "Time Taken: ", Ftime

start = time.time()
print(fib(107))
end = time.time()
Ftime = end - start
print "Time Taken: ", Ftime

start = time.time()
print(fib(8508))
end = time.time()
Ftime = end - start
print "Time Taken: ", Ftime

start = time.time()
print(fib(3033018665))
end = time.time()
Ftime = end - start
print "Time Taken: ", Ftime
