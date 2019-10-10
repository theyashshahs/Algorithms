import time
def linear (a,b):
 for i in range(0,len(a)):
   if a[i]==int(b):
       break
for j in range (1,11):
 print("File No :"+str(j))
 a = []
 string='File '+str(j)+'.txt'
 with open(string) as filehandle:
    for i in filehandle.readlines():
        currentIndex = int(i)
        a.append(currentIndex)
 filehandle.close()
 start = time.time()
 linear(a,a[0])
 end = time.time()
 Ftime = end - start
 print(" Best Time Taken: ",Ftime)
 start = time.time()
 linear(a,-500)
 end = time.time()
 Ftime = end - start
 print(" Worst Time Taken: ",Ftime)