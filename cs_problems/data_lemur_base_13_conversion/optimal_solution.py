"""An optimal solution for converting a number to its base-13 string representation."""

def convertToBase13(num: int) -> str:
  """
  Converts a base-10 integer to its base-13 string representation.

  This solution uses the standard algorithm of repeated division and
  modulo to find digits from right to left.

  Args:
    num: An integer in base-ten.
  
  Returns:
    A string representation of num in base-13.
  """
  if num == 0:
    return "0"

  # A string is a simple and effective map for 0-12 -> 0-C
  digit_map = "0123456789ABC"
  
  is_negative = num < 0
  if is_negative:
    num = -num

  result = ""
  while num > 0:
    remainder = num % 13
    result = digit_map[remainder] + result # Prepend the new digit
    num //= 13

  return "-" + result if is_negative else result