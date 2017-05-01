# big O: size**2 time, 2(size*2+2) space
def increment_scores(scores, x, y, size):
	scores[x] += 1
	scores[size+y] += 1
	if x == y:
		scores[-2] += 1
	if size - 1 - x == y:
		scores[-1] += 1

def has_winner(board, player_one, player_two):
	size = len(board)
	column = 0
	scores_player_one = [0]*(size*2+2)
	scores_player_two = [0]*(size*2+2)

	while column < size:
		row = 0
		while row < size:
			if board[column][row] == player_one:
				increment_scores(scores_player_one, row, column, size)
			elif board[column][row] == player_two:
				increment_scores(scores_player_two, row, column, size)
			row += 1
		column += 1

	print(scores_player_one)
	print(scores_player_two)
	if max(scores_player_one) == size or max(scores_player_two) == size:
		return True
	else:
		return False

test_one = [
[0, None, 0],
[None, 1, None],
[None, 1, 1]
]

test_two = [
[0, None, 0],
[1, 1, None],
[None, 1, 1]
]

test_col = [
[0, 1, 0],
[None, 1, None],
[None, 1, 1]
]

test_row = [
[0, 0, 0],
[None, 1, None],
[None, 1, 1]
]

test_forward = [
[1, 0, 0],
[None, 1, None],
[None, 1, 1]
]

test_back = [
[1, 0, 0],
[None, 0, None],
[0, 1, 1]
]

print(has_winner(test_one, 0, 1))
print(has_winner(test_two, 0, 1))
print(has_winner(test_col, 0, 1))
print(has_winner(test_row, 0, 1))
print(has_winner(test_forward, 0, 1))
print(has_winner(test_back, 0, 1))
