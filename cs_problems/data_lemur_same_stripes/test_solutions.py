"""A unified test suite for the same stripes problem."""

import pytest
from .solution import is_same_stripes as standard_solution
from .optimal_solution import is_same_stripes as optimal_solution

# A list of test cases: (input_matrix, expected_result)
test_data = [
    ([[0]], True),
    ([[1, 0], [0, 1]], True),
    ([[1, 0], [1, 0]], False),
    ([[42, 7, 13, 99], [6, 42, 7, 13], [1, 6, 42, 7]], True),
    ([[42, 8, 13, 99], [6, 42, 7, 13], [1, 6, 42, 7]], False),
]

# A list of human-readable IDs for each test case
test_ids = [
    "trivial_1x1",
    "square_valid",
    "square_invalid",
    "nonsquare_valid",
    "nonsquare_invalid",
]

# We stack decorators to test every combination of solution and test data.
@pytest.mark.parametrize("solution_function", [standard_solution, optimal_solution], ids=["standard", "optimal"])
@pytest.mark.parametrize("test_input, expected_output", test_data, ids=test_ids)
def test_is_same_stripes(solution_function, test_input, expected_output):
    """
    Tests a given solution function with a specific input and expected output.
    """
    assert solution_function(test_input) == expected_output
