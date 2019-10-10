import time

a = []

with open('SortedFile 3.txt') as filehandle:
    for i in filehandle.readlines():
        currentIndex = int(i)
        a.append(currentIndex)

start = time.time()

for i in range(0, len(a)-1):
    for j in range(0, len(a)-i-1):
        if a[j] > a[j+1]:
            t = a[j]
            a[j] = a[j+1]
            a[j+1] = t

end = time.time()
Ftime = end - start
print("Time Taken: ", Ftime)
# with open('SortedFile 2.txt', 'w') as filehandle:
#     filehandle.writelines("%s\n" % i for i in a)
