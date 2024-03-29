import time

def fib(n): 
	F = [[1, 1], [1, 0]] 
	if (n == 0): 
		return 0
	power(F, n - 1) 
	return F[0][0] 

def multiply(F, M): 

	x = (F[0][0] * M[0][0] + F[0][1] * M[1][0]) 
	y = (F[0][0] * M[0][1] + F[0][1] * M[1][1]) 
	z = (F[1][0] * M[0][0] + F[1][1] * M[1][0]) 
	w = (F[1][0] * M[0][1] + F[1][1] * M[1][1]) 
	
	F[0][0] = x
	F[0][1] = y
	F[1][0] = z
	F[1][1] = w

def power(F, n): 

	M = [[1, 1],[1, 0]] 

	for i in range(2, n + 1): 
		multiply(F, M) 

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
