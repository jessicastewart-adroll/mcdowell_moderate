from collections import defaultdict

def master_mind(guess, solution):
	result = {'hit': 0, 'pseudo-hit': 0}
	solution_counts = defaultdict(lambda: 0)
	guess_counts = defaultdict(lambda: 0)
	i = 0
	while i < 4:
		if guess[i] == solution[i]:
			result['hit'] += 1
		else:
			solution_counts[solution[i]] += 1
			guess_counts[guess[i]] += 1
		i += 1

	for letter in solution_counts:
		if solution_counts[letter] and guess_counts.get(letter):
			result['pseudo-hit'] += 1
			guess_counts[letter] -= 1
			solution_counts[letter] -= 1

	return result

print(master_mind('RGGB', 'YRGB'))
# hit: 2 pseudo: 1

print(master_mind('RGBY', 'GGRR'))
# hit: 1, pseudo: 1
