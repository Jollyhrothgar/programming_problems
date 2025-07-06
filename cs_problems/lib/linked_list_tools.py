"""A very simple linkedlist class definition"""


class ListNode:
  """A simple ListNode class to practice solving problems with LinkedLists."""
  def __init__(self, x):
    self.val = x
    self.next = None


def create_linked_list_with_cycle(values, pos):
  """
  Creates a singly-linked list from a list of values and introduces a cycle.

  Args:
    values: A list of values for the nodes (e.g., [3, 2, 0, -4]).
    pos: The 0-indexed position where the cycle should connect. If -1,
         no cycle is created.

  Returns:
    The head node of the newly created linked list.
  """
  if not values:
    return None

  # Create all the nodes first and store them in a list for easy access.
  nodes = [ListNode(val) for val in values]
  head = nodes[0]

  # Link the nodes together in a chain.
  for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i+1]

  # Create the cycle if a valid position is given.
  if pos != -1 and pos < len(nodes):
    last_node = nodes[-1]
    cycle_node = nodes[pos]
    last_node.next = cycle_node

  return head
