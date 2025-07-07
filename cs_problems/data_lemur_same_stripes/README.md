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

# Solution Analysis
