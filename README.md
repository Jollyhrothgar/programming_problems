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