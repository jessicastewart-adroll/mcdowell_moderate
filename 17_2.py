# big O: size**2 time, size*2+2 space
def increment_scores(scores, x, y, size, player):
	scores[x] += player
	scores[size+y] += player
	if x == y:
		scores[-2] += player
	if size - 1 - x == y:
		scores[-1] += player

def has_winner(board, player_one, player_two):
	size = len(board)
	column = 0
	scores = [0]*(size*2+2)

	while column < size:
		row = 0
		while row < size:
			if board[column][row] == player_one:
				increment_scores(scores, row, column, size, 1)
			elif board[column][row] == player_two:
				increment_scores(scores, row, column, size, -1)
			row += 1
		column += 1

	return max(scores) == size or abs(min(scores)) == size

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
