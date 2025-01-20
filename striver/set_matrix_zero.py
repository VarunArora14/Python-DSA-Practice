# input format is in form of array
matrix = [[1, 1, 1, 0], [1, 1, 1, 1], [1, 0, 1, 1], [0, 1, 1, 1]]

def partiallyOptimal(matrix:list[list[int]]):
  col_len = len(matrix)
  row_len = len(matrix[0])

  rows = set()
  cols = set()

  for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
      if matrix[i][j]==0:
        if i not in rows:
          rows.add(i)
        if j not in cols:
          cols.add(j)

  print(rows)
  print(cols)

  for row_idx in rows:
    for col_idx in range(col_len):
      matrix[row_idx][col_idx]=0
      
  for col_idx in cols:
    for row_idx in range(row_len):
      matrix[row_idx][col_idx]=0

  print(matrix)

def trulyOptimal(matrix:list[list[int]]):
  # we avoid any extra space and use the first row and first col as the storage to check if row/col is 0 or not
  # edge case occurs at 0,0 as (n,0) and (0,m) could both exist as well as just (n,0), so we use another variable for either row/col
  col0=1 # set this to 0 if the first column is 0
  
  m = len(matrix[0])
  n = len(matrix)
  
  # Mark the first elements of row and columns as 0
  for i in range(0,n):
    for j in range(0,m):
      if matrix[i][j]==0:
        
        # set first element of row to 0
        matrix[i][0]=0
        
        # mark jth column
        if j!=0:
          matrix[0][j]=0
        else:
          col0=0
  # Mark 0 from (1,1) to (n-1,m-1)
  for i in range(1,n):
    for j in range(1,m):
      if matrix[i][j]!=0:
        if matrix[i][0]==0 or matrix[0][j]==0:
          matrix[i][j]=0
  
  # handle edge case of first row and first col
  
  # first row set to 0 
  if matrix[0][0]==0:
    for j in range(m):
      matrix[0][j]=0

  # first column set to 0
  if col0==0:
    for i in range(n):
      matrix[i][0]=0
  
  print(matrix)
      
  
trulyOptimal(matrix=matrix)