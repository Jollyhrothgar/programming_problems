"""A unified test suite for the LeetCode-style solutions."""

import pytest
from .solution import Solution as UserSolution
from .optimal_solution import Solution as OptimalSolution

# A list of test cases: (input_data, expected_result)
test_data = [
    ("sample_input_1", "sample_output_1"),
    ("sample_input_2", "sample_output_2"),
]

# A list of human-readable IDs for each test case
test_ids = [
    "sample_case_1",
    "sample_case_2",
]

@pytest.mark.parametrize("SolutionClass", [UserSolution, OptimalSolution], ids=["user", "optimal"])
@pytest.mark.parametrize("test_input, expected_output", test_data, ids=test_ids)
def test_solve(SolutionClass, test_input, expected_output):
    """
    Tests a given solution class with a specific input and expected output.
    """
    solver = SolutionClass()
    assert solver.solve(test_input) == expected_output
