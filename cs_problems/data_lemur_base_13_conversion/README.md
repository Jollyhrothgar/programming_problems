# Question

Given an integer num, return its string representation in base 13.

In case you don’t use base 13 that much (who does, right?), here’s a quick
rundown: just like base 10 uses digits from 0 to 9. But also for 10, 11 and 12,
we use the letters A, B, and C.

For example:

9 in base 13 is still "9"
10 in base 13 is "A"
11 in base 13 is "B"
12 in base 13 is "C"
13 in base 13 is "10"
14 in base 13 is "11"
49 in base 13 is "3A" (since 3 _ 13 + 10 = 493 _ 13 + 10 = 49)
69 in base 13 is "54" (since 5 _ 13 + 4 = 69 5 _ 13 + 4 = 69)

# Thinking

- Let's define what base 13 means: it means that you write numbers as (13)^N +
  ... (13)^3 + (13)^2 + (13)^1 + (13)^0, with each place value having a
  coefficient of how many times it appears, and now we represent a coefficient as
  a digit (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A=10, B=11, C=12).
- The issue with any number is that they are unbounded. And with string
  repreesentations, we have basically unlimited precision. So, we'll make some
  assuptions about the precision of the number.
- We'll assume up to a 5 digit base 13 number and add more precision as we
  discover issues.

---

## Solution Analysis

### 1. User's Solution (`solution.py`)
-   **Approach:** This solution iterates from a large, fixed power of 13 down to 0. For each power, it calculates how many times the corresponding place value fits into the remaining number. This determines the digit for that position. The number is then reduced by that amount, and the process continues. It builds the base-13 string from left to right.
-   **Time Complexity:** `O(d_max)` where `d_max` is the fixed maximum number of digits (e.g., 10). The loop runs a constant number of times, regardless of the input number's size. This can be seen as `O(1)` if `d_max` is constant, but it's less efficient than an approach that adapts to the input size.
-   **Space Complexity:** `O(d_max)` for the resulting string.

### 2. Optimal Solution (`optimal_solution.py`)
-   **Approach:** This solution uses the classic algorithm of repeated division and modulo. It finds the rightmost digit by taking the number `modulo 13`. It then "shifts" to the next digit by performing integer division of the number by 13. This process repeats until the number is 0. The digits are collected and prepended to build the final string.
-   **Time Complexity:** `O(log_13(n))` or `O(d)`, where `d` is the actual number of digits in the base-13 representation of `n`. The number of loop iterations is proportional to the number of digits.
-   **Space Complexity:** `O(d)` to store the resulting string.

### Trade-Offs
The user's solution is conceptually straightforward but has a few drawbacks. It assumes a maximum number of digits, which can be inefficient for small numbers and will fail for numbers that exceed this precision. It also involves more complex calculations within the loop. The optimal solution is the standard, most efficient method for base conversion. It's elegant, concise, and handles numbers of any size gracefully, making it the preferred approach.
