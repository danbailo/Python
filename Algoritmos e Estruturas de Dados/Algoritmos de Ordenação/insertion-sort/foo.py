def insertionSort(alist):

   for i in range(1,len(alist)):

       #element to be compared
       current = alist[i]

       #comparing the current element with the sorted portion and swapping
       while i>0 and alist[i-1]>current:
           alist[i] = alist[i-1]
           i = i-1
           alist[i] = current

       #print(alist)

   return alist

array = [0, 12, 5, 72, 1, 2, 12, 333 , 44]
print(array)

insertionSort(array)
print(array)