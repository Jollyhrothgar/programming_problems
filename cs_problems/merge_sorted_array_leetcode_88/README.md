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

---

## Suggested Solution Analysis

### 1. User's Solution (`solution_1.py`)
-   **Approach:** This solution takes a straightforward but inefficient approach. It first creates a new list by concatenating the significant elements of `nums1` (the first `m` elements) and all of `nums2`. It then sorts this new, combined list. Finally, it iterates through the sorted list and copies its elements back into the original `nums1` array.
-   **Time Complexity:** `O((m+n) log(m+n))`. The dominant operation is the sort function called on the combined list of `m+n` elements.
-   **Space Complexity:** `O(m+n)`. A new list is created to hold all `m+n` elements, which requires memory proportional to the total number of elements.

### 2. Optimal Solution (`optimal_solution_1.py`)
-   **Approach:** The optimal solution uses a clever, in-place, three-pointer technique. It works backward from the end of the arrays. One pointer (`p1`) tracks the last valid element of `nums1`, another (`p2`) tracks the last element of `nums2`, and a third (`p_write`) tracks the position in `nums1` where the next largest element should be written (starting from the very end). By comparing `nums1[p1]` and `nums2[p2]` and placing the larger one at `nums1[p_write]`, it correctly merges the arrays without needing extra space and without overwriting un-inspected elements.
-   **Time Complexity:** `O(m+n)`. Each element is examined and placed exactly once, resulting in a linear runtime.
-   **Space Complexity:** `O(1)`. The merge is performed in-place within the `nums1` array, using only a few pointers. This is the most significant advantage.

### Trade-Offs
The user's solution is simple to understand but fails to meet the typical constraints of this problem, which usually imply an in-place, efficient solution. Its high space and time complexity make it impractical for large inputs. The optimal solution is the standard, accepted way to solve this problem. It is significantly more efficient and demonstrates a strong understanding of array manipulation and in-place algorithms, which is often what interviewers are looking for.
