"""Test cases for fizz_buzz_sum."""


from . import fizz_buzz_sum as original_solution
from . import fizz_buzz_sum_optimal as optimal_solution

def test_fizz_buzz_sum():
  assert original_solution.fizz_buzz_sum(0)  == 0
  assert original_solution.fizz_buzz_sum(1)  == 0
  assert original_solution.fizz_buzz_sum(2)  == 0
  assert original_solution.fizz_buzz_sum(3)  == 0
  assert original_solution.fizz_buzz_sum(4)  == 3
  assert original_solution.fizz_buzz_sum(5)  == 3
  assert original_solution.fizz_buzz_sum(6)  == (3 + 5)
  assert original_solution.fizz_buzz_sum(7)  == (3 + 5 + 6)
  assert original_solution.fizz_buzz_sum(8)  == (3 + 5 + 6)
  assert original_solution.fizz_buzz_sum(9)  == (3 + 5 + 6)
  assert original_solution.fizz_buzz_sum(10) == (3 + 5 + 6 + 9)
  
def test_fizz_buzz_sum_optimal():
  assert optimal_solution.fizz_buzz_sum(0)  == 0
  assert optimal_solution.fizz_buzz_sum(1)  == 0
  assert optimal_solution.fizz_buzz_sum(2)  == 0
  assert optimal_solution.fizz_buzz_sum(3)  == 0
  assert optimal_solution.fizz_buzz_sum(4)  == 3
  assert optimal_solution.fizz_buzz_sum(5)  == 3
  assert optimal_solution.fizz_buzz_sum(6)  == (3 + 5)
  assert optimal_solution.fizz_buzz_sum(7)  == (3 + 5 + 6)
  assert optimal_solution.fizz_buzz_sum(8)  == (3 + 5 + 6)
  assert optimal_solution.fizz_buzz_sum(9)  == (3 + 5 + 6)
  assert optimal_solution.fizz_buzz_sum(10) == (3 + 5 + 6 + 9)
