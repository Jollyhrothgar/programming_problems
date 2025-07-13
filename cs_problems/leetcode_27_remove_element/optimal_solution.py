"""An optimal solution for the problem (LeetCode style)."""

from typing import List

class Solution:
  def solve(self, nums: List[int], val: int) -> int:
    # `k` acts as the "write" pointer. It tracks the next position
    # where a non-`val` element should be placed.
    k = 0

    # `i` is the "read" pointer that iterates through the entire array.
    for i in range(len(nums)):
      # If the current element is not the value to be removed...
      if nums[i] != val:
        # ...place it at the `k`-th position.
        nums[k] = nums[i]
        # And move the "write" pointer to the next spot.
        k += 1

    # `k` is now the count of elements that are not `val`.
    print(nums)
    return k

if __name__ == "__main__":
  sol = Solution()
  k = sol.solve(nums=[3, 2, 2, 3], val=3)
  print(k)
  k = sol.solve(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2)
  print(k)
