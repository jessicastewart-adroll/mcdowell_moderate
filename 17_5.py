import random
from collections import defaultdict

class MasterMind(object):
	COLORS = 'RYGB'
	GUESS_LENGTH = 4
	COLOR_CODES = {
		'R':0,
		'Y':1,
		'G':2,
		'B':3
	}

	def __init__(self):
		self.solution = None

	@classmethod
	def get_code(cls, letter):
		return cls.COLOR_CODES[letter]

	def generate_solution(self):
		solution = []

		i = 0
		while i < MasterMind.GUESS_LENGTH:
			random_num = random.randint(0, MasterMind.GUESS_LENGTH-1)
			solution.append(MasterMind.COLORS[random_num])
			i += 1 

		self.solution = solution

	def guess(self, guess):
		# debug
		# print('\n', self.solution)
		# print(guess)

		result = {
			'hits': 0,
			'pseudo-hits': 0
		}
		freqency_table = [0]*MasterMind.GUESS_LENGTH

		if len(guess) != MasterMind.GUESS_LENGTH:
			return

		if set(guess) - set(MasterMind.COLORS):
			return

		i = 0
		while i < MasterMind.GUESS_LENGTH:
			if guess[i] == self.solution[i]:
				result['hits'] += 1
			else:
				freqency_table[self.get_code(self.solution[i])] += 1
			i += 1

		i = 0
		while i < MasterMind.GUESS_LENGTH:
			if freqency_table[self.get_code(guess[i])] > 0 and guess[i] != self.solution[i]:
				freqency_table[self.get_code(guess[i])] -= 1
				result['pseudo-hits'] += 1
			i += 1

		return result

mm_2= MasterMind()
mm_2.generate_solution()
print(mm_2.guess('RGBY'))
print(mm_2.guess('RRRR'))
print(mm_2.guess('XX'))
print(mm_2.guess('BYGB'))
print(mm_2.guess('ZZZZ'))
