from heapq import *

def smallest_sort(array):
	if len(array) < 2:
		return 

	heap = array[:]
	heapify(array)
	i = 0
	min_index = None
	max_index = None
	while heap:
		element = heappop(heap)
		if element != array[i]:
			if min_index == None:
				min_index = i
			else:
				max_index = i
		i += 1 

	if min_index == None:
		return (0, 0)

	return (min_index, max_index)

print(smallest_sort([]))
print(smallest_sort([1]))
print(smallest_sort([2, 3]))
print(smallest_sort([3, 2]))
print(smallest_sort([2, 3, 0]))
print(smallest_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
