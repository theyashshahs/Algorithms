import time

for z in range(1, 2):
    a = []

    with open('File '+str(z)+'.txt') as filehandle:
        for i in filehandle.readlines():
            currentIndex = int(i)
            a.append(currentIndex)

    def mergeSort(a):
        if len(a) > 1:
            m1 = int(len(a)/3)
            m2 = m1*2 + 1
            l = a[:m1]
            m = a[m1:m2]
            r = a[m2:]
            mergeSort(l)
            mergeSort(m)
            mergeSort(r)
            i = 0
            j = 0
            k = 0
            s = 0

            while i < len(l) and j < len(m) and k < len(r):
                if l[i] < r[j] and l[i] < m[k]:
                    a[s] = l[i]
                    i += 1
                elif r[j] < m[k]:
                    a[s] = r[j]
                    j += 1
                else:
                    a[s] = m[k]
                    k += 1
                s += 1

            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    a[s] = l[i]
                    i += 1
                else:
                    a[s] = r[j]
                    j += 1
                s += 1

            while i < len(l) and k < len(m):
                if l[i] < m[k]:
                    a[s] = l[i]
                    i += 1
                else:
                    a[s] = m[k]
                    k += 1
                s += 1

            while k < len(m) and j < len(r):
                if m[k] < r[j]:
                    a[s] = m[k]
                    k += 1
                else:
                    a[s] = r[j]
                    j += 1
                s += 1

            while i < len(l):
                a[s] = l[i]
                i += 1
                s += 1

            while j < len(r):
                a[s] = r[j]
                j += 1
                s += 1

            while k < len(m):
                a[s] = m[k]
                k += 1
                s += 1

    start = time.time()
    a.reverse()
    mergeSort(a)

    end = time.time()
    Ftime = end - start
    print("Time Taken: ", Ftime)

    # with open('SortedFile '+str(z)+'.txt', 'w') as filehandle:
    #     filehandle.writelines("%s\n" % i for i in a)
