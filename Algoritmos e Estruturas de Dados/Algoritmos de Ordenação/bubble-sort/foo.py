def bubble_sort(array):
	i = len(array) - 1
	# print(i)
	# print(list(range(i)))
	while i >= 1:
		for j in range(i):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
		i -= 1

array = [333, 12, 5, 72, 1, 2, 12, 0 , 44]
# array = [33, 5, 7, 1, 2, 12 , 44]
print(array)
bubble_sort(array)
print(array)
