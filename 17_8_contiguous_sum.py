def longest_sum(array):
	i = 0
	n = len(array)
	sums = []
	while i < n:
		j = i + 1
		while j < n:
			sums.append((sum(array[i:j]), array[i:j]))
			j += 1
		i += 1

	largest = max(sums)
	return largest

print(longest_sum([2, -8, 3, -2, 4, -10]))
