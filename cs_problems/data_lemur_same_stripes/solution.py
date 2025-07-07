"""A standard solution for the problem."""

def is_same_stripes(matrix):
  """
  An m x n matrix with numbers is supplied and we have to check all diagnoals for the same content.

  Args:
    matrix: List[List] with m rows and n columns.
  """

  m = len(matrix)
  n = len(matrix[0])

  # Check from the bottom most row to the top most row, then proceed to the columns. The topmost row
  # is also the topmost column.
  
  # Row Check
  same_stripes = True
  for i in range(m-1, -1, -1):
    row = i
    col = 0
    while row < m and col < n:
      value = matrix[row][col]
      row += 1
      col += 1
      try:
        next_value = matrix[row][col]
        if next_value != value:
          return False
      except IndexError:
        break
      

  # Column Check
  for j in range(1, n):
    row = 0
    col = j
    while row < m and col < n:
      value = matrix[row][col]
      row += 1
      col += 1
      try:
        next_value = matrix[row][col]
        if next_value != value:
          return False
      except IndexError:
        break
  return same_stripes