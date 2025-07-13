# Question

Given an integer array, nums, and an interger, val, remove all occurances of val in nums (in-place).
The order of the elements may be changed. Return the number of elements in nums which are not equal
to val.

Consider: number of elements in nums which are not equal to val to be k, to get accepted must do the
following things:

- Change the array nums so that the first k elements of nums contains the elements which are not
  equal to val. The remaining elements of nums are not important as well as the size of nums.
- Return k.

# Thinking

- It seems like this is part of a sorting solution.
- We might be able to solve this problem by using a sequence of swaps, where loop through the array
  and then swap the current element (if it is val) with the end element. We keep two pointers - the
  pointer to the current element and the pointer of the next element we can swap to. The problem is
  done when the two pointers are the same.
- To finish the problem, we'll also need a counter, which counts how often we see a numbers that are
  not val.
- Consider a test case: `[3, 2, 2, 3]` with `val = 3`
  - `start = [3], remainder: [2, 2, 3]`
  -  is element 3?
    - Yes
      - We wish to move the element somewhere else in the array, and then keep track that we saw an
        instance of val. We also don't want to overcount instances of val.
      - If we swap the first and last element, we risk swapping in a value that is "wrong".
      - Maybe we can't solve this with O(N) - which was my original intent.
- Implemented logic where we add a second loop to look up the next item that is not val, and this
  produces arrays that have been "sorted" properly, with val consistently swapped to the end.

---

## Solution Analysis

### 1. User's Solution (`solution.py`)
-   **Approach:** This solution uses a nested loop. The outer loop iterates through the array. When it finds an element equal to `val`, the inner loop searches for the next element that is *not* equal to `val`. It then swaps these two elements. After the loops complete, it performs a final iteration over the modified array to count the number of elements not equal to `val` (which is `k`).
-   **Time Complexity:** `O(n^2)` in the worst case. The nested loop structure means that for each element, it might have to scan a large portion of the remaining array, leading to a quadratic runtime.
-   **Space Complexity:** `O(1)`. The swaps are done in-place, and no extra data structures are used that scale with the input size.

### 2. Optimal Solution (`optimal_solution.py`)
-   **Approach:** This solution uses a two-pointer technique, which is much more efficient. It maintains a "write" pointer `k` that tracks the position for the next element that is not `val`. It iterates through the array with a "read" pointer `i`. If `nums[i]` is not `val`, it's copied to `nums[k]`, and `k` is incremented. This effectively moves all non-`val` elements to the beginning of the array in a single pass.
-   **Time Complexity:** `O(n)`. The solution iterates through the array only once, making it linear in time.
-   **Space Complexity:** `O(1)`. The operation is performed in-place, requiring no additional space.

### Trade-Offs
The user's solution is functionally correct but highly inefficient due to its `O(n^2)` time complexity, making it unsuitable for large arrays. The optimal solution is the standard and highly efficient way to solve this problem. Its single-pass, two-pointer approach is a classic pattern for in-place array manipulations and achieves the best possible time complexity of `O(n)`.