"""The fancy solution"""
from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
  """
  Merges nums2 into nums1 in-place using a three-pointer approach.

  This optimal solution works backward from the end of both arrays,
  placing the largest elements into the empty space at the end of nums1.

  Time Complexity: O(m + n) because we iterate through both lists once.
  Space Complexity: O(1) because we do not use any extra space.
  """
  # Pointer for the last element of the initial part of nums1
  p1 = m - 1
  # Pointer for the last element of nums2
  p2 = n - 1
  # Pointer for the last position in the combined nums1 array
  p_write = m + n - 1

  # Loop backwards as long as there are still elements in nums2 to merge.
  while p2 >= 0:
    # If p1 is still valid and its value is larger than p2's value...
    if p1 >= 0 and nums1[p1] > nums2[p2]:
      # Place the larger element from nums1 at the write position.
      nums1[p_write] = nums1[p1]
      # Move the nums1 pointer to the left.
      p1 -= 1
    else:
      # Otherwise, the element from nums2 is larger or p1 is exhausted.
      # Place the element from nums2 at the write position.
      nums1[p_write] = nums2[p2]
      # Move the nums2 pointer to the left.
      p2 -= 1
    
    # Move the write position to the left for the next element.
    p_write -= 1
  return nums1
