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

print(count_max(10, 30)) # assumes positive integers

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

print(bucket_max(-10, -30)) # positive or negative integers

def get_max_float(a, b):
  # assumes positive or negative integers or floats
  pass
