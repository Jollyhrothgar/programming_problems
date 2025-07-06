#!/bin/bash

# A script to display a LeetCode problem, all associated solutions,
# and all test files for a comprehensive review.

# --- 1. Input Validation ---
# Check if exactly one argument (the directory) was provided.
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <directory_name>"
  exit 1
fi

# Assign the first argument to a variable for clarity.
SOLUTION_DIR=$1

# Check if the provided argument is actually a directory.
if [ ! -d "$SOLUTION_DIR" ]; then
  echo "Error: Directory '$SOLUTION_DIR' not found."
  exit 1
fi

# --- 2. Output Formatting & README ---
# Clear the screen for a clean view.
clear

echo "=================================================="
echo "Here's my solution for: $(basename "$SOLUTION_DIR")"
echo "=================================================="
echo ""
echo "--- Question ---"

README_FILE="$SOLUTION_DIR/README.md"
if [ -f "$README_FILE" ]; then
  cat "$README_FILE"
else
  echo "README.md not found."
fi
echo ""

# --- 3. Find and Display All Solutions ---
# This section dynamically finds any file starting with 'solution'.
echo "--- Solutions ---"
solution_found=false
# Loop through all files matching the 'solution*.py' pattern.
for file in "$SOLUTION_DIR"/solution*.py; do
  # The check '[ -f "$file" ]' is crucial. If no files match the pattern,
  # the loop will still run once with the literal string. This check prevents that.
  if [ -f "$file" ]; then
    echo ""
    echo "## File: $(basename "$file")"
    echo "--------------------------------------------------"
    cat "$file"
    solution_found=true
  fi
done

if ! $solution_found; then
  echo "No standard solution files (solution*.py) found."
fi
echo ""

# --- 4. Find and Display All Optimal Solutions ---
echo "--- Optimal Solutions ---"
optimal_found=false
for file in "$SOLUTION_DIR"/optimal_solution*.py; do
  if [ -f "$file" ]; then
    echo ""
    echo "## File: $(basename "$file")"
    echo "--------------------------------------------------"
    cat "$file"
    optimal_found=true
  fi
done

if ! $optimal_found; then
  echo "No optimal solution files (optimal_solution*.py) found."
fi
echo ""

# --- 5. Find and Display All Test Files ---
echo "--- Tests ---"
tests_found=false
for file in "$SOLUTION_DIR"/test_*.py; do
  if [ -f "$file" ]; then
    echo ""
    echo "## File: $(basename "$file")"
    echo "--------------------------------------------------"
    cat "$file"
    tests_found=true
  fi
done

if ! $tests_found; then
  echo "No test files (test_*.py) found."
fi
echo ""


