#!/bin/bash

# A script to display a clean, readable directory tree, ignoring common
# virtual environment, cache, and version control directories.

# --- 1. Check for `tree` command ---
# The 'tree' command is not installed on macOS by default. This check
# verifies if the command exists in the user's PATH.
if ! command -v tree &> /dev/null
then
    echo "Error: 'tree' command not found."
    echo "This script requires the 'tree' utility."
    echo "On macOS, you can install it using Homebrew:"
    echo "brew install tree"
    exit 1
fi

# --- 2. Determine Target Directory ---
# Use the first argument as the target directory. If no argument is
# provided, default to the current directory ('.').
TARGET_DIR=${1:-.}

# Check if the target directory actually exists.
if [ ! -d "$TARGET_DIR" ]; then
  echo "Error: Directory '$TARGET_DIR' not found."
  exit 1
fi

# --- 3. Define Ignore Pattern ---
# The -I flag for 'tree' takes a pipe-separated list of patterns to ignore.
# We are ignoring common Python, Git, and pytest artifacts.
IGNORE_PATTERN="venv|__pycache__|.git|.pytest_cache"

# --- 4. Execute and Display Tree ---
echo "Displaying tree for: $TARGET_DIR"
echo "Ignoring: $IGNORE_PATTERN"
echo "--------------------------------------------------"

# -a:         List all files, including hidden ones (like .DS_Store if not ignored)
# -I PATTERN: Exclude files/directories matching the pattern.
tree -a -I "$IGNORE_PATTERN" "$TARGET_DIR"


