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

# Solution
