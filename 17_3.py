def factorial_zeros(number):
	if number <= 0:
		return 0

	factorial = 1
	i = 1
	while i <= number:
		factorial *= i
		i += 1

	zeros = 0
	while not factorial%10:
		zeros += 1
		factorial /= 10

	return zeros

print(factorial_zeros(20))
print(factorial_zeros(4))
print(factorial_zeros(10))
