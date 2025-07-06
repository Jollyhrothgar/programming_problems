# Question

Write a function `fizz_buzz_sum` to find the sum of all multiples of 3 or 5 below a target value.

For example, if the target value was 10, the multiples of 3 or 5 below 10 are 3, 5, 6, and 9.

Because 3 + 5 + 6 + 9 = 23, our function would return 23.

# Thinking

- We could create two helper functions "is multiple of three" and "is multiple of five" and then
  return the list of factors.
- Some multiples may be a multiple of both 3 and 5 - in those cases, the helper functions will
  return duplicate numbers - for example, if the number is 16, one of the factors will be 15.
- This could be a dynamic programming problem, because each subsequent call to this function will
  comprise all previously solved instances. For example - if the user or system called
  `fizz_buzz_sum(10)` and then subsequently calls `fizz_buzz_sum(11)`, we can use the result of
  `fizz_buzz_sum(10)` and then only check new factors. However, this is maybe a bad example, because
  11 is a prime number.

---

## Solution Analysis

### 1. Standard Solution (`solution.py`)
-   **Approach:** This solution iterates from 3 up to the target value. For each number, it checks if it's a multiple of 3 or 5 and, if so, adds it to a list of factors. The sum of this list is then returned. The results are memoized to avoid re-computation for the same target.
-   **Time Complexity:** `O(n)` - The loop runs from 3 to `n` (the target), so the time taken is directly proportional to the target value.
-   **Space Complexity:** `O(n)` - In the worst case, the `factors` list can grow to a size proportional to `n`.

### 2. Optimal Solution (`optimal_solution.py`)
-   **Approach:** The optimal solution uses a bottom-up dynamic programming approach (tabulation). It builds a table (`memory`) storing the sum of multiples up to each number from 0 to the target. It computes the sum for a target `i` by taking the already computed sum for `i-1` and adding `i-1` to it if `i-1` is a multiple of 3 or 5. This avoids redundant calculations when the function is called with increasing targets.
-   **Time Complexity:** `O(n)` - Where `n` is the difference between the current target and the largest previously computed target. In the best case (a cache hit), it's `O(1)`.
-   **Space Complexity:** `O(n)` - The `memory` dictionary stores the sum for each number up to the target, leading to space usage proportional to `n`.

### Trade-Offs
The standard solution is straightforward but inefficient if called multiple times, as it re-computes the entire sum each time for a new target. The optimal solution is much more efficient for sequential or repeated calls with increasing targets because it leverages past results. However, it has a higher memory footprint as it stores the intermediate sums for all numbers up to the target.
