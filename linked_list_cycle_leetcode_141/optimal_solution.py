"""Solution for the linked list cycle problem using a visited set."""

from lib.linked_list_tools import ListNode
from typing import Optional

def has_cycle(head: Optional[ListNode]) -> bool:
  """
  Determines if a linked list has a cycle by tracking visited nodes.

  This solution has a time complexity of O(n) and a space complexity of O(n),
  where n is the number of nodes in the list.
  """
  visited_nodes = set()
  current_node = head

  # Loop as long as we haven't reached the end of the list.
  while current_node:
    # If we've seen this node object before, we've found a cycle.
    if current_node in visited_nodes:
      return True
    
    # If not, add the current node to our set of visited nodes.
    visited_nodes.add(current_node)
    
    # Move to the next node in the list.
    current_node = current_node.next
  
  # If the loop finishes, it means we reached the end (None), so no cycle exists.
  return False