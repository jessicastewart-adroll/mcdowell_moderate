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
  
  # check diagonals
