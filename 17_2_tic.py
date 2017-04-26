def has_winner(board):
  size = len(board)
  
  # check rows
  row = 0
  while row < size:
    start = 0
    next = 1
    while next < size:
      if board[row][start] != board[row][next]:
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
      if board[start][column] != board[next][column]:
        break
      if next == size-1:
        return True
      next += 1  
    column += 1  
  
  # \ diagonal
  start = board[0][0]
  next = 1
  while next < size:
    if board[next][next] != start:
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
    if board[i][j] != start:
      break
    if j == size-1:
      return True
      
  return False    
      
test_one = [[None, None, None],
[None, None, None],
[None, None, None]]
print(has_winner(test_one))
