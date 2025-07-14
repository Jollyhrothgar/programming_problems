"""Recursive implementation of summing a list"""
import sys
import math

def sum_list(nums):
  if len(nums) == 0:
    return 0
  print(f"{nums[0]}")
  return nums[0] + sum_list(nums[1:])

if __name__ == '__main__':
  nums = [int(i) for i in (sys.argv[1]).split(",")]
  test = sum(nums)
  result = sum_list(nums)
  print(f"Processing list {nums}. Success: {test == result}")
