import random

class MasterMind(object):
	COLORS = 'RYGB'
	GUESS_LENGTH = 4

	def __init__(self):
		self.result = {
			'hits': 0,
			'pseudo-hits': 0
			}
		self.pseudo_guess_candidates = list()
		self.pseudo_solution_candidates = list()
		self.solution = MasterMind.generate_solution()

	@classmethod
	def generate_solution(cls):
		solution = list()

		i = 0
		while i < cls.GUESS_LENGTH:
			random_num = random.randint(0, cls.GUESS_LENGTH-1)
			solution.append(cls.COLORS[random_num])
			i += 1 

		return solution

	def master_mind(self, guess):
		print(self.solution)
		if len(guess) != MasterMind.GUESS_LENGTH:
			return

		if set(guess) - set(MasterMind.COLORS):
			return

		i = 0
		while i < MasterMind.GUESS_LENGTH:
			if guess[i] == self.solution[i]:
				self.result['hits'] += 1
			else:
				self.pseudo_guess_candidates.append(guess[i])
				self.pseudo_solution_candidates.append(guess[i])
			i += 1

		for char in self.pseudo_guess_candidates:
			if char in self.pseudo_solution_candidates:
				self.result['pseudo-hits'] += 1

		return self.result


	
mm_1 = MasterMind()
print(mm_1.master_mind('RGGB'))
# 'YRGB'
# hit: 2 pseudo: 1

mm_2= MasterMind()
print(mm_2.master_mind('RGBY'))
# 'GGRR'
# hit: 1, pseudo: 1
