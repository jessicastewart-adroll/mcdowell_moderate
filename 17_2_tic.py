def get_neighbors(graph, node):
	neighbors = []
	size = len(graph)
	moves = [(1, 0), (0, 1), (1, 1), (-1, 1)]
	for move in moves:
		neighbor = (move[0] + node[0], move[1] + node[1], node[2] + 1)
		if neighbor[0] >=0 and neighbor[1] >= 0 and neighbor[0] < size and neighbor[1] < size:
			if graph[node[0]][node[1]] == graph[neighbor[0]][neighbor[1]]:
				neighbors.append(neighbor)

	return neighbors

def dfs(graph, start):
	size = len(graph)
	stack = [start]

	while stack:
		node = stack.pop()
		if node[2] == size:
			print(node)
			return True

		for neighbor in get_neighbors(graph, node):
			stack.append((neighbor))


def has_winner(graph):
	pass

graph = [
[0, None, 1],
[0, None, None],
[1, 0, 0]
]

print(dfs(graph, (0, 0, 1)))

################################

def dfs(board, i, j, count):
  size = len(board)
  if i >= size or j >= size or not board[i][j]:
    return count
  else:  
    dfs(board, i+1, j, count+1)
    dfs(board, i, j+1, count+1)
    dfs(board, i+1, j+1, count+1)
  
def has_winner(board):
  size = len(board)
  i = 0
  j = 0
  while j < size:
    dfs(board, i, j, 0)

# big 0 -> n*n + n*n + 2n
# n = size of board
def has_winner(board):
  size = len(board)
  
  # check rows
  row = 0
  while row < size:
    start = 0
    next = 1
    while next < size:
      if board[row][start] == None or board[row][start] != board[row][next]:
        break
      if next == size-1:
        return True
      next += 1
    row += 1  
        
  # check columns
  column = 0
  while column < size:
    start = 0
    next = 1
    while next < size:
      if board[start][column] == None or board[start][column] != board[next][column]:
        break
      if next == size-1:
        return True
      next += 1  
    column += 1  
  
  # \ diagonal
  start = board[0][0]
  next = 1
  while next < size:
    if board[next][next] == None or board[next][next] != start:
      next = size
      break
    if next == size-1:
      return True
    next += 1 
    
  # / diagonal
  i = size-1
  j = 0
  start = board[i][j]
  next = (-1, 1)
  while i >= 0:
    i = i+next[0]
    j = j+next[1]
    if board[i][j] == None or board[i][j] != start:
      break
    if j == size-1:
      return True
      
  return False    
      
test_one = [[None, None, None],
[None, None, None],
[None, None, None]]
print(has_winner(test_one))

test_two = [[1, None, 1],
[None, None, None],
[None, None, 1]]
print(has_winner(test_two))

test_three = [[1, None, None],
[1, None, 1],
[None, None, None]]
print(has_winner(test_three))

test_four = [[None, None, None],
[0, 0, 0],
[None, None, None]]
print(has_winner(test_four))

test_five = [[None, None, 0],
[None, None, 0],
[None, None, 0]]
print(has_winner(test_five))

test_six = [[None, None, 0],
[None, 0, None],
[0, None, None]]
print(has_winner(test_six))

test_seven = [[1, None, None],
[None, 1, None],
[None, None, 1]]
print(has_winner(test_seven))
