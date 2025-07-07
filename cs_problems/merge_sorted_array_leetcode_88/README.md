# Question

You are given two integer arrays nums1 and nums2, sorted in non-decreasing
order, and two integers m and n, representing the number of elements in nums1
and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be
stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged, and the
last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Thinking

- The challenge of this problem is to use no additional memory to produce a final sorted array.
- We know that nums1 and nums2 have been pre-sorted (in ascending order).
- We'll keep the sorting schema (ascending).
- There's a dumb N^2 solution we could use where we just push everything back until we're done.

---

## Solution Analysis

### 1. Standard Solution (`solution_1.py`)
-   **Approach:** This solution takes a simple, yet inefficient approach. It slices the meaningful elements from `nums1` (the first `m` elements), concatenates `nums2`, sorts the resulting new list, and then copies the elements back into `nums1`.
-   **Time Complexity:** `O((m+n) log(m+n))` - The dominant operation is sorting the combined list of `m+n` elements.
-   **Space Complexity:** `O(m+n)` - An entirely new list is created in memory to hold the combined elements before sorting.

### 2. Optimal Solution (`optimal_solution_1.py`)
-   **Approach:** The optimal solution uses a three-pointer, in-place merge strategy. It starts from the end of both arrays and the end of the `nums1` buffer. It compares the elements at the pointers of `nums1` and `nums2` and places the larger of the two at the end of `nums1`, moving the corresponding pointers backward. This avoids overwriting elements in `nums1` that haven't been compared yet.
-   **Time Complexity:** `O(m+n)` - Each element from `nums1` and `nums2` is visited and compared exactly once.
-   **Space Complexity:** `O(1)` - The merge operation is done in-place, using only a few pointers for tracking, thus requiring no extra space.

### Trade-Offs
The standard solution is very easy to write and understand, but it's highly inefficient in terms of both time and space, failing to meet the implicit constraints of a good solution for this kind of problem. The optimal solution is more complex to reason about but is significantly more performant, using constant extra space, which is crucial for large datasets.
