# check for already sorted
# check for swap 1
# quicksort
def smallest_sort(array):
	i = 0
	n = len(array) - 1

	while i < len(array):
	 	if array[i] > array[i+1]:
	 		break
 		i += 1

	while n > 0:
		if array[n-1] > array[n]:
			break
		n -= 1

	smallest = min(array[i:n+1])
	largest = max(array[i:n+1])	

	# debug
	# print(smallest, largest)
	# print(array[i:n+1])

	i -= 1
	while smallest < array[i] and i >= 0:
		i -= 1

	n += 1
	while largest > array[n] and n < len(array):
		n += 1

	return (i+1, n-1)

print(smallest_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
