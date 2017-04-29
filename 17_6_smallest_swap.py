def smallest_sort(array):
	start = 0
	n = len(array)
	counts = [0]*n
	end = n-1

	while start < end:
		if array[start] <= array[start+1]:
			counts[start+1] = counts[start]+1
		if array[end-1] <= array[end]:
			counts[end-1] = counts[end]+1

		start += 1
		end -= 1

	print(counts)

smallest_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])
