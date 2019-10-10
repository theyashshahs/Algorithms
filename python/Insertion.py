import time

a = []

with open('SortedFile 2.txt', 'r') as filehandle:
    for i in filehandle.readlines():
        currentIndex = int(i)
        a.append(currentIndex)

start = time.time()

for i in range(1,len(a)):
    cur = a[i]
    j = i-1
    while j>=0 and cur<a[j]:
        a[j+1] = a[j]
        j-=1
    a[j+1] = cur

end = time.time()
Ftime = end - start
print("Time Taken: ",Ftime)
"""with open('SortedFile 2.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % i for i in a)"""