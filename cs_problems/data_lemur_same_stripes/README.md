# Question

You are given an m x n matrix. Your task is to determine if the matrix has diagonal stripes where all elements in each diagonal from top-left to bottom-right are of the same stripe—that is, they are identical.

In this context, each diagonal stripe runs from the top-left corner to the bottom-right corner of the matrix. Check if every diagonal stripe consists entirely of the same number.

Return True if all diagonal stripes are of the same stripe, otherwise return False.

# Thinking

- This is an indexing problem that essentially requires us to check each diagnoal has the same numbers.
- There's probably a really cool two-liner solution where the matrix is reshaped
- I'll try for a solution where we just loop over diagnoals.
- Every diagonal starts on the left-most column or the top-most row.
- A cute solution would be to count the number of unique diagonals and then count the number of
  unique numbers, but this fails to account for instances where the numbers are mixed up.

# Solution

## Solution Analysis

### 1. User's Solution (`solution.py`)
-   **Approach:** The solution iterates through each possible starting point of a diagonal stripe. It starts by checking all diagonals that begin from the last row up to the first row (at column 0). Then, it checks all diagonals that begin from the second column to the last column (at row 0). For each diagonal, it traverses it from top-left to bottom-right, comparing each element with the next one. If any two adjacent elements on the same diagonal are different, it immediately returns `False`. If all diagonals are checked without finding any mismatches, it returns `True`.
-   **Time Complexity:** `O(m * n)`. In the worst case, every element in the `m x n` matrix is visited at least once. The nested loops might seem to suggest a higher complexity, but the inner `while` loop's total iterations are bounded by the number of cells in the matrix.
-   **Space Complexity:** `O(1)`. The solution uses only a few variables to keep track of the current position (`row`, `col`) and the value being checked. No extra space proportional to the input size is required.
