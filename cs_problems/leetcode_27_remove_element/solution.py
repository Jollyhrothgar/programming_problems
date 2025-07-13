"""A standard solution for the problem (LeetCode style)."""

from typing import List

class Solution:
  def solve(self, nums: List[int], val:int) -> int:
    # Initialize pointers for legibility.
    start = 1
    end = len(nums) - 1
    k = 0

    for i in range(end+1):
      if nums[i] == val:
        # find the next value in the array that is NOT val, and swap.
        for j in range(i+1, end+1):
          if nums[j] != val:
            right_val = nums[i]
            left_val = nums[j]

            nums[i] = left_val
            nums[j] = right_val

            break
    # Add one more linear execution to count k
    for elem in nums:
      if elem != val:
        k+=1

    print(nums)
    return k

if __name__ == "__main__":
  sol = Solution()
  k = sol.solve(nums=[3, 2, 2, 3], val=3)
  print(k)
  k = sol.solve(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2)
  print(k)
