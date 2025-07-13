"""A unified test suite for the LeetCode-style solutions."""

import pytest
from .solution import Solution as UserSolution
from .optimal_solution import Solution as OptimalSolution

@pytest.mark.parametrize(
    "SolutionClass",
    [
      (UserSolution),
      (OptimalSolution)
    ]
)
@pytest.mark.parametrize(
    "nums, val, expected_k",
    [
      ([3, 2, 2, 3], 3, 2),
      ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5),
    ]
)

def test_solutions(SolutionClass, nums, val, expected_k):
  """
  tests the solutions
  """
  print(f"\n--> Testing {SolutionClass.__name__} with nums={nums}, val={val}")
  sol = SolutionClass()
  k = sol.solve(nums, val)
  assert k == expected_k

