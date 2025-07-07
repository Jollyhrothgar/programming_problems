"""Write a string representation of a number in base 13."""

def convertToBase13(num):
  """Assume at most a 5-digit base-13 number.
  
  Args:
    num: An integer in base-ten
  Returns:
    A string representation of num in base-13.
  """
  if num == 0:
    return "0"

  digit_map = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C" 
  }
  is_negative = False
  if num < 0:
    num = abs(num)
    is_negative = True
  
  number = ""
  max_digits = 10

  for i in range(max_digits, -1, -1):
    place_value = (13)**i
    digit = int(num / place_value)
    if i == max_digits and digit > 12:
      raise ValueError(f"Precision of {max_digits} is not sufficient for {num} 5-digit base-13 number")
    
    # Carry on.
    try:
      number += digit_map[digit]
    except KeyError:
      raise KeyError(f"Got key {digit}, expected in the range of 0-C")
    num -= digit * place_value

  sign = "-" if is_negative else ""
  return sign + number.lstrip("0")
