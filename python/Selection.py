import time

a = []

with open('SortedFile 3.txt', 'r') as filehandle:
    for i in filehandle.readlines():
        currentIndex = int(i)
        a.append(currentIndex)

start = time.time()

for i in range(0,len(a)):
    min = i
    for j in range(i+1,len(a)):
        if a[min]<a[j]:
            min = j
    a[i],a[min] = a[min],a[i]

end = time.time()
Ftime = end - start
print("Time Taken: ",Ftime)
"""with open('SortedFile.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % i for i in a)"""