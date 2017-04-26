def has_winner(board):
  size = len(board)
  # check rows
  for row in board:
    start = 0
    next = 1
    while next < size:
      if row[start] != row[next]:
        break
      if next == size-1:
        return True
      next += 1
        
  # check columns
  column = 0
  while column < size:
    start = 0
    next = 1
    while next < size:
      if board[column][start] != board[column][next]:
        break
      if next == size-1:
        return True
      next += 1  
    column += 1  
  
  # check diagonals
