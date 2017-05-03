def max_no_conditional(x, y):
	return x + (x-y>>64) * (x-y)

print(max_no_conditional(5, 7))
print(max_no_conditional(7, 5))
print(max_no_conditional(-7000000000087554, 5))
print(max_no_conditional(-7000000000087554, -5))
