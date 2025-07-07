from . import solution_1
from . import optimal_solution_1

def test_trivial_case_1():
  assert solution_1.merge(nums1=[0], m=0, nums2=[1], n=1) == [1]

def test_trivial_case_2():
  assert solution_1.merge(nums1=[0, 0, 0], m=0, nums2=[1, 2, 3], n=3) == [1, 2, 3]

def test_trivial_case_3():
  assert solution_1.merge(nums1=[1, 2, 0], m=2, nums2=[1], n=1) == [1, 1, 2]

def test_case_1():
  assert solution_1.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3) == [1,2,2,3,5,6]

def test_optimal_1():
  assert optimal_solution_1.merge(nums1=[0], m=0, nums2=[1], n=1) == [1]

def test_optimal_2():
  assert optimal_solution_1.merge(nums1=[0, 0, 0], m=0, nums2=[1, 2, 3], n=3) == [1, 2, 3]

def test_optimal_3():
  assert optimal_solution_1.merge(nums1=[1, 2, 0], m=2, nums2=[1], n=1) == [1, 1, 2]

def test_optimal_4():
  assert optimal_solution_1.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3) == [1,2,2,3,5,6]
