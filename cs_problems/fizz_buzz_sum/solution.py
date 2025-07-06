"""Solution for the fizz_buzz_sum problem."""

memory = {}

def fizz_buzz_sum(target):
  """

  Computes the sum of all multiples of 3 or 5 below the target value.

  For example, if the target value was 10, the multiples of 3 or 5 below 10 are 3, 5, 6, and 9.

  Because 3 + 5 + 6 + 9 = 23, fizz_buzz_sum returns 23.

  Args:
    target: an integer
  Returns:
    The sum of all factors of 3 and 5 which are below target.

  """
  if target in memory:
    return memory[target]

  factors = []
  # Range generator starts at 0 or the value we supply and stops at the n-1 end value.
  for i in range(3, target):
    if i % 3 == 0 and i % 5 != 0:
      factors.append(i)
    elif i % 3 != 0 and i % 5 == 0:
      factors.append(i)
    elif i % 3 == 0 and i % 5 == 0:
      factors.append(i)
    memory[target] = sum(factors)
  
  # Case where the loop is not executed because of low values.
  if target not in memory:
    memory[target] = sum(factors)

  return memory[target]
