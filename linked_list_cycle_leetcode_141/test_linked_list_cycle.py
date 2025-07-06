from linked_list_cycle_leetcode_141.linked_list_cycle import has_cycle
from lib.linked_list_tools import ListNode
from lib.linked_list_tools import create_linked_list_with_cycle


def test_solution():
  assert has_cycle(create_linked_list_with_cycle(values=[3,2,0,-4], pos = 1)) == True


def test_solution_no_cycle():
  assert has_cycle(create_linked_list_with_cycle(values=[1,2], pos = -1)) == False


def test_solution_one_node():
  assert has_cycle(create_linked_list_with_cycle(values=[1], pos = -1)) == False
