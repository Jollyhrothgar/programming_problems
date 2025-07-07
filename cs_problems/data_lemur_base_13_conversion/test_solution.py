from . import solution
from . import optimal_solution

def test_standard_solution():
  assert solution.convertToBase13(9) == "9"
  assert solution.convertToBase13(10) == "A"
  assert solution.convertToBase13(11) == "B"
  assert solution.convertToBase13(12) == "C"
  assert solution.convertToBase13(13) == "10"
  assert solution.convertToBase13(14) == "11"
  assert solution.convertToBase13(49) == "3A"
  assert solution.convertToBase13(69) == "54"
  assert solution.convertToBase13(-1845) == "-ABC"

def test_optimal_solution():
  assert optimal_solution.convertToBase13(9) == "9"
  assert optimal_solution.convertToBase13(10) == "A"
  assert optimal_solution.convertToBase13(11) == "B"
  assert optimal_solution.convertToBase13(12) == "C"
  assert optimal_solution.convertToBase13(13) == "10"
  assert optimal_solution.convertToBase13(14) == "11"
  assert optimal_solution.convertToBase13(49) == "3A"
  assert optimal_solution.convertToBase13(69) == "54"
  assert optimal_solution.convertToBase13(-1845) == "-ABC"