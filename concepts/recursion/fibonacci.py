import sys

def fibonacci(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
  n = int(sys.argv[1])
  print(f"Fibbonacci #{n}: {fibonacci(n)}")

