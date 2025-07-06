from linked_list_cycle_leetcode_141.solution import has_cycle as my_solution
from linked_list_cycle_leetcode_141.optimal_solution import has_cycle as optimal_solution
from lib.linked_list_tools import ListNode
from lib.linked_list_tools import create_linked_list_with_cycle

print("Testing basic solution")

def test_solution():
  assert my_solution(create_linked_list_with_cycle(values=[3,2,0,-4], pos = 1)) == True


def test_solution_no_cycle():
  assert my_solution(create_linked_list_with_cycle(values=[1,2], pos = -1)) == False


def test_solution_one_node():
  assert my_solution(create_linked_list_with_cycle(values=[1], pos = -1)) == False


print("Testing optimal solution")

def test_optimal_solution():
  assert optimal_solution(create_linked_list_with_cycle(values=[3,2,0,-4], pos = 1)) == True


def test_optimal_solution_no_cycle():
  assert optimal_solution(create_linked_list_with_cycle(values=[1,2], pos = -1)) == False


def test_optimal_solution_one_node():
  assert optimal_solution(create_linked_list_with_cycle(values=[1], pos = -1)) == False