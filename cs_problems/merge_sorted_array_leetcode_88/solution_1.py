"""The stupid space inefficient solution."""
from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
  """
  Merges the elements of nums2 into nums1 in place.

  Args:
    nums1 - List of ascending integers with zero padding to account for nums2
    m - Number of non-zero entries in nums1.
    nums2 - List of ascending integers.
    n - Number of entries in nums2.

  Returns
    nums1 (after merge)
  """

  # Shit solution:
  final_list = sorted(nums1[:m] + nums2)
  for i in range(m+n):
    nums1[i] = final_list[i]
  return nums1

