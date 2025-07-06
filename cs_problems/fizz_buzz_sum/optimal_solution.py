"""Optimal solution for the fizz_buzz_sum problem using a bottom-up DP (dynamic programming)
approach."""

# The cache now acts as our "table" for tabulation.
# The key is the target, and the value is the sum of multiples below it.
memory = {0: 0}

def fizz_buzz_sum(target):
  """
  Computes the sum of all multiples of 3 or 5 below the target value. This version builds upon
  previous calculations for efficiency using an optimal bottom-up dynamic programming approach.

  Args:
    target: An integer specifying the upper limit (exclusive).

  Returns:
    The integer sum of all multiples of 3 or 5 below the target.
  """
  # If we have already fully computed the answer for this target, return it.
  if target in memory:
    return memory[target]

  # Find the largest target we've already solved for. This is our starting point.
  last_known_target = max(memory.keys())
  current_sum = memory[last_known_target]

  # Iterate only from our last known point up to the new target.
  # This is the key optimization you were aiming for.
  for i in range(last_known_target, target):
    # The sum for the next number (i + 1) is the current_sum...
    memory[i + 1] = current_sum
    # ...plus the number `i` itself, if `i` is a multiple of 3 or 5.
    if i % 3 == 0 or i % 5 == 0:
      current_sum += i
      memory[i + 1] = current_sum
  
  return memory[target]

