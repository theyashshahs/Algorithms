import time

for z in range(1, 6):
    a = []

    with open('File '+str(z)+'.txt') as filehandle:
        for i in filehandle.readlines():
            currentIndex = int(i)
            a.append(currentIndex)

    def mergeSort(alist, start, end):
        if end - start > 1:
            mid = (start + end)//2
            mergeSort(alist, start, mid)
            mergeSort(alist, mid, end)
            merge(alist, start, mid, end)

    def merge(alist, start, mid, end):
        left = alist[start:mid]
        right = alist[mid:end]
        k = start
        i = 0
        j = 0
        while (start + i < mid and mid + j < end):
            if (left[i] <= right[j]):
                alist[k] = left[i]
                i = i + 1
            else:
                alist[k] = right[j]
                j = j + 1
            k = k + 1
        if start + i < mid:
            while k < end:
                alist[k] = left[i]
                i = i + 1
                k = k + 1
        else:
            while k < end:
                alist[k] = right[j]
                j = j + 1
                k = k + 1

    start = time.time()
    a.reverse()
    mergeSort(a, 0, int(len(a)))

    end = time.time()
    Ftime = end - start
    print("File No.", z)
    print("Time Taken: ", Ftime)

    # with open('SortedFile '+str(z)+'.txt', 'w') as filehandle:
    #     filehandle.writelines("%s\n" % i for i in a)
