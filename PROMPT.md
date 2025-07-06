## CONTEXT
You will be analyzing a repository located at the current path (`.`). This repository contains a series of programming practice problems, where each problem is contained within its own subdirectory inside `cs_problems/`.

The structure for a typical problem directory (e.g., `cs_problems/fizz_buzz_sum/`) is:
- `README.md`: Contains a "Question" and "Thinking" section. This file will be MODIFIED by you.
- `solution.py`: Contains a standard or brute-force solution.
- `optimal_solution.py`: (Optional) Contains a more optimized solution.
- `test_*.py`: Contains test cases.

## PERSONA
Act as an expert software engineer and technical writer. Your goal is to create clear, concise documentation for each solution and then generate a high-level conceptual guide for the entire repository.

## TASKS & STEP-BY-STEP PROCESS

### Task 1: Document Individual Solutions
For each problem subdirectory within `cs_problems/`:
1.  **Analyze Solutions:** Read and understand the code in `solution.py` and, if it exists, `optimal_solution.py`.
2.  **Identify Approaches:** Determine the algorithm, data structures, time complexity, and space complexity for each solution. Note the key differences between the standard and optimal approaches.
3.  **Generate Documentation:** Create a new "Solution Analysis" section in Markdown format. Use the template provided below.
4.  **Update README.md:** Read the existing `README.md` in the problem's directory. Preserve the "Question" and "Thinking" sections, but **replace** the old "Solution" section (if any) with your newly generated "Solution Analysis".

### Task 2: Generate Top-Level Conceptual Guide
After all individual READMEs have been updated:
1.  **Build Conceptual Map:** Using the knowledge gathered from all problems, create an internal map where keys are CS concepts (e.g., "Linked Lists," "Dynamic Programming") and values are the problems that exemplify them.
2.  **Generate Top-Level README:** Create a single `README.md` file at the repository root, using the "Top-Level README Template" provided below. This file should serve as a high-level, clickable guide to the concepts demonstrated in the repository.

## OUTPUT FORMAT AND CONSTRAINTS
-   You WILL modify the `README.md` file inside each problem subdirectory.
-   You WILL create ONE new file at the root of the repository: `README.md`.
-   All links MUST be relative and clickable on GitHub.
-   The tone should be helpful, educational, and professional.

---

## TEMPLATES

### Template for "Solution Analysis" Section (for sub-directory READMEs)
````markdown
---

## Solution Analysis

### 1. Standard Solution (`solution.py`)
-   **Approach:** A brief description of the algorithm used. For example, "This solution uses a hash set to keep track of visited nodes. It iterates through the list, adding each node to the set. If a node is encountered that is already in the set, a cycle is detected."
-   **Time Complexity:** `O(n)` - Explain why (e.g., "as we visit each of the n nodes at most once").
-   **Space Complexity:** `O(n)` - Explain why (e.g., "as in the worst case, the hash set will store all n nodes").

### 2. Optimal Solution (`optimal_solution.py`)
-   **Approach:** A description of the optimized algorithm. For example, "The optimal solution uses the 'Tortoise and Hare' (Floyd's Cycle-Finding) algorithm. It uses two pointers, a slow pointer that moves one step at a time and a fast pointer that moves two steps. If the pointers ever meet, a cycle exists."
-   **Time Complexity:** `O(n)` - Explain why.
-   **Space Complexity:** `O(1)` - Explain why (e.g., "as it only uses two pointers and requires no extra data structures").

### Trade-Offs
A brief comparison. For example, "The standard solution is intuitive and easy to understand but uses extra memory that scales with the input size. The optimal solution is more clever and uses constant memory, making it far more efficient for very large inputs."

