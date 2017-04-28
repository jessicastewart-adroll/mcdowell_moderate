# bitwise?
def count_min(a, b):
	buffer = [0 for i in range(a+b+1)]

	i = 0
	while i < len(buffer):
		if i == a or i == b:
			buffer[i] += 1
		i += 1

	i = 0
	while i < len(buffer):
		if buffer[i]:
			return i
		i += 1

def count_max(a, b):
	buffer = [0 for i in range(a+b+1)]

	i = 0
	while i < len(buffer):
		if i == a or i == b:
			buffer[i] += 1
		i += 1

	i = len(buffer)-1
	while i >= 0:
		if buffer[i]:
			return i
		i -= 1

print(count_max(10, 30))

def bucket_max(a, b):
	negative_values = []
	positive_values = []

	if abs(a) != a:
		negative_values.append(a)
	else:
		positive_values.append(a)

	if abs(b) != b:
		negative_values.append(b)
	else:
		positive_values.append(b)

	if len(positive_values) == len(negative_values):
		return positive_values[0]

	if positive_values:
		return count_max(a, b)

	if negative_values:
		return -count_min(abs(a), abs(b))

print(bucket_max(-10, -30))

def max_floating_point(a, b):
	a_len = str(a).split('.')
	b_len = str(b).split('.')

	if len(a_len) == 1 and len(b_len) == 1:
		return bucket_max(a, b)
	elif len(a_len) == 2 and len(b_len) == 2:
		multiplier = count_max(len(a_len[1]), len(b_len[1]))
	elif len(a_len) == 2:
		multiplier = len(a_len[1])
	else:
		multiplier = len(b_len[1])

	lookup = {}
	mult_a = int(multiplier*10*a)
	mult_b = int(multiplier*10*b)
	lookup[mult_a] = a
	lookup[mult_b] = b

	int_max = bucket_max(mult_a, mult_b)

	return lookup[int_max]

print(max_floating_point(.6, -7.59))
