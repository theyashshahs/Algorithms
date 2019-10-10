import time

def binary(ar,lo,hi,num):
    while(lo<hi):
        mid = int((lo+hi)/2)
        if (a[mid]==num):
            break
        elif (a[mid]<num):
            lo = mid+1
        elif (a[mid]>num):
            hi = mid-1

a = []

with open('File 10.txt') as filehandle:
    for i in filehandle.readlines():
        currentIndex = int(i)
        a.append(currentIndex)

a.sort()

start = time.time()

h = len(a)-1
l=0
print("Best Case")
n = a[int((l+h)/2)]+1
pos = binary(a,l,h,n)

end = time.time()
Ftime = end - start
print("Time Taken: {:.6f}".format(Ftime))
start = time.time()

print("Worst Case")
n = a[h]+1
pos = binary(a,l,h,n)

end = time.time()
Ftime = end - start
print("Time Taken: ",Ftime)