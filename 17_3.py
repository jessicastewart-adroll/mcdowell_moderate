def factorial_zeros(number):
	if number < 5:
		return 0

	if number == 5:
		return 1

	counts = {
		2: 1,
		5: 1
	}
	factorial_number = 6
	temp = factorial_number

	while factorial_number <= number:
		while not temp%5:
			temp /= 5
			counts[5] += 1
		while not temp%2:
			temp /= 2
			counts[2] += 1
		factorial_number += 1
		temp = factorial_number

	# factorial check
	# total = number
	# while number > 1:
	# 	number-=1
	# 	total *= number
	# print(total)

	total_zeros = 0
	total_zeros += min(counts[2], counts[5])

	return total_zeros

print(factorial_zeros(20))
print(factorial_zeros(6))
print(factorial_zeros(100))
