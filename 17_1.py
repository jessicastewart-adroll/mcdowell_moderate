def arithmetic_swap(x, y):
	print('Before', x, y)
	x = x-y
	y += x
	x = y-x
	print('After', x, y)


def bitwise_swap(x, y):
	print('Before', x, y)
	x = x^y
	y = x^y
	x = x^y
	print('After', x, y)

bitwise_swap(1, 2)
bitwise_swap(-11, 32)
arithmetic_swap(1, 2)
arithmetic_swap(-11, 32)
arithmetic_swap(19.6, 2.8)
