"""Recursive implementation of the factorial function"""
import sys
import math

def factorial(n):
  print(f"Step {n}")
  if n == 1:
    return 1
  else:
    return n * factorial(n - 1)

if __name__ == '__main__':
  n = int(sys.argv[1])
  print(f"Factorial: {n}")
  result = factorial(n)
  check_val = math.factorial(n)
  print(f"Result is {result} -> Check: {check_val}, {result == check_val}")
