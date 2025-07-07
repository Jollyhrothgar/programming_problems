"""An optimal solution for the same stripes problem."""

from typing import List

def is_same_stripes(matrix: List[List[int]]) -> bool:
  """
  Determines if a matrix has uniform diagonal stripes.

  This optimal solution iterates through the matrix and checks if each
  element is equal to its bottom-right neighbor.

  Time Complexity: O(m * n)
  Space Complexity: O(1)
  """
  if not matrix or not matrix[0]:
    return True # An empty matrix is considered valid.

  m = len(matrix)
  n = len(matrix[0])

  # Iterate through each element that has a bottom-right neighbor.
  # We only need to go up to the second-to-last row and column.
  for row in range(m - 1):
    for col in range(n - 1):
      # If an element does not match its bottom-right neighbor,
      # we have found a broken stripe.
      if matrix[row][col] != matrix[row + 1][col + 1]:
        return False
  
  # If we get through the entire loop without finding any mismatches,
  # all stripes must be uniform.
  return True
