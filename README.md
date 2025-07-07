# Code Practice: A Curated Collection of Problems & Solutions

This repository contains a collection of programming problems, complete with standard and optimized solutions. It serves as a practical guide to understanding key computer science concepts and trade-offs in algorithm design.

Each problem is self-contained in its own directory and includes:
- A clear problem description (`README.md`).
- A standard or brute-force solution (`solution.py`).
- An optimized solution (`optimal_solution.py`).
- A detailed analysis of both approaches, including time and space complexity.

## Conceptual Guide

This section categorizes the problems by the primary computer science concepts they demonstrate.

### Arrays

- **[Merge Sorted Array (LeetCode 88)](./cs_problems/merge_sorted_array_leetcode_88/)**
  - **Concept:** In-place merging of two sorted arrays.
  - **Key Algorithm:** Three-pointer technique for efficient, O(1) space merging.

### Linked Lists

- **[Linked List Cycle (LeetCode 141)](./cs_problems/linked_list_cycle_leetcode_141/)**
  - **Concept:** Cycle detection in a linked list.
  - **Key Algorithm:** Floyd's "Tortoise and Hare" cycle-finding algorithm.

### Dynamic Programming

- **[FizzBuzz Sum](./cs_problems/fizz_buzz_sum/)**
  - **Concept:** Using tabulation (bottom-up DP) to optimize a summation problem.
  - **Key Algorithm:** Building a memoization table to avoid redundant calculations.

### Number Theory

- **[Base 13 Conversion](./cs_problems/data_lemur_base_13_conversion/)**
  - **Concept:** Converting a number from base-10 to a different base.
  - **Key Algorithm:** Repeatedly using modulo and division to extract digits.
