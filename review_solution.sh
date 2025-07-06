#!/bin/bash

# A script to display a LeetCode problem, solution, tests, and notes for review.

# --- 1. Input Validation ---
# Check if exactly one argument (the directory) was provided.
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <directory_name>"
  exit 1
fi

# Assign the first argument to a variable for clarity.
SOLUTION_DIR=$1
BASENAME=$(basename "$SOLUTION_DIR")

# Check if the provided argument is actually a directory.
if [ ! -d "$SOLUTION_DIR" ]; then
  echo "Error: Directory '$SOLUTION_DIR' not found."
  exit 1
fi

# --- 2. File Path Construction ---
# Construct the paths to the README, solution, and test files.
# This assumes a consistent naming convention.
README_FILE="$SOLUTION_DIR/README.md"
SOLUTION_FILE="$SOLUTION_DIR/$BASENAME.py"
TEST_FILE="$SOLUTION_DIR/test_$BASENAME.py"

# Check if the required files exist before trying to read them.
if [ ! -f "$README_FILE" ]; then
  echo "Error: README.md not found in '$SOLUTION_DIR'."
  exit 1
fi

if [ ! -f "$SOLUTION_FILE" ]; then
  echo "Error: Solution file '$SOLUTION_FILE' not found."
  exit 1
fi

if [ ! -f "$TEST_FILE" ]; then
  echo "Error: Test file '$TEST_FILE' not found."
  exit 1
fi

# --- 3. Output Formatting ---
# Clear the screen for a clean view.
clear

# Print the formatted output.
echo "=================================================="
echo "Here's my solution for: $BASENAME"
echo "=================================================="
echo ""
echo "--- Question ---"
# Use cat to print the contents of the README file.
cat "$README_FILE"
echo ""
echo ""
echo "--- Solution ---"
# Use cat to print the contents of the Python solution file.
cat "$SOLUTION_FILE"
echo ""
echo ""
echo "--- Tests ---"
# Use cat to print the contents of the Python test file.
cat "$TEST_FILE"
echo ""


