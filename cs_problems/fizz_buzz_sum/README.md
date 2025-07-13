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

---

## Suggested Solution Analysis

### 1. User's Solution (`solution.py`)
-   **Approach:** This solution iterates from 3 up to the target number. For each number, it checks if it is a multiple of 3 or 5 (or both). If it is, the number is added to a list. Finally, it computes the sum of this list. The result for each target is stored in a `memory` dictionary (memoization) to avoid re-computation if the same target is requested again.
-   **Time Complexity:** `O(n)` for the first call with a given `n`. The loop runs up to `n` times. For subsequent calls with the same `n`, the complexity is `O(1)` due to the cache hit.
-   **Space Complexity:** `O(n)` in the worst case for the `factors` list, which can store a significant number of multiples. The `memory` cache also contributes to space complexity over multiple calls.

### 2. Optimal Solution (`optimal_solution.py`)
-   **Approach:** This solution uses a more advanced dynamic programming technique called tabulation (a bottom-up approach). It builds a `memory` table that stores the cumulative sum of multiples up to each number. When called with a new `target`, it starts from the highest number it has already calculated (`last_known_target`) and iteratively computes the sum up to the new `target`. This avoids re-evaluating numbers that have already been processed in previous calls for smaller targets.
-   **Time Complexity:** `O(n - k)`, where `n` is the new target and `k` is the `last_known_target`. If the function is called sequentially with increasing targets (e.g., 10, 11, 12), each subsequent call is nearly `O(1)`. The initial call is `O(n)`.
-   **Space Complexity:** `O(n)` because the `memory` dictionary stores the sum for every number up to the maximum target requested.

### Trade-Offs
The user's solution is a good attempt at optimization with memoization, but it is inefficient for sequential calls with increasing targets (e.g., `fizz_buzz_sum(10)` then `fizz_buzz_sum(11)`), as it re-computes the entire list of factors each time. The optimal solution is significantly more efficient for this sequential pattern because it builds upon its previous work. However, the optimal solution's memory usage is higher as it stores the sum for every intermediate value, whereas the user's solution only stores the final sum for each target in its cache.
