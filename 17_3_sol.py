def fib(num, cache):
	if num <= 2:
		return cache[num]

	if not cache.get(num):
		cache[num] = fib(num-1, cache) + fib(num-2, cache)

	return cache[num]

def fib_trailing_zeros(num):
	cache = {
		0: 0,
		1: 1,
		2: 1
	}
	fib_num = fib(num, cache)
	count = 0

	while not fib_num % 10:
		count += 1
		fib_num /= 10
	return count

fib_trailing_zeros(60)
