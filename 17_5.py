## pseudo-hits can only be used once
## frequency table

import random

class MasterMind(object):
	COLORS = 'RYGB'
	GUESS_LENGTH = 4

	def __init__(self):
		self.solution = None

	def generate_solution(self):
		solution = []

		i = 0
		while i < MasterMind.GUESS_LENGTH:
			random_num = random.randint(0, MasterMind.GUESS_LENGTH-1)
			solution.append(MasterMind.COLORS[random_num])
			i += 1 

		self.solution = solution

	def guess(self, guess):
		result = {
			'hits': 0,
			'pseudo-hits': 0
		}
		pseudo_candidates = []
		solution_candidates = []

		if len(guess) != MasterMind.GUESS_LENGTH:
			return

		if set(guess) - set(MasterMind.COLORS):
			return

		i = 0
		while i < MasterMind.GUESS_LENGTH:
			if guess[i] == self.solution[i]:
				result['hits'] += 1
			else:
				pseudo_candidates.append(guess[i])
				solution_candidates.append(self.solution[i])
			i += 1

		for char in pseudo_candidates:
			if char in solution_candidates:
				result['pseudo-hits'] += 1

		return result


	
mm_1 = MasterMind()
mm_1.generate_solution()
print(mm_1.guess('RGGB'))

mm_2= MasterMind()
mm_2.generate_solution()
print(mm_2.guess('RGBY'))
