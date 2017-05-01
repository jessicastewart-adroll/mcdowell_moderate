def fib(num):
	cache = {
		0: 0,
		1: 1,
		2: 1
	}
	if num <= 2:
		return cache[num]

	if not cache.get(num):
		cache[num] = fib(num-1) + fib(num-2)

	return cache[num]

def fib_trailing_zeros(num):
	fib_num = fib(num)
	count = 0

	while not fib_num % 10:
		count += 1
		fib_num /= 10

	return count
