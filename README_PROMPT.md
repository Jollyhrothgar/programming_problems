## CONTEXT
You will be analyzing a repository located at the current path (`.`). This repository contains a
series of programming practice problems, where each problem is contained within its own
subdirectory.

The structure for a typical problem directory (e.g., `fizz_buzz_sum/`) is:
- `README.md`: Contains the problem description and my thought process.
- `problem_name.py`: Contains a solution to the problem.
- `problem_name_optimal.py`: (Optional) Contains a more optimized solution.
- `test_problem_name.py`: Contains test cases for the solution(s).

## PERSONA
Act as an expert software engineer and technical writer tasked with creating a high-level conceptual
guide for this practice repository. Your goal is to make the repository easily navigable for a
developer studying for technical interviews.

## TASK
Your primary task is to generate a single, top-level `README.md` file that serves as a conceptual
map of all the problems solved in this repository.

## STEP-BY-STEP PROCESS
1.  **Scan & Analyze:** Recursively scan all subdirectories. For each problem directory, read the
    contents of its `README.md`, `*.py` solution files, and `test_*.py` files.
2.  **Identify Concepts:** From the content you read, identify the key computer science concepts,
    data structures, and algorithmic patterns used. Examples include "Dynamic Programming,"
    "Memoization," "Linked Lists," "Hash Set," "Two Pointers," etc. A single problem can be
    associated with multiple concepts.
3.  **Build Internal Map:** Before writing, create an internal map where keys are the identified
    concepts and values are a list of the problems that exemplify that concept.
4.  **Generate README:** Using your internal map, generate the `README.md` file according to the
    format specified below.

## OUTPUT FORMAT AND CONSTRAINTS
-   You MUST only create ONE file at the root of the repository: `README.md`.
-   You MUST NOT modify any other files.
-   All links to problem directories MUST be relative and clickable on GitHub.
-   The tone should be helpful and educational.

---

### README.md Template and Example

Use the following Markdown structure. Here is an example of the desired output for a few concepts:

````markdown
# Computer Science Problem-Solving Guide

This repository contains a collection of solved programming problems, organized by computer science
concepts to aid in studying for technical interviews.

---

## Table of Contents
    * [Data Structures](#data-structures)
* [Algorithmic Patterns](#algorithmic-patterns)

    ---

## Data Structures

### Linked Lists
A linear data structure where elements are not stored at contiguous memory locations but are
linked using pointers. Each node contains data and a reference (or link) to the next node in the
sequence.

-   **[Linked List Cycle Detection](./linked_list_cycle_leetcode_141/)**: An example of identifying
    cycles using the fast and slow pointer technique.

### Hash Sets

A data structure that stores a collection of unique items in an unordered fashion. It provides
highly efficient (average O(1) time complexity) lookups, insertions, and deletions.

-   **[Linked List Cycle Detection](./linked_list_cycle_leetcode_141/)**: Demonstrates using a hash
    set to track visited nodes to detect a cycle.

---

## Algorithmic Patterns

### Dynamic Programming & Memoization
    A method for solving complex problems by breaking them down into simpler, overlapping subproblems. Results of subproblems are stored (memoized) to avoid redundant calculations.

    -   **[Fizz Buzz Sum](./fizz_buzz_sum/)**: A bottom-up dynamic programming approach to build a solution iteratively.


