#!/bin/bash

# A script to scaffold a new problem directory within the cs_problems folder.
# Supports both functional and LeetCode class-based styles.

# --- 1. Argument Parsing ---
# Initialize a flag for the style. Default is functional.
is_leetcode_style=false

# Check if the first argument is the --leetcode flag.
if [ "$1" == "--leetcode" ]; then
  is_leetcode_style=true
  shift # Remove the flag from the arguments list, so $1 is now the problem name.
fi

# --- 2. Input Validation ---
# After potentially shifting, we should have exactly one argument left.
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 [--leetcode] <problem_name>"
  echo "Example (functional): $0 two_sum_leetcode_1"
  echo "Example (LeetCode):   $0 --leetcode valid_parentheses_20"
  exit 1
fi

# --- 3. Define Paths ---
PROBLEM_NAME=$1
BASE_DIR="cs_problems"
PROBLEM_DIR="$BASE_DIR/$PROBLEM_NAME"

# Check if the problem directory already exists.
if [ -d "$PROBLEM_DIR" ]; then
  echo "Error: Directory '$PROBLEM_DIR' already exists."
  exit 1
fi

# --- 4. Create Directory and Files ---
echo "Creating new problem directory: $PROBLEM_DIR"
mkdir -p "$PROBLEM_DIR"

# --- Create README.md with boilerplate headings ---
cat <<EOF > "$PROBLEM_DIR/README.md"
# Question

# Thinking

# Solution

# Solution Analysis
EOF

# --- Create empty __init__.py ---
touch "$PROBLEM_DIR/__init__.py"

# --- Conditionally Create Boilerplate Files ---
if [ "$is_leetcode_style" = true ]; then
  # --- LeetCode Style (Class-based) ---
  echo "Generating LeetCode style (class-based) templates..."

  cat <<'EOF' > "$PROBLEM_DIR/solution.py"
"""A standard solution for the problem (LeetCode style)."""

from typing import List

class Solution:
  def solve(self, input_data):
    # Your standard solution code here.
    # Remember to use two-space indentation.
    pass
EOF

  cat <<'EOF' > "$PROBLEM_DIR/optimal_solution.py"
"""An optimal solution for the problem (LeetCode style)."""

from typing import List

class Solution:
  def solve(self, input_data):
    # Your optimal solution code here.
    # Remember to use two-space indentation.
    pass
EOF

  cat <<'EOF' > "$PROBLEM_DIR/test_solutions.py"
"""A unified test suite for the LeetCode-style solutions."""

import pytest
from .solution import Solution as StandardSolution
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

@pytest.mark.parametrize("SolutionClass", [StandardSolution, OptimalSolution], ids=["standard", "optimal"])
@pytest.mark.parametrize("test_input, expected_output", test_data, ids=test_ids)
def test_solve(SolutionClass, test_input, expected_output):
    """
    Tests a given solution class with a specific input and expected output.
    """
    solver = SolutionClass()
    assert solver.solve(test_input) == expected_output
EOF

else
  # --- Functional Style (Default) ---
  echo "Generating functional style templates..."

  cat <<'EOF' > "$PROBLEM_DIR/solution.py"
"""A standard solution for the problem."""

from typing import List

def solve(input_data):
  # Your standard solution code here.
  # Remember to use two-space indentation.
  pass
EOF

  cat <<'EOF' > "$PROBLEM_DIR/optimal_solution.py"
"""An optimal solution for the problem."""

from typing import List

def solve(input_data):
  # Your optimal solution code here.
  # Remember to use two-space indentation.
  pass
EOF

  cat <<'EOF' > "$PROBLEM_DIR/test_solutions.py"
"""A unified test suite for the functional solutions."""

import pytest
from .solution import solve as standard_solution
from .optimal_solution import solve as optimal_solution

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

@pytest.mark.parametrize("solution_function", [standard_solution, optimal_solution], ids=["standard", "optimal"])
@pytest.mark.parametrize("test_input, expected_output", test_data, ids=test_ids)
def test_solve(solution_function, test_input, expected_output):
    """
    Tests a given solution function with a specific input and expected output.
    """
    assert solution_function(test_input) == expected_output
EOF
fi

echo "Successfully created problem: $PROBLEM_NAME"
tree "$PROBLEM_DIR"